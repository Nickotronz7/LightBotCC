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
char player = '2'; // 0 = N; 1 = E; 2 = S; 3 = W
int posx = 0;
int posy = 0;

// Counter
int counter = 0;

char option;

// Guarda la matrix original
String matrixMem = "";


void setup(){
  
  Serial.begin(9600);
  matrix.begin();
  delay(1100);
 
}


/*
 * mietnras recibe el serial; los primeros, asumiendo que comienza en 1 
 * cuando en realidad comienza en 0, 64 bytes que recibe se vuelven la
 * matriz del juego, los byte 65 y 66 para la posicion 'x' y 'y' del jugador
 * respectivamente en int y los caracteres que siguen se vuelven los
 * movimientos por hacer del jugador
 */
void loop() {
  while(Serial.available()){
    option = Serial.read();
  
    if (counter <64){
      setMap(option);
    }
    if (counter == 64){
      posx = option - '0';
    }
    if (counter == 65){
      posy = option - '0';
      playerOrientation (posx, posy, player);
    }
    if (counter > 65){
      playGame(option);
      delay(500);
    }
      counter++;
  }
}

/*
 * Paso inicial que hace al llegar las primeras 64 siglas del buffer
 * va de cuadro a cuadro poniendo el color respectivo a la matriz 
 * recibida.
 */
void setMap(char option){
  
  matrixMem += option;
  
  switch(option)
  {
    case '0':
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(0,130,200));
      break;
    case '1':
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(0,180,75));
      break;
    case '2':
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(170,110,40));
      break;
    case '3':
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(245,130,48));
      break;
    case '4':
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(0,130,200));
      matrix.fillRect(((counter%8)*4)+2,(floor(counter/8)*4)+2,2,2,matrix.Color333(7,0,4));
      break;
    case '5':
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(0,180,75));
      matrix.fillRect(((counter%8)*4)+2,(floor(counter/8)*4)+2,2,2,matrix.Color333(7,0,4));
      break;
    case '6':
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(170,110,40));
      matrix.fillRect(((counter%8)*4)+2,(floor(counter/8)*4)+2,2,2,matrix.Color333(7,0,4));
      break;
    case '7':
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(245,130,48));
      matrix.fillRect(((counter%8)*4)+2,(floor(counter/8)*4)+2,2,2,matrix.Color333(7,0,4));
      break;
    case '8':
      matrix.fillRect((counter%8)*4,floor(counter/8)*4,4,4,matrix.Color333(0,0,0));
      break;  
  }
}

/*
 * Pone bloque especificos en las posiciones 'x' y 'y' del cuadro especifico
 * junto a su color, esto se usa para volver a poner el cuadro original sin
 * modificar antes de que el jugador llegara.
 */
void setMap(int x, int y, char option){
  switch(option)
  {
    case '0':
      matrix.fillRect(x*4,y*4,4,4,matrix.Color333(0,130,200));
      break;
    case '1':
      matrix.fillRect(x*4,y*4,4,4,matrix.Color333(0,180,75));
      break;
    case '2':
      matrix.fillRect(x*4,y*4,4,4,matrix.Color333(170,110,40));
      break;
    case '3':
      matrix.fillRect(x*4,y*4,4,4,matrix.Color333(245,130,48));
      break;
    case '4':
      matrix.fillRect(x*4,y*4,4,4,matrix.Color333(0,130,200));
      matrix.fillRect((x*4)+2,(y*4)+2,2,2,matrix.Color333(7,0,4));
      break;
    case '5':
      matrix.fillRect(x*4,y*4,4,4,matrix.Color333(0,180,75));
      matrix.fillRect((x*4)+2,(y*4)+2,2,2,matrix.Color333(7,0,4));
      break;
    case '6':
      matrix.fillRect(x*4,y*4,4,4,matrix.Color333(170,110,40));
      matrix.fillRect((x*4)+2,(y*4)+2,2,2,matrix.Color333(7,0,4));
      break;
    case '7':
      matrix.fillRect(x*4,y*4,4,4,matrix.Color333(245,130,48));
      matrix.fillRect((x*4)+2,(y*4)+2,2,2,matrix.Color333(7,0,4));
      break;
    case '8':
      matrix.fillRect(x*4,y*4,4,4,matrix.Color333(0,0,0));
      break;
    case 'w':
      matrix.fillRect(x*4,y*4,4,4,matrix.Color333(0,130,200));
      matrix.fillRect((x*4)+2,(y*4)+2,2,2,matrix.Color333(255,255,255));
      break;
    case 'x':
      matrix.fillRect(x*4,y*4,4,4,matrix.Color333(0,180,75));
      matrix.fillRect((x*4)+2,(y*4)+2,2,2,matrix.Color333(255,255,255));
      break;
    case 'y':
      matrix.fillRect(x*4,y*4,4,4,matrix.Color333(170,110,40));
      matrix.fillRect((x*4)+2,(y*4)+2,2,2,matrix.Color333(255,255,255));
      break;
    case 'z':
      matrix.fillRect(x*4,y*4,4,4,matrix.Color333(245,130,48));
      matrix.fillRect((x*4)+2,(y*4)+2,2,2,matrix.Color333(255,255,255));
      break;
  }
}

/*
 *Agarra el buffer que contiene la secuencia de movimientos del juego 
 *y lo analiza para poder hacer sus movimientos respectivos.
 *0 o 3 para moverse para adelante (se utilizan el mismo porque la
 *aplicacion valida los movimientos antes de mandarlo), 1 para girar
 *hacia la derecha y 2 para girar hacia la izquierda, el 4 para encender
 *o apagar la luz del cuadro donde estael jugador. El 9 es un char que
 *se manda si usted gano.
 */
void playGame(char option){
  //move forward / jump
  if ((option == '0') || (option == '3'))
  {
    setMap(posx, posy, matrixMem.charAt(posx+(posy*8)));
    switch(player)
    {
      case '0':
        posy -= 1;
        playerOrientation (posx, posy, player);
        break;
      case '1':
        posx += 1;
        playerOrientation (posx, posy, player);
        break;
      case '2':
        posy += 1;
        playerOrientation (posx, posy, player);
        break;
      case '3':
        posy -= 1;
        playerOrientation (posx, posy, player);
        break;
    }
    return;
  }
  
  //rotate left
  if (option == '2')
  {
    setMap(posx, posy, matrixMem.charAt(posx+(posy*8)));
    switch(player){
      case '0':
        playerOrientation (posx, posy, '3');
        break;
      case '3':
        playerOrientation (posx, posy, '2');
        break;
      case '2':
        playerOrientation (posx, posy, '1');
        break;
      case '1':
        playerOrientation (posx, posy, '0');
        break;
    }
    return;
  }
  
  //rotate right
  if (option == '1')
  {
    setMap(posx, posy, matrixMem.charAt(posx+(posy*8)));
    switch(player){
      case '0':
        playerOrientation (posx, posy, '1');
        break;
      case '1':
        playerOrientation (posx, posy, '2');
        break;
      case '2':
        playerOrientation (posx, posy, '3');
        break;
      case '3':
        playerOrientation (posx, posy, '0');
        break;
    }
    return;
  }

  //turn light off / on
  if (option == '4'){
   lightSwitch(posx, posy);
   playerOrientation(posx,posy,player);
   return;
  }

  if (option == '9')
  {
    delay(2000);
    matrix.fillScreen(matrix.Color333(0,0,0));
    matrix.setTextColor(matrix.Color333(7,0,0));
    matrix.setCursor(8,12);
    matrix.print("WIN");
   
    return;
  }
}

/*
 * Determina la orientacion del jugador y en el lugar donde esta,
 * se utiliza para determinar la posicion inicial, al igual que su
 * orientacion inicial.
 */
void playerOrientation (int posx, int posy, char option){
  switch(option)
  {
    case '0':
      matrix.fillRect((posx)*4,floor(posy)*4,2,1,matrix.Color333(255,0,0));
      matrix.fillRect((posx)*4,(floor(posy)*4)+1,2,1,matrix.Color333(0,0,255));
      player = option;
      break;
    case '1':
      matrix.fillRect((posx)*4,posy*4,1,2,matrix.Color333(0,0,255));
      matrix.fillRect(((posx)*4)+1,posy*4,1,2,matrix.Color333(255,0,0));
      player = option;
      break;
    case '2':
      matrix.fillRect((posx)*4,(floor(posy)*4)+1,2,1,matrix.Color333(255,0,0));
      matrix.fillRect((posx)*4,floor(posy)*4,2,1,matrix.Color333(0,0,255));
      player = option;
      break;
    case '3':
      matrix.fillRect((posx)*4,posy*4,1,2,matrix.Color333(255,0,0));
      matrix.fillRect(((posx)*4)+1,posy*4,1,2,matrix.Color333(0,0,255));
      player = option;
      break;
  }
}

/*
 * Determina si esta en un cuadro con la luz apagada o encendida y una vez
 * que se llama a la funcion apaga/enciende la luz
 */
void lightSwitch(int posx, int posy)
{
  switch((matrixMem.charAt(posx+(posy*8))))
  {
    case '4':
      matrixMem.setCharAt(posx+(posy*8), 'w');
      matrix.fillRect((posx*4)+2,(posy*4)+2,2,2,matrix.Color333(255,255,255));
      break;
    case '5':
      matrixMem.setCharAt(posx+(posy*8), 'x');
      matrix.fillRect((posx*4+2),(posy*4)+2,2,2,matrix.Color333(255,255,255));
      break;
    case '6':
      matrixMem.setCharAt(posx+(posy*8), 'y');
      matrix.fillRect((posx*4)+2,(posy*4)+2,2,2,matrix.Color333(255,255,255));
      break;
    case '7':
      matrixMem.setCharAt(posx+(posy*8), 'z');
      matrix.fillRect((posx*4)+2,(posy*4)+2,2,2,matrix.Color333(255,255,255));
      break;
    case 'w':
      matrixMem.setCharAt((posx*4)+(posy*8), '4');
      matrix.fillRect((posx*4)+2,(posy*4)+2,2,2,matrix.Color333(7,0,4));
      break;
    case 'x':
      matrixMem.setCharAt(posx+(posy*8), '5');
      matrix.fillRect((posx*4)+2,(posy*4)+2,2,2,matrix.Color333(7,0,4));
      break;
    case 'y':
      matrixMem.setCharAt(posx+(posy*8), '6');
      matrix.fillRect((posx*4)+2,(posy*4)+2,2,2,matrix.Color333(7,0,4));
      break;
    case 'z':
      matrixMem.setCharAt(posx+(posy*8), '7');
      matrix.fillRect((posx*4)+2,(posy*4)+2,2,2,matrix.Color333(7,0,4));
      break;
  }  
}


    
