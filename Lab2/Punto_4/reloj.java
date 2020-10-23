public class reloj {

    public static void main(String[] args) throws InterruptedException{

        int hora= 23,minutos=59,segundos=30,mili=0;

        while (true){
            Thread.sleep(1);
            if (hora < 10){
                System.out.print("0");
            }
            System.out.print(hora+":");
        
            if (minutos < 10){
                System.out.print("0");
            }
            System.out.print(minutos+":");

            if (segundos < 10){
                System.out.print("0");
            }
            System.out.print(segundos+":");
            //System.out.print(segundos);
            if (mili <10){
                System.out.print(0);
            }
        
            System.out.println(mili);

            mili ++;
            //timer.sleep();
            if (mili == 1000){
                mili= 0;
                segundos ++;
                if (segundos == 60){
                    segundos = 0;
                    minutos ++;
                    if (minutos == 60){
                        minutos= 0;
                        hora++;
                        if (hora== 24){
                            hora=0;
                                }
                            }
                        }
                        
                }    
        }
    }
}