package main

import (
	"fmt"
	"net"
	"os"
	"time"

	"github.com/davecheney/gpio"
	"github.com/davecheney/gpio/rpi"
)

var (
	SENSOR_PIN = 4
	SOCKET     = "test.sock"
)

func main() {
	os.Remove(SOCKET)

	sensor, err := rpi.OpenPin(SENSOR_PIN, gpio.ModeInput)
	if err != nil {
		panic(err.Error())
	}
	defer sensor.Close()

	ssock, err := net.Listen("unix", SOCKET)
	if err != nil {
		panic(err.Error())
	}
	os.Chmod(SOCKET, os.ModeSocket|0777)
	defer ssock.Close()

	socks := make([]net.Conn, 0)
	defer func() {
		for _, sock := range socks {
			sock.Close()
		}
	}()
	defer os.Remove(SOCKET)

	count := 0
	state := false

	sendState := func() {
		stateChar := 'C'
		if state {
			stateChar = 'O'
		}

		var closed []net.Conn
		for _, sock := range socks {
			_, err := fmt.Fprintf(sock, "%c%d\n", stateChar, count)

			if err != nil {
				fmt.Println("Closed connection")
				closed = append(closed, sock)
			}
		}

		if closed != nil {
			remains := make([]net.Conn, 0)
			for _, s := range socks {
				for _, c := range closed {
					if s != c {
						remains = append(remains, s)
					}
				}
			}
			socks = remains
		}

		stateStr := "CLOSE"
		if state {
			stateStr = "OPEN"
		}
		fmt.Printf("%d client(s): %s\n", len(socks), stateStr)
	}

	var lastTime int64 = 0
	sensor.BeginWatch(gpio.EdgeBoth, func() {
		now := time.Now().UnixNano()
		if lastTime+500*1000 < now {
			lastTime = now

			//state = !sensor.Get()
			state = !state
			if state {
				count++
			}

			sendState()
		}
	})
	defer sensor.EndWatch()

	for {
		sock, err := ssock.Accept()
		if err != nil {
			panic(err.Error())
		}
		fmt.Println("Incomming connection")
		socks = append(socks, sock)
	}
}
