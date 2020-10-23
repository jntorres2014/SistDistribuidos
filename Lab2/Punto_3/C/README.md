#
# Como usar... 
#openjdk 11.0.7 2020-04-14
#OpenJDK Runtime Environment (build 11.0.7+10-post-Ubuntu-2ubuntu219.10)
#OpenJDK 64-Bit Server VM (build 11.0.7+10-post-Ubuntu-2ubuntu219.10, mixed mode, sharing)
#
Iniciar rmi registry:
	> rmiregistry
para correr Servidor use:
	> javac Servidorrmi.java (para compilar)
	> java Servidorrmi (para ejecutar)
para correr Cliente use:
	> javac Clientermi.java (para compilar)
	> java Clientermi <operacion> <int 1> <int 2>
	> ej: java Clientermi suma 1 2 
