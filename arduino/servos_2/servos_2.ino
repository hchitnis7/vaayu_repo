#include <Servo.h>


Servo servo1; 

Servo servo2;

int i = 0;


void setup() {

  servo1.attach(10);

  servo2.attach(9); 

}


void loop() {

  

    servo1.write(i);              
             

    delay(10);                      
               

    servo2.write(i);     
    delay(10);                      




}
