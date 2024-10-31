package org.libertas;

public class Retorno {
	private boolean Sucesso;
	private String Mensagem;
	
	public boolean isSucesso() {
		return Sucesso;
	}
	public void setSucesso(boolean sucesso) {
		Sucesso = sucesso;
	}
	public String getMensagem() {
		return Mensagem;
	}
	public void setMensagem(String mensagem) {
		Mensagem = mensagem;
	}
	
	public void Mensagem(Retorno r) {
		if (Sucesso == true) {
			r.setMensagem("Opearacao realizada");
		} else {
			r.setMensagem("Operacao Falhou");
		}
	}
}
