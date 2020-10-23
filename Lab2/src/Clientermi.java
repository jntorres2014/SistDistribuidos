/*
 * Cliente.java
 *
 * Ejemplo de muy simple de rmi
 */

import java.rmi.Naming;                    /* lookup         */
import java.rmi.registry.Registry;         /* REGISTRY_PORT  */

import java.net.MalformedURLException;     /* Exceptions...  */
import java.rmi.NotBoundException;
import java.rmi.RemoteException;

/*
 * Ejemplo de cliente rmi 
*/
public class Clientermi {
    
    /** Crea nueva instancia de Cliente */
    public Clientermi(String alfa) 
    {
        try
        {
		// Lugar en el que está el objeto remoto.
		// Debe reemplazarse "localhost" por el nombre o ip donde está corriendo "rmiregistry".
		// Naming.lookup() obtiene el objeto remoto
	    String rname = "//" + alfa + ":" + Registry.REGISTRY_PORT + "/ObjetoRemoto";
	    String rname2 = "//" + alfa + ":" + Registry.REGISTRY_PORT + "/ObjetoRemoto2";
        InterfaceRemota objetoRemoto = (InterfaceRemota)Naming.lookup (rname);
        InterfacePD objetoRemoto2 = (InterfacePD)Naming.lookup (rname2);
            
            // Se realiza la suma remota.
            System.out.print ("2 + 3 = ");
            System.out.println (objetoRemoto.suma(2,3));
            System.out.print ("2 - 3 = ");
            System.out.println (objetoRemoto.resta(2,3));
            System.out.print ("2 * 3 = ");
            System.out.println (objetoRemoto2.producto(2,3));
            System.out.print ("2 / 3 = ");
            System.out.println (objetoRemoto2.division(10,2));
            
        } catch (MalformedURLException e) {
	    e.printStackTrace();
	} catch (RemoteException e) {
	    e.printStackTrace();
	} catch (NotBoundException e) {
	    e.printStackTrace();
	}
    }
    
    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        new Clientermi(args[0]);
    }
    
}
