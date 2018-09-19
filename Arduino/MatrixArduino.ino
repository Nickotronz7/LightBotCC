#include <RGBmatrixPanel.h>

#define CLK  8
#define OE   9
#define LAT 10
#define A   A0
#define B   A1
#define C   A2
#define D   A3

RGBmatrixPanel matrix(A, B, C, D, CLK, LAT, OE, false);

// Player initial position
int posx = 0;
int posy = 0;

// Matrix Set
bool isSet = false;

// Counter


char option;


void setup(){
  
  Serial.begin(9600);
  matrix.begin();
  delay(1100);
 
}

int counter = 0;

void loop() {

  option = Serial.read();

  if (counter < 64){
    if (option == '0') //floor 0
    {
        matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(0,130,200));
    }
    if (option == '1') // floor 1
    {
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(0,180,75));
    }
    if (option == '2') // floor 2
    {
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(170,110,40));
    }
    if (option == '3') // floor 3
    {
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(245,130,48));
    }
    if (option == '4') // floor 0 light
    {
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(0,130,200));
      matrix.fillRect(((counter%8)*4)+2,(floor(counter/8)*4)+2,2,2,matrix.Color333(255,255,255));
    }
    if (option == '5') // floor 1 light
    {
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(0,180,75));
      matrix.fillRect(((counter%8)*4)+2,(floor(counter/8)*4)+2,2,2,matrix.Color333(255,255,255));
    }
    if (option == '6') // floor 2 light
    {
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(170,110,40));
      matrix.fillRect(((counter%8)*4)+2,(floor(counter/8)*4)+2,2,2,matrix.Color333(255,255,255));
    }
    if (option == '7') // floor 3 light
    {
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(245,130,48));
      matrix.fillRect(((counter%8)*4)+2,(floor(counter/8)*4)+2,2,2,matrix.Color333(255,255,255));
    }
    if (option == '8') // wall
    {
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(0,0,0));
    }
    delay (600);
  }
  
    counter++;

}
