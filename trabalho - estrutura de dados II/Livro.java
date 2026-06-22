package arvoreLivros;

public class Livro implements Comparable<Livro> {
    private String titulo;
    private String autor;
    private int ano;
    public Livro(String titulo, String autor, int ano) {
        this.titulo = titulo;
        this.autor = autor;
        this.ano = ano;
    }
    public String getTitulo() {
        return titulo;
    }
    @Override
    public int compareTo(Livro outro) {
        // ignora maiúsculas/minúsculas pra não acontecer das maiúsculas virem antes das minúsculas
        return this.titulo.compareToIgnoreCase(outro.getTitulo());
    }
    @Override
    public String toString() {
        return String.format("Título: '%s' | Autor: %s | Ano: %d", titulo, autor, ano);
    }
}
