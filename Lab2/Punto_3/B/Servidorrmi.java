/*
 * Servidor.java
 *
 * Contiene el código para instanciar y publicar el objetoRemoto en la rmiregistry
 */
 
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
		// Se indica a rmiregistry donde están las clases.
		// Cambiar el paht al sitio en el que esté. Es importante
		// mantener la barra al final.
		/*	System.setProperty(
				"java.rmi.server.codebase",
				"file:/D:/users/javier/java/rmi_simple/src_servidor/");
		*/	
            // Se publica el objeto remoto
            
            InterfaceRemota objetoRemoto = new ObjetoRemoto();
			String rname = "//localhost:" + Registry.REGISTRY_PORT  + "/ObjetoRemoto";
            Naming.rebind (rname, objetoRemoto);
            
            InterfacePD objetoRemoto2 = new ObjetoRemoto();
			String rname2 = "//localhost:" + Registry.REGISTRY_PORT  + "/ObjetoRemoto2";
            Naming.rebind (rname2, objetoRemoto2);
            
            
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
