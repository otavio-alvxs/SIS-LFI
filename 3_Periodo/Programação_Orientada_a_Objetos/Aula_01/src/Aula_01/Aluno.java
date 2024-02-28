package Aula_01;

public class Aluno {
	String nome;
	double nota1;
	double nota2;
	double media;
	void cadastraAluno(String novoAluno) {
		nome = novoAluno;
	}
	void cadastraNotas (double n1, double n2) {
		nota1 = n1;
		nota2 = n2;
	}
	void calculaMedia() {
		media = (nota1 + nota2) / 2;
	}
	String retornaMedia() {
		return "Francisco sua média foi: " + media;
	}
}
