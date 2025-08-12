package main

import "fmt"

func main() {
	numero := 7

	for i := 1; i <= 10; i++ {
		r := numero * i
		fmt.Println(numero, "x", i, "=", r)
	}
}
