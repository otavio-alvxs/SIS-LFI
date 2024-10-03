package org.libertas;

public class Marca{
	private  int IdMarca;
	private String NomeMarca;
	private String Descricao;
	private String Status;
	
	public int getIdMarca() {
		return IdMarca;
	}
	public void setIdMarca(int IdMarca) {
		this.IdMarca = IdMarca;
	}
	public String getNomeMarca() {
		return NomeMarca;
	}
	public void setNomeMarca(String NomeMarca) {
		this.NomeMarca = NomeMarca;
	}
	public String getDescricao() {
		return Descricao;
	}
	public void setDescricao(String Descricao) {
		this.Descricao = Descricao;
	}
	public String getStatus() {
		return Status;
	}
	public void setStatus(String Status) {
		this.Status = Status;
	}
	@Override
	public String toString() {
		return "Marca [IdMarca=" + IdMarca + ", NomeMarca=" + NomeMarca + ", Descricao=" + Descricao + ", Status=" + Status
				+ "]";
	}

	
}
