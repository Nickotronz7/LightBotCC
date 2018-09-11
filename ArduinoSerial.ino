const int pinLED = 13;
 
void setup(){
   Serial.begin(9600);
   pinMode(pinLED, OUTPUT);
}

char moves[7][7];
char option;

void loop(){
  if (Serial.available()>0){
    option = Serial.read();
    Serial.println(option);
    if(option == '0'){
      digitalWrite(pinLED, HIGH);
      delay(500);
      digitalWrite(pinLED, LOW);
      delay(200);    
    }
  }
}
  
