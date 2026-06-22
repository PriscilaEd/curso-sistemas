package arvoreLivros;

public class ArvoreLivros {
    protected No raiz;
    public ArvoreLivros() {
        this.raiz = null;
    }
    public boolean estaVazia() {
        return this.raiz == null;
    }

    // operação fundamental de inserção
    public void inserir(Livro livro) {
        this.raiz = inserirNo(this.raiz, livro);
    }
    private No inserirNo(No no, Livro livro) {
        if (no == null) {
            return new No(livro);
        }
        if (livro.compareTo(no.livro) < 0) {
            no.esquerdo = inserirNo(no.esquerdo, livro); // chamada recursiva pra esquerda
        } else if (livro.compareTo(no.livro) > 0) {
            no.direito = inserirNo(no.direito, livro); // chamada recursiva pra direita
        }
        return no;
    }

    // operação fundamentao de busca
    public Livro buscar(String titulo) {
        No resultado = buscarNo(this.raiz, titulo);
        return (resultado != null) ? resultado.livro : null;
    }
    private No buscarNo(No no, String titulo) {
        if (no == null || no.livro.getTitulo().equalsIgnoreCase(titulo)) {
            return no;
        }
        if (titulo.compareToIgnoreCase(no.livro.getTitulo()) < 0) {
            return buscarNo(no.esquerdo, titulo);
        }
        return buscarNo(no.direito, titulo);
    }

    // operação fundamental de remoção
    public void remover(String titulo) {
        if (buscar(titulo) == null) {
            System.out.println("Atenção: Livro '" + titulo + "' não encontrado para ser removido!");
            return;
        }
        this.raiz = removerNo(this.raiz, titulo);
        System.out.println("Opa! Livro '" + titulo + "' removido com sucesso!");
    }
    private No removerNo(No no, String titulo) {
        if (no == null) return null;
        if (titulo.compareToIgnoreCase(no.livro.getTitulo()) < 0) {
            no.esquerdo = removerNo(no.esquerdo, titulo);
        } else if (titulo.compareToIgnoreCase(no.livro.getTitulo()) > 0) {
            no.direito = removerNo(no.direito, titulo);
        } else {
            // encontrou o nó a ser removido. tratamento de caso 1 (nó folha) ou caso 2 (apenas um filho direito)
            if (no.esquerdo == null) {
                return no.direito;
            }
            // tratamento de caso 2  (apenas um filho esquerdo)
            else if (no.direito == null) {
                return no.esquerdo;
            }
            // tratamento de caso 3 (nó com dois filhos) / encontra o menor elemento na subárvore direita
            no.livro = menorValor(no.direito);
            // remover o sucessor duplicado
            no.direito = removerNo(no.direito, no.livro.getTitulo());
        }
        return no;
    }
    private Livro menorValor(No no) {
        Livro menor = no.livro;
        while (no.esquerdo != null) {
            menor = no.esquerdo.livro;
            no = no.esquerdo;
        }
        return menor;
    }
    
    // operação fundamental de percurso (emordem, pósordem e préordem)
    public void exibirEmOrdem() {
        if (raiz == null) System.out.println("Árvore vazia.");
        percorrerEmOrdem(this.raiz);
        System.out.println();
    }
    private void percorrerEmOrdem(No no) {
        if (no != null) {
            percorrerEmOrdem(no.esquerdo);
            System.out.println(" -> " + no.livro);
            percorrerEmOrdem(no.direito);
        }
    }
    
    public void exibirPreOrdem() {
        if (raiz == null) System.out.println("Árvore vazia.");
        percorrerPreOrdem(this.raiz);
        System.out.println();
    }
    private void percorrerPreOrdem(No no) {
        if (no != null) {
            System.out.println(" -> " + no.livro);
            percorrerPreOrdem(no.esquerdo);
            percorrerPreOrdem(no.direito);
        }
    }
    
    public void exibirPosOrdem() {
        if (raiz == null) System.out.println("Árvore vazia.");
        percorrerPosOrdem(this.raiz);
        System.out.println();
    }
    private void percorrerPosOrdem(No no) {
        if (no != null) {
            percorrerPosOrdem(no.esquerdo);
            percorrerPosOrdem(no.direito);
            System.out.println(" -> " + no.livro);
        }
    }
}