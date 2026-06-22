package arvoreLivros;
import java.util.Scanner;

public class Principal {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArvoreLivros arvore = new ArvoreLivros();
        arvore.inserir(new Livro("É Assim que Acaba", "Colleen Hoover", 2016));
        arvore.inserir(new Livro("É Assim que Começa", "Colleen Hoover", 2022));
        arvore.inserir(new Livro("Em Algum Lugar Dentro de Mim", "Julius Vieira", 2019));
        arvore.inserir(new Livro("Extraordinário", "R.J. Palacio", 2013));
        arvore.inserir(new Livro("O Homem de Giz", "C.J. Tudor", 2018));
        arvore.inserir(new Livro("As Outras Pessoas", "C.J. Tudor", 2020));
        arvore.inserir(new Livro("O que aconteceu com Annie", "C.J. Tudor", 2019));
        arvore.inserir(new Livro("A morte é um dia que vale a pena viver", "Ana Claudia Quintana Arantes", 2016));

        int opcao = -1;

        while (opcao != 0) {

            System.out.println("\n========= MENU INTERATIVO =========");
            System.out.println("(1) Inserir Livro");
            System.out.println("(2) Buscar por Título");
            System.out.println("(3) Remover Livro");
            System.out.println("(4) Exibir Em-Ordem (Alfabética)");
            System.out.println("(5) Exibir Pré-Ordem");
            System.out.println("(6) Exibir Pós-Ordem");
            System.out.println("(0) Sair");
            System.out.print("Escolha uma opção: ");
            
            try {
                opcao = Integer.parseInt(scanner.nextLine());
            } catch (NumberFormatException e) {
                System.out.println("Erro! Digite um título válido");
                continue;
            }

            switch (opcao) {
                case 1:
                    System.out.print("Digite o título do livro: ");
                    String titulo = scanner.nextLine();
                    System.out.print("Digite o autor do livro: ");
                    String autor = scanner.nextLine();
                    System.out.print("Digite o ano de publicação: ");
                    int ano = Integer.parseInt(scanner.nextLine());
                    
                    arvore.inserir(new Livro(titulo, autor, ano));
                    System.out.println("Livro inserido com sucesso!");
                    break;

                case 2:
                    System.out.print("Digite o título para buscar: ");
                    String buscaTitulo = scanner.nextLine();
                    Livro encontrado = arvore.buscar(buscaTitulo);
                    if (encontrado != null) {
                        System.out.println("\n[LIVRO ENCONTRADO]:\n" + encontrado);
                    } else {
                        System.out.println("\n[AVISO]: Esse livro não foi encontrado");
                    }
                    break;

                case 3:
                    System.out.print("Digite o título do livro a ser removido: ");
                    String removerTitulo = scanner.nextLine();
                    arvore.remover(removerTitulo);
                    break;

                case 4:
                    System.out.println("\n--- Exibição Em-Ordem ---");
                    arvore.exibirEmOrdem(); 
                    break;

                case 5:
                    System.out.println("\n--- Exibição Pré-Ordem ---");
                    arvore.exibirPreOrdem(); // 
                    break;

                case 6:
                    System.out.println("\n--- Exibição Pós-Ordem ---");
                    arvore.exibirPosOrdem(); // 
                    break;

                case 0:
                    System.out.println("Encerrando. Até logo!");
                    break;

                default:
                    System.out.println("Erro! Digite uma opção válida");
            }
        }
        scanner.close();
    }
}