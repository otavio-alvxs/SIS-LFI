package	main

import "fmt"

func main() {
	preco := 100
	var quantidade float64
	quantidade = 50

	total := preco * quantidade
	if (quantidade >= 5) {
		total = total - (total * 0.1)
	}

	fmt.Println("Total: R$", total)
}