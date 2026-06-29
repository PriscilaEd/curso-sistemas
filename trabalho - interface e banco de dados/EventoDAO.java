import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.LinkedList;

public class EventoDAO {
	public LinkedList<Evento> listar() {
		Conexao con = new Conexao();
		LinkedList<Evento> lista = new LinkedList<Evento>();
		try {
			String sql = "SELECT * FROM eventos";
			Statement instrucao = con.getConexao().createStatement();
			ResultSet res = instrucao.executeQuery(sql);
			while (res.next()) {
				Evento e = new Evento();
				e.setId_evento(res.getInt("id_evento"));
				e.setNome(res.getString("nome"));
				e.setLocal(res.getString("local"));
				e.setData_evento(res.getString("data_evento"));
				e.setCapacidade(res.getInt("capacidade"));
				lista.add(e);
			}
		} catch (Exception e) {
			e.printStackTrace();
		} finally {
			con.desconecta();
		}
		return lista;
	}

	public void inserir(Evento e) {
		Conexao con = new Conexao();
		LinkedList<Evento> lista = new LinkedList<Evento>();
		try {
			String sql = "INSERT INTO eventos" + "(nome,\n" + "	local,\n" + "	data_evento,\n" + "	capacidade) "
					+ "VALUES (?,?,?,?)";
			PreparedStatement prep = con.getConexao().prepareStatement(sql);
			prep.setString(1, e.getNome());
			prep.setString(2, e.getLocal());
			prep.setString(3, e.getData_evento());
			prep.setInt(4, e.getCapacidade());
			prep.execute();
		} catch (Exception E) {
			E.printStackTrace();
		} finally {
			con.desconecta();
		}
	}
}
