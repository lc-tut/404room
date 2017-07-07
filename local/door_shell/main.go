package main

import (
	"fmt"
	"net"
	"os/exec"
)

var (
	COMMAND = "/home/pi/door_event.sh"
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
	con, err := net.Dial("unix", "/tmp/door.sock")
	if err != nil {
		panic(err.Error())
	}
	defer con.Close()

	for {
		var state State
		var stateChar rune
		if _, err = fmt.Fscanf(con, "%c%d", &stateChar, &state.Count); err != nil {
			continue
		}
		state.Opened = stateChar == 'O'

		exec.Command("/bin/sh", COMMAND, state.OpenedStr(), fmt.Sprintf("%d", state.Count)).Run()
	}
}
