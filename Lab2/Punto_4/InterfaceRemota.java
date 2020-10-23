import java.rmi.Remote;
import java.rmi.RemoteException;

public interface InterfazRemota extends Remote{
	//Colocar metodos remotos.
	public long obtenerHora()throws RemoteException;

}
