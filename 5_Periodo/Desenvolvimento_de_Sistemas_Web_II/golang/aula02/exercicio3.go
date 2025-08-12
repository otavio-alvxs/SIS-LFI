package main

import "fmt"

func main() {
	distancia := 100.0
	precoetanol := 3.99
	precogasolina := 5.99
	gastoetanol := distancia / 9 * precoetanol
	gastogasolina := distancia / 11 * precogasolina	
	fmt.Printf("Gasto com etanol: R$", gastoetanol)
	fmt.Println("Gasto com gasolina: R$", gastogasolina)
	if (gastoetanol < gastogasolina) {
		fmt.Println("Etanol compensa muito")
	} else if gastoetanol > gastogasolina {
		fmt.Println("Gasolina compensa muito")
	} else{
		fmt.Println("Qualquer um compensa muito")
	}
}