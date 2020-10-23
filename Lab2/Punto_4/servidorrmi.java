import java.rmi.Naming;                    /* lookup         */
import java.rmi.registry.Registry;         /* REGISTRY_PORT  */
import java.util.concurrent.TimeUnit;

/**
 * Servidor para el ejemplo de RMI.
 * Exporte un metodo para sumar dos enteros y devuelve el resultado.
 */
public class Servidorrmi
{
    
    /** Crea nueva instancia de Servidor rmi */
    public Servidorrmi() {
        try 
        {
            InterfaceRemota objetoRemoto = new ObjetoRemoto();
			String rname = "//localhost:" + Registry.REGISTRY_PORT  + "/ObjetoRemoto";
            Naming.rebind (rname, objetoRemoto);
                    
        }
        
        catch (Exception e)
        {
            e.printStackTrace();
        }
    }
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        new Servidorrmi();
    }
}
		