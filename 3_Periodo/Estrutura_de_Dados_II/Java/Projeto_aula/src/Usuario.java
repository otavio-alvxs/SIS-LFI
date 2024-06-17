public class Usuario {
    private int id;
    private String nome;
    private String email;
    private static int contador = 0;

    public Usuario(String nome, String email) {
        this.setNome(nome);
        this.setEmail(email);
        
        contador += 1;
        this.setId(contador);
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getNome() {
        return nome;
    }

    public String getEmail() {
        return email;
    }

    public int getId() {
        return this.id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String toString() {
        return "Id: " + getId() + " Nome: " + getNome() + " E-mail: " + getEmail();
    }

}
