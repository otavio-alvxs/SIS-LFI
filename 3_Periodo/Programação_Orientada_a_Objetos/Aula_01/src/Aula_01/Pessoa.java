package Aula_01;

public class Pessoa {
	String nome;
	int idade;
	
	void alteraNome(String novoNome) {
		nome = novoNome;
	}
	String retornaNome() {
		return nome;
	}
	int aumentaIdade(int aumento) {
		int novaIdade = idade + aumento;
			return novaIdade;
	}
}
