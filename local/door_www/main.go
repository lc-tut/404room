package main

import (
	"net/http"
	"fmt"
	"net"
	"time"

	"golang.org/x/net/websocket"
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

func main() {
	con, err := net.Dial("unix", "../test.sock")
	if err != nil {
		panic(err.Error())
	}
	defer con.Close()

	var connections []*websocket.Conn

	stateUpdated := make(chan State)
	var state State
	go func() {
		for {
			var stateChar rune
			if _, err = fmt.Fscanf(con, "%c%d", &stateChar, &state.Count); err != nil {
				continue
			}
			state.Opened = stateChar == 'O'

			stateUpdated <- state
		}
	}()

	http.Handle("/", http.FileServer(http.Dir("static")))

	http.Handle("/socket", websocket.Handler(func(ws *websocket.Conn) {
		fmt.Fprintf(ws, `{"type": "%s", "count": %d}`, state.OpenedStr(), state.Count)

		connections = append(connections, ws)

		defer func() {
			var droped []*websocket.Conn
			for _, c := range connections {
				if c != ws {
					droped = append(droped, c)
				}
			}
			connections = droped
		}()

		for {
			time.Sleep(5 * time.Minute)
		}
	}))

	go func() {
		for {
			select {
			case s := <-stateUpdated:
				for _, ws := range connections {
					fmt.Fprintf(ws, `{"type": "%s", "count": %d}`, s.OpenedStr(), s.Count)
				}
			}
		}
	}()

	http.ListenAndServe("localhost:8080", nil)
}
