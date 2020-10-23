/*
 * ObjetoRemoto.java
 */

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

/**
 * Objeto que implementa la interfaz remota
 */
public class ObjetoRemotoMD extends UnicastRemoteObject 
    implements InterfacePD
{
    /**
     * Construye una instancia de ObjetoRemoto
     * @throws RemoteException
     */
    //Crear estado de objeto remoto
    protected ObjetoRemotoMD () throws RemoteException
        {
        super();
    }

    /**
        Obtiene el producto y la division 
     */
    public int producto (int a,int b){
        System.out.println("Restando: " + a +" + " + b + " ..." );
        return a*b;
    }
    public float division (int a,int b){
        System.out.println("Dividiendo : " + a +" + " + b + " ..." );
        return a / b;
    }

}
