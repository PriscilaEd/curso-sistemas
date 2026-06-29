import java.sql.Connection;
import java.sql.DriverManager;

public class Conexao {
private Connection conexao;
	
	public Conexao() {
		try {
			String url = "jdbc:mysql://localhost:3306/trabalho_eventos";
		    String usuario = "root";
			String senha = "Aspire5";
			conexao = DriverManager.getConnection(url, usuario, senha);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	public void desconecta() {
		try {
			conexao.close();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	public Connection getConexao() {
		return conexao;
	}

	public void setConexao(Connection conexao) {
		this.conexao = conexao;
	}
}
