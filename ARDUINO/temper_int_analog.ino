int sens = A0;   //Analog pin is changeable
float VOLT;
float TEMP;
#include <Wire.h> 

void setup(){
   while(!Serial);
   Serial.begin(9600);  
   

}
 
void loop(){
 
  //Internal termometer
  int temp = analogRead(sens);      
  VOLT = (temp * 5.0) / 1024.0;        
  TEMP = VOLT  * 100;    
   Serial.print(TEMP);
   Serial.println(F(" 'C - internal"));
   delay(1000);
}                         
