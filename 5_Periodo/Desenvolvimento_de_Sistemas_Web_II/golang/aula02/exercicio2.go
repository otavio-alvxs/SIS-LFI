package main

import "fmt"

func main() {
	altura := 1.95
	peso := 70.0
	imc := peso / (altura * altura)

	if (imc < 25) {
		fmt.Println("Peso correto com IMC de", imc))
	} else if (imc >= 25) {
		fmt.Println("Sobrepeso com IMC de", imc)
}
