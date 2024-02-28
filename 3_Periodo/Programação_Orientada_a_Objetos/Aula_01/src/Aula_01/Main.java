package Aula_01;

public class Main {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Pessoa pessoa;
		pessoa = new Pessoa();
		pessoa.nome = "Fulano";
		pessoa.idade = 20;
		System.out.println("Olá " + pessoa.nome);
		System.out.println("Sua idade é " + pessoa.idade);
		Aluno aluno1;
		aluno1 = new Aluno();
		aluno1.cadastraAluno("Francisco");
		aluno1.cadastraNotas(7.5, 8.2);
		aluno1.calculaMedia();
		System.out.println(aluno1.retornaMedia());

	}

}
