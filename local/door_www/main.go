package main

import (
	"fmt"
	"net/http"
	"time"

	"github.com/lc-tut/404room/local/libs/go/door"
	"golang.org/x/net/websocket"
)

func main() {
	conn, err := door.Dial(door.DEFAULT_PATH)
	if err != nil {
		panic(err.Error())
	}
	defer conn.Close()

	var connections []*websocket.Conn

	stateUpdated := make(chan door.State)
	var state door.State
	go conn.Watch(func(s door.State) {
		state = s
		stateUpdated <- s
	})

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
