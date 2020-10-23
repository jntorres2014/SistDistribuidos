import java.rmi.Naming;                    /* lookup         */
import java.rmi.registry.Registry;         /* REGISTRY_PORT  */

import java.net.MalformedURLException;     /* Exceptions...  */
import java.rmi.NotBoundException;
import java.rmi.RemoteException;

public class Clientermi{

    public Clientermi(String alfa){
    String rname = "//" + alfa + ":" + Registry.REGISTRY_PORT + "/ObjetoRemoto";
    InterfaceRemota objetoRemoto = (InterfaceRemota)Naming.lookup (rname);
    
        }
        
    public static void main(String[] args) {
        new Clientermi(args[0]);
    }
}
