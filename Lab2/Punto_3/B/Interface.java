public class Interface extends JFrame implements Runnable{
 
    private JLabel horaLabel;
    private Reloj reloj;
 
    public Interface(){
 
        reloj = new Reloj();
 
        horaLabel = new JLabel();
        this.add(horaLabel);
 
        this.setSize(100, 100);
        Thread t = new Thread(this);
        t.start();
 
    }
 
    @Override
    public void run() {
 
        while(true){
            reloj.calcular();
            if(reloj.getMeridiem() == 1)
                horaLabel.setText(reloj.getHora() + ":" + reloj.getMinuto() + ":" + reloj.getSegundo() + " PM");
            else
                horaLabel.setText(reloj.getHora() + ":" + reloj.getMinuto() + ":" + reloj.getSegundo() + " AM");
            try{
                Thread.sleep(1000);
            }catch(Exception e){
                e.printStackTrace();
            }
        }
 
    }
 
}

