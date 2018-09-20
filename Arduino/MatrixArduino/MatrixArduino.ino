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
int player = 0; // 0 = N; 1 = E; 2 = S; 3 = W
int posx = 0;
int posy = 0;


// Counter
int counter = 0;

char option;

String matrixMem = "";


void setup(){
  
  Serial.begin(9600);
  matrix.begin();
  delay(1100);
 
}

void loop() {

  option = Serial.read();

  if (counter <64){
    setMap(option);
  }

  if (counter == 64){
    return;
  }
  
  if (counter == 65){
    return;
  }

  if (counter > 65){
    return;
  }
  
    counter++;
}

void setMap(char option){
  
  matrixMem += option;
  
  if (option == '0') //floor 0 //verde oscuro
    {
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(0,130,200));
    }
    if (option == '1') // floor 1 //azul
    {
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(0,180,75));
    }
    if (option == '2') // floor 2 //verde claro
    {
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(170,110,40));
    }
    if (option == '3') // floor 3 //anaranjado
    {
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(245,130,48));
    }
    if (option == '4') // floor 0 light
    {
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(0,130,200));
      matrix.fillRect(((counter%8)*4)+2,(floor(counter/8)*4)+2,2,2,matrix.Color333(7,0,4));
    }
    if (option == '5') // floor 1 light
    {
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(0,180,75));
      matrix.fillRect(((counter%8)*4)+2,(floor(counter/8)*4)+2,2,2,matrix.Color333(7,0,4));
    }
    if (option == '6') // floor 2 light
    {
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(170,110,40));
      matrix.fillRect(((counter%8)*4)+2,(floor(counter/8)*4)+2,2,2,matrix.Color333(7,0,4));
    }
    if (option == '7') // floor 3 light
    {
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(245,130,48));
      matrix.fillRect(((counter%8)*4)+2,(floor(counter/8)*4)+2,2,2,matrix.Color333(7,0,4));
    }
    if (option == '8') // wall
    {
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(0,0,0));
    }
}

void setMap(int x, int y, char option){
  
  if (option == '0') //floor 0 //verde oscuro
  {
    matrix.fillRect(x*4,y*4,4,4,matrix.Color333(0,130,200));
  }
  if (option == '1') // floor 1 //azul
  {
    matrix.fillRect(x*4,y*4,4,4,matrix.Color333(0,180,75));
  }
  if (option == '2') // floor 2 //verde claro
  {
    matrix.fillRect(x*4,y*4,4,4,matrix.Color333(170,110,40));
  }
  if (option == '3') // floor 3 //anaranjado
  {
    matrix.fillRect(x*4,y*4,4,4,matrix.Color333(245,130,48));
  }
  if (option == '4') // floor 0 light off
  {
    matrix.fillRect(x*4,y*4,4,4,matrix.Color333(0,130,200));
    matrix.fillRect((x*4)+2,(y*4)+2,2,2,matrix.Color333(7,0,4));
  }
  if (option == '5') // floor 1 light off
  {
    matrix.fillRect(x*4,y*4,4,4,matrix.Color333(0,180,75));
    matrix.fillRect((x*4)+2,(y*4)+2,2,2,matrix.Color333(7,0,4));
  }
  if (option == '6') // floor 2 light off
  {
    matrix.fillRect(x*4,y*4,4,4,matrix.Color333(170,110,40));
    matrix.fillRect((x*4)+2,(y*4)+2,2,2,matrix.Color333(7,0,4));
  }
  if (option == '7') // floor 3 light off
  {
    matrix.fillRect(x*4,y*4,4,4,matrix.Color333(245,130,48));
    matrix.fillRect((x*4)+2,(y*4)+2,2,2,matrix.Color333(7,0,4));
  }
  if (option == '8') // wall
  {
    matrix.fillRect(x*4,y*4,4,4,matrix.Color333(0,0,0));
  }
  if (option == 'w') // floor 0 light on
  {
    matrix.fillRect(x*4,y*4,4,4,matrix.Color333(0,130,200));
    matrix.fillRect((x*4)+2,(y*4)+2,2,2,matrix.Color333(255,255,255));
  }
  if (option == 'x') // floor 1 light on
  {
    matrix.fillRect(x*4,y*4,4,4,matrix.Color333(0,180,75));
    matrix.fillRect((x*4)+2,(y*4)+2,2,2,matrix.Color333(255,255,255));
  }
  if (option == 'y') // floor 2 light on
  {
    matrix.fillRect(x*4,y*4,4,4,matrix.Color333(170,110,40));
    matrix.fillRect((x*4)+2,(y*4)+2,2,2,matrix.Color333(255,255,255));
  }
  if (option == 'z') // floor 3 light on
  {
    matrix.fillRect(x*4,y*4,4,4,matrix.Color333(245,130,48));
    matrix.fillRect((x*4)+2,(y*4)+2,2,2,matrix.Color333(255,255,255));
  }
}



/*
 * 0 -> forward
 * 1 -> rotate left
 * 2 -> roate right
 * 3 -> jump (move forward)
 * 4 -> turn light off / on
 * 
 */
void playgame(char option){
  //move forward

  //rotate left

  //rotate right

  //jump

  //turn light off / on
  
}

void playerOrientation (int posx, int posy, int option){
  if (option == '0')  //North
  {
    matrix.fillRect((posx)*4,floor(posy)*4,2,1,matrix.Color333(255,0,0));
    matrix.fillRect((posx)*4,(floor(posy)*4)+1,2,1,matrix.Color333(0,0,255));
    
  }
  if (option == '1')  //East
  {
    matrix.fillRect((posx)*4,floor(posy)*4,1,2,matrix.Color333(0,0,255));
    matrix.fillRect(((posx)*4)+1,floor(posy)*4,1,2,matrix.Color333(255,0,0));
    
  }
  if (option == '2')  //South
  {
    matrix.fillRect((posx)*4,(floor(posy)*4)+1,2,1,matrix.Color333(255,0,0));
    matrix.fillRect((posx)*4,floor(posy)*4,2,1,matrix.Color333(0,0,255));
    
  }
  if (option == '3')  //West
  {
    matrix.fillRect((posx)*4,floor(posy)*4,1,2,matrix.Color333(255,0,0));
    matrix.fillRect(((posx)*4)+1,floor(posy)*4,1,2,matrix.Color333(0,0,255));
    
  }
}

void lightSwitch(int posx, int posy)
{
  if (matrixMem.charAt(posx+(posy*8)) == '4')
  {
    matrixMem.setCharAt(posx+(posy*8), 'w');
    matrix.fillRect(posx+2,(posy*4)+2,2,2,matrix.Color333(255,255,255));
  }
  if (matrixMem.charAt(posx+(posy*8)) == '5')
  {
    matrixMem.setCharAt(posx+(posy*8), 'x');
    matrix.fillRect(posx+2,(posy*4)+2,2,2,matrix.Color333(255,255,255));
  }
  if (matrixMem.charAt(posx+(posy*8)) == '6')
  {
    matrixMem.setCharAt(posx+(posy*8), 'y');
    matrix.fillRect(posx+2,(posy*4)+2,2,2,matrix.Color333(255,255,255));
  }
  if (matrixMem.charAt(posx+(posy*8)) == '7')
  {
    matrixMem.setCharAt(posx+(posy*8),'z');
    matrix.fillRect(posx+2,(posy*4)+2,2,2,matrix.Color333(255,255,255));
  }

  if (matrixMem.charAt(posx+(posy*8)) == 'w')
  {
    matrixMem.setCharAt(posx+(posy*8), '4');
    matrix.fillRect(posx+2,(posy*4)+2,2,2,matrix.Color333(7,0,4));
  }
  if (matrixMem.charAt(posx+(posy*8)) == 'x')
  {
    matrixMem.setCharAt(posx+(posy*8), '5');
    matrix.fillRect(posx+2,(posy*4)+2,2,2,matrix.Color333(7,0,4));
  }
  if (matrixMem.charAt(posx+(posy*8)) == 'y')
  {
    matrixMem.setCharAt(posx+(posy*8), '6');
    matrix.fillRect(posx+2,(posy*4)+2,2,2,matrix.Color333(7,0,4));
  }
  if (matrixMem.charAt(posx+(posy*8)) == 'z')
  {
    matrixMem.setCharAt(posx+(posy*8),'7');
    matrix.fillRect(posx+2,(posy*4)+2,2,2,matrix.Color333(7,0,4));
  }
  
}


    
