package main

import (
	"fmt"
	"net"
	"os"
	"time"
)

func main() {
	os.Remove("../test.sock")

	ssock, err := net.Listen("unix", "../test.sock")
	if err != nil {
		panic(err.Error())
	}
	defer ssock.Close()

	socks := make([]net.Conn, 0)
	defer func() {
		for _, sock := range socks {
			sock.Close()
		}
	}()
	defer os.Remove("../test.sock")

	go func() {
		for {
			sock, err := ssock.Accept()
			if err != nil {
				panic(err.Error())
			}
			fmt.Println("incomming connection")
			socks = append(socks, sock)
		}
	}()

	count := 0
	state := false
	for {
		state = !state
		if state {
			count++
		}

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
		time.Sleep(1 * time.Second)
	}
}
