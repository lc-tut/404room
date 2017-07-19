package main

import (
	"fmt"
	"os/exec"

	"github.com/lc-tut/404room/local/libs/go/door"
)

var (
	COMMAND = "/home/pi/door_event.bash"
)

func main() {
	conn, err := door.Dial(door.DEFAULT_PATH)
	if err != nil {
		panic(err.Error())
	}
	defer conn.Close()

	conn.Watch(func(state door.State) {
		exec.Command("/bin/bash", COMMAND, state.OpenedStr(), fmt.Sprintf("%d", state.Count)).Run()
	})
}
