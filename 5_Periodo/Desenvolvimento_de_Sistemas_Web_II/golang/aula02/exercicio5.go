package main

import "fmt"

func main() {
	numero := 5
	
	for i := numero; i >= 1; i-- {
		numero = numero * i
	}

	fmt.println(numero)
}