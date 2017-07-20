ドアの状況を見るためのライブラリ
================================

とりあえずイベントを受け取れるだけで、現在の状況を取ったりは出来ない。

## サンプル
``` go
package main

import (
	"fmt"

	"github.com/lc-tut/404room/local/libs/go/door"
)

func main() {
	conn, err := door.Dial(door.DEFAULT_PATH)
	if err != nil {
		panic(err.Error())
	}
	defer conn.Close()

	conn.Watch(func(state door.State) {
		fmt.Println(state)
	})
}
```
