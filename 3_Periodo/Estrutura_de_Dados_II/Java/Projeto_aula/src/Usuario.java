public class Usuario {
    private int id;
    private String nome;
    private String email;

    public Usuario(String nome, String email) {
        this.setNome(nome);
        this.setEmail(email);
    }

    public void setId(int id) {
        this.id = id;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public int getId() {
        return this.id;
    }

    public String getNome() {
        return nome;
    }

    public String getEmail() {
        return email;
    }

    public String toString() {
        return "Id: " + getId() + " Nome: " + getNome() + " E-mail: " + getEmail();
    }

}
