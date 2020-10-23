/*
 * ObjetoRemoto.java
 */

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

/**
 * Objeto que implementa la interfaz remota
 */
public class ObjetoRemoto extends UnicastRemoteObject 
    implements InterfaceRemota, InterfacePD
{
    /**
     * Construye una instancia de ObjetoRemoto
     * @throws RemoteException
     */
    //Crear estado de objeto remoto
    protected ObjetoRemoto () throws RemoteException
        {
        super();
    }

    /**
     * Obtiene la suma y la resta de los sumandos que le pasan y la devuelve.
     */
    public int suma(int a, int b) 
    {
	    System.out.println ("Sumando " + a + " + " + b +"...");
        return a+b;
    }
    public int resta (int a,int b) 
    {
        System.out.println("Restando: " + a +" + " + b + " ..." );
        try {
            Thread.sleep(1);
        }
        catch (InterruptedException e) {
            e.printStackTrace();    
        }
        return a-b;
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
