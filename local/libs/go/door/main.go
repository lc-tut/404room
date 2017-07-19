package door

import (
	"fmt"
	"net"
	"time"
)

var (
	DEFAULT_PATH     = "/tmp/door.sock"
	ConnectionClosed = fmt.Errorf("connection closed")
)

type State struct {
	Opened bool
	Count  int
}

func (s State) OpenedStr() string {
	if s.Opened {
		return "opened"
	} else {
		return "closed"
	}
}

func (s State) String() string {
	return fmt.Sprintf("Status[%s, %d]", s.OpenedStr(), s.Count)
}

func (s State) ToPacket() string {
	opened := 'C'
	if s.Opened {
		opened = 'O'
	}
	return fmt.Sprintf("%c%d", opened, s.Count)
}

type Conn struct {
	path      string
	conn      net.Conn
	Connected bool
}

func Dial(path string) (*Conn, error) {
	conn, err := net.Dial("unix", path)
	return &Conn{path, conn, true}, err
}

func (conn *Conn) Close() {
	conn.Close()
}

func (conn *Conn) ReConnect() error {
	if conn.Connected {
		conn.conn.Close()
		conn.Connected = false
	}
	c, err := net.Dial("unix", conn.path)
	conn.conn = c
	return err
}

func (conn *Conn) GetStatus() (State, error) {
	var state State
	var stateChar rune

	if _, err := fmt.Fscanf(conn.conn, "%c%d", &stateChar, &state.Count); err != nil {
		return state, ConnectionClosed
	}

	state.Opened = stateChar == 'O'

	return state, nil
}

func (conn *Conn) Watch(callback func(State)) {
	for {
		if state, err := conn.GetStatus(); err != nil {
			for {
				time.Sleep(1 * time.Second)
				if err = conn.ReConnect(); err == nil {
					break
				}
			}
		} else {
			callback(state)
		}
	}
}
