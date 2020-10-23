/*
 * Cliente.java
 *
 * Ejemplo de muy simple de rmi
 */

import java.rmi.Naming;                    /* lookup         */
import java.rmi.registry.Registry;         /* REGISTRY_PORT  */

//import sun.jvm.hotspot.debugger.posix.elf.ELFFile;

import java.net.MalformedURLException;     /* Exceptions...  */
import java.rmi.NotBoundException;
import java.rmi.RemoteException;

/*
 * Ejemplo de cliente rmi 
*/
public class Clientermi {
    
    /** Crea nueva instancia de Cliente */
    public Clientermi(String alfa, String operacion, int num1, int num2) 
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
            System.out.println(operacion);
            if (operacion.equals("suma")){
                System.out.print (num1+" + "+ num2+ " = ");
                System.out.println (objetoRemoto.suma(num1,num2));
            }
            if (operacion.equals("resta")){
            System.out.print (num1+" - "+ num2+ " = ");
            System.out.println (objetoRemoto.resta(num1,num2));
            }
            if (operacion.equals("producto")){ 
            System.out.print (num1+" * "+ num2+ " = ");
            System.out.println (objetoRemoto2.producto(num1,num2));
            }
            if (operacion.equals("division")){
            System.out.print (num1+" / "+ num2+ " = ");
            System.out.println (objetoRemoto2.division(num1,num2));
            }
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
        //System.out.print(args);
        int num1= Integer.parseInt(args[2]);
        int num2= Integer.parseInt(args[3]);
        //int num2= (int) args[3];
        new Clientermi(args[0],args[1],num1,num2 );
    }
    
}
