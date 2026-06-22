package arvoreLivros;

public class No {
    Livro livro;
    No esquerdo;
    No direito;
    
    public No(Livro livro) {
        this.livro = livro;
        this.esquerdo = null;
        this.direito = null;
    }
}