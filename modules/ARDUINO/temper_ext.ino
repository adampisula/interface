float temperature;
#include <Wire.h>  
#include <OneWire.h>
#include <DS18B20.h>
#define ONEWIRE_PIN 2   //Pin is changable
byte address[8] = {0x28, 0xFF, 0x4C, 0xCF, 0x33, 0x16, 0x4, 0x3E};  //Address is unique for every device, and it has to be read before putting into the code

OneWire onewire(ONEWIRE_PIN);
DS18B20 sensors(&onewire);

void setup(){
   while(!Serial);
sensors.begin();
  sensors.request(address);
   Serial.begin(9600);  

}
 
void loop(){
  //External termometer
  
   if (sensors.available())
  {
    temperature = sensors.readTemperature(address);

    Serial.print(temperature);
    Serial.println(F(" 'C - external"));

    sensors.request(address);
  }
   delay(1000);
}                         
