import java.rmi.Remote;
import java.rmi.RemoteException;

public interface InterfacePD extends Remote {
	public float division(int a , int b) throws RemoteException;
	public int producto(int a, int b) throws RemoteException;
}