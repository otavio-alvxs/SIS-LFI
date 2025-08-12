package	main

import "fmt"

func main() {
	a := 1
	b := 0
	for i := 0; i < 20; i++ {
		fmt.Println(a)
		c:= a + b
		a = b
		b = c
	}
}
