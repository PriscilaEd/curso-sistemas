import java.awt.Font;
import javax.swing.SwingUtilities;
import javax.swing.UIManager;

public class Main {

	public static void main(String[] args) {
		 java.util.Enumeration<Object> keys = UIManager.getDefaults().keys();
		    while (keys.hasMoreElements()) {
		        Object key = keys.nextElement();
		        Object value = UIManager.getDefaults().get(key);
		        if (value instanceof javax.swing.plaf.FontUIResource) {
		            UIManager.put(key, new javax.swing.plaf.FontUIResource("Arial", Font.PLAIN, 26));
		        }
		    }
		    SwingUtilities.invokeLater(EventoView::new);
		}

	}


