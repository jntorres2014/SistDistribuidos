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
    private int result;
    /**
     * Construye una instancia de ObjetoRemoto
     * @throws RemoteException
     */
    //Crear estado de objeto remoto
    protected ObjetoRemoto () throws RemoteException
        {
        super();
    }
    public int getResult() {
        return result;
    }
    public void setResult(int result) {
        this.result = result;
    }
    /**
     * Obtiene la suma y la resta de los sumandos que le pasan y la devuelve.
     */
    public int suma(int a, int b) 
    {
	    System.out.print ("Sumando " + a + " + " + b +"=");
        this.setResult(a+b);
        System.out.println(this.getResult());
        return this.getResult();
    }
    public synchronized int resta (int a,int b)  
    {
        System.out.print("Restando: " + a +" - " + b + "= " );
        this.setResult(a-b);
        try {
            Thread.sleep(10000);
        }
        catch (InterruptedException e) {
            e.printStackTrace();    
        }
        System.out.println(this.getResult());
        return getResult();
     }

    /**
        Obtiene el producto y la division 
     */
    public int producto (int a,int b){
        System.out.println("Restando: " + a +" - " + b + " ..." );
        return a*b;
    }
    public float division (int a,int b){
        System.out.println("Dividiendo : " + a +" / " + b + " ..." );
        return a / b;
    }

}
