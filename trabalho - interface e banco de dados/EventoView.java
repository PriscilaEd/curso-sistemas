import java.awt.BorderLayout;
import java.awt.FlowLayout;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.Insets;
import java.util.LinkedList;
import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.ListSelectionModel;
import javax.swing.SwingUtilities;
import javax.swing.table.DefaultTableModel;

public class EventoView extends JFrame {
    // ── Campos do formulário 
    private JTextField campoNome       = new JTextField(20);
    private JTextField campoLocal      = new JTextField(20);
    private JTextField campoData       = new JTextField(20); 
    private JTextField campoCapacidade = new JTextField(20);
 
    // ── Tabela 
    private DefaultTableModel modeloTabela;
    private JTable tabela;
 
    // ── DAO 
    private EventoDAO eventoDAO = new EventoDAO();
 
    public EventoView() {
        setTitle("Organização de Eventos");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setSize(1920, 1080);
        setLocationRelativeTo(null);
        setLayout(new BorderLayout(10, 10));
 
        add(criarPainelFormulario(), BorderLayout.NORTH);
        add(criarPainelTabela(),     BorderLayout.CENTER);
        add(criarPainelBotoes(),     BorderLayout.SOUTH);
 
        carregarTabela();
        setVisible(true);
    }
 
    // ── Painel superior: formulário 
    private JPanel criarPainelFormulario() {
        JPanel painel = new JPanel(new GridBagLayout());
        painel.setBorder(BorderFactory.createTitledBorder("Novo Evento"));
        GridBagConstraints c = new GridBagConstraints();
        c.insets = new Insets(5, 8, 5, 8);
        c.anchor = GridBagConstraints.WEST;
 
        // Linha 0
        c.gridx = 0; c.gridy = 0; painel.add(new JLabel("Nome:"),       c);
        c.gridx = 1;               painel.add(campoNome,                  c);
        c.gridx = 2;               painel.add(new JLabel("Local:"),       c);
        c.gridx = 3;               painel.add(campoLocal,                 c);
 
        // Linha 1
        c.gridx = 0; c.gridy = 1; painel.add(new JLabel("Data (DD/MM/YYYYS):"), c);
        c.gridx = 1;               painel.add(campoData,                        c);
        c.gridx = 2;               painel.add(new JLabel("Capacidade:"),        c);
        c.gridx = 3;               painel.add(campoCapacidade,                  c);
 
        return painel;
    }
 
    // ── Painel central: tabela 
    private JPanel criarPainelTabela() {
        String[] colunas = {"ID", "Nome", "Local", "Data", "Capacidade"};
        modeloTabela = new DefaultTableModel(colunas, 0) {
            @Override public boolean isCellEditable(int row, int col) { return false; }
        };
        tabela = new JTable(modeloTabela);
        tabela.setRowHeight(30);
        tabela.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        tabela.getTableHeader().setReorderingAllowed(false);
 
        
        tabela.getSelectionModel().addListSelectionListener(e -> {
            if (!e.getValueIsAdjusting()) preencherFormularioComLinhaSelecionada();
        });
 
        JPanel painel = new JPanel(new BorderLayout());
        painel.setBorder(BorderFactory.createTitledBorder("Eventos Cadastrados"));
        painel.add(new JScrollPane(tabela), BorderLayout.CENTER);
        return painel;
    }
 
    // ── Painel inferior: botões 
    private JPanel criarPainelBotoes() {
        JButton btnInserir    = new JButton("Inserir Evento");
        JButton btnAtualizar  = new JButton("Atualizar Lista");
        JButton btnLimpar     = new JButton("Limpar Campos");
 
        btnInserir.addActionListener(e -> inserirEvento());
        btnAtualizar.addActionListener(e -> carregarTabela());
        btnLimpar.addActionListener(e -> limparCampos());
 
        JPanel painel = new JPanel(new FlowLayout(FlowLayout.CENTER, 15, 8));
        painel.add(btnInserir);
        painel.add(btnAtualizar);
        painel.add(btnLimpar);
        return painel;
    }
 
    // ── Lógica: carregar eventos na tabela 
    private void carregarTabela() {
        modeloTabela.setRowCount(0); // limpa as linhas existentes
        LinkedList<Evento> lista = eventoDAO.listar();
        for (Evento ev : lista) {
            modeloTabela.addRow(new Object[]{
                ev.getId_evento(),
                ev.getNome(),
                ev.getLocal(),
                ev.getData_evento(),
                ev.getCapacidade()
            });
        }
    }
 
    // ── Lógica: inserir evento 
    private void inserirEvento() {
        String nome       = campoNome.getText().trim();
        String local      = campoLocal.getText().trim();
        String data       = campoData.getText().trim();
        String capTexto   = campoCapacidade.getText().trim();
 
        // Validação básica
        if (nome.isEmpty() || local.isEmpty() || data.isEmpty() || capTexto.isEmpty()) {
            JOptionPane.showMessageDialog(this,
                "Por favor, preencha todos os campos.",
                "Campos obrigatórios", JOptionPane.WARNING_MESSAGE);
            return;
        }
 
        int capacidade;
        try {
            capacidade = Integer.parseInt(capTexto);
        } catch (NumberFormatException ex) {
            JOptionPane.showMessageDialog(this,
                "Capacidade deve ser um número inteiro.",
                "Valor inválido", JOptionPane.ERROR_MESSAGE);
            return;
        }
 
        Evento ev = new Evento();
        ev.setNome(nome);
        ev.setLocal(local);
        ev.setData_evento(data);
        ev.setCapacidade(capacidade);
 
        eventoDAO.inserir(ev);
        JOptionPane.showMessageDialog(this,
            "Evento inserido com sucesso!",
            "Sucesso", JOptionPane.INFORMATION_MESSAGE);
 
        limparCampos();
        carregarTabela();
    }
 
    // ── Preenchimento do formulário ao clicar na tabela 
    private void preencherFormularioComLinhaSelecionada() {
        int linha = tabela.getSelectedRow();
        if (linha < 0) return;
        campoNome.setText((String) modeloTabela.getValueAt(linha, 1));
        campoLocal.setText((String) modeloTabela.getValueAt(linha, 2));
        campoData.setText((String) modeloTabela.getValueAt(linha, 3));
        campoCapacidade.setText(String.valueOf(modeloTabela.getValueAt(linha, 4)));
    }
 
    // ── Limpar campos 
    private void limparCampos() {
        campoNome.setText("");
        campoLocal.setText("");
        campoData.setText("");
        campoCapacidade.setText("");
        tabela.clearSelection();
    }
 
    // ── Ponto de entrada 
    public static void main(String[] args) {
        SwingUtilities.invokeLater(EventoView::new);
    }

}
