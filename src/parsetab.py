
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ADD ASSIGN BACK BEGIN BLOCK CALL CHANGEDIR COMMA COMMENT END ENDPROC EOL ESPECIAL FEND FOR HIGH ID KEEP KEND LBRA LCBRA LEFT LESS LIGHT LPAR MATHEXPR NUM PLACE POS POSSTART PROC PUT QUOTE RBRA RCBRA RES RIGHT RPAR SAME SEMICOLON SET SKIP SUM THEN TIMES VAR WHEN WHEND WHITESPACEprograma : variable BEGIN expresiones END procedimientosvariable : VAR variable1variable1 : ID ASSIGN NUM SEMICOLONvariable1 : ID SEMICOLONexpresiones : asignar expresionesexpresiones : actualizar expresionesexpresiones : cambiar_direccion expresionesexpresiones : colocar expresionesexpresiones : elevar expresionesexpresiones : encender expresionesexpresiones : mover expresionesexpresiones : pos_inicio expresionesexpresiones : llamar expresionesexpresiones : c_keep expresionesexpresiones : c_for expresionesexpresiones : c_when expresiones expresiones : SKIP SEMICOLON expresionesexpresiones  : COMMENT expresionesexpresiones : epsilonc_for : FOR ID ASSIGN NUM TIMES expresiones FEND SEMICOLONc_when : WHEN ID ASSIGN NUM THEN expresiones WHEND SEMICOLONc_keep : KEEP expresiones KEND SEMICOLONasignar : SET ID ASSIGN NUM SEMICOLONactualizar : ADD SUM ID SEMICOLONactualizar : LESS SUM ID SEMICOLONcambiar_direccion : CHANGEDIR LPAR LEFT RPAR SEMICOLONcambiar_direccion : CHANGEDIR LPAR RIGHT RPAR SEMICOLONcambiar_direccion : CHANGEDIR LPAR BACK RPAR SEMICOLONcambiar_direccion : CHANGEDIR LPAR SAME RPAR SEMICOLONcolocar : PLACE BLOCK SEMICOLONcolocar : PLACE BLOCK NUM SEMICOLONelevar : HIGH BLOCK SEMICOLONelevar : HIGH BLOCK NUM SEMICOLONencender : PUT LIGHT SEMICOLONmover : POS LPAR NUM COMMA NUM RPAR SEMICOLONpos_inicio : POSSTART LPAR NUM COMMA NUM RPAR SEMICOLONllamar : CALL ID SEMICOLONprocedimientos : PROC ID expresiones ENDPROC SEMICOLONprocedimientos : epsilonepsilon :'
    
_lr_action_items = {'VAR':([0,],[3,]),'$end':([1,38,67,69,120,],[0,-40,-1,-39,-38,]),'BEGIN':([2,5,37,89,],[4,-2,-4,-3,]),'ID':([3,23,32,34,35,54,55,68,],[6,53,62,64,65,72,73,90,]),'SKIP':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,78,80,82,85,90,92,93,98,99,102,106,107,108,109,110,113,114,121,122,125,126,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-30,-32,-34,-37,20,-24,-25,-31,-33,-22,-23,-26,-27,-28,-29,20,20,-35,-36,-20,-21,]),'COMMENT':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,78,80,82,85,90,92,93,98,99,102,106,107,108,109,110,113,114,121,122,125,126,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-30,-32,-34,-37,21,-24,-25,-31,-33,-22,-23,-26,-27,-28,-29,21,21,-35,-36,-20,-21,]),'SET':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,78,80,82,85,90,92,93,98,99,102,106,107,108,109,110,113,114,121,122,125,126,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-30,-32,-34,-37,23,-24,-25,-31,-33,-22,-23,-26,-27,-28,-29,23,23,-35,-36,-20,-21,]),'ADD':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,78,80,82,85,90,92,93,98,99,102,106,107,108,109,110,113,114,121,122,125,126,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-30,-32,-34,-37,24,-24,-25,-31,-33,-22,-23,-26,-27,-28,-29,24,24,-35,-36,-20,-21,]),'LESS':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,78,80,82,85,90,92,93,98,99,102,106,107,108,109,110,113,114,121,122,125,126,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-30,-32,-34,-37,25,-24,-25,-31,-33,-22,-23,-26,-27,-28,-29,25,25,-35,-36,-20,-21,]),'CHANGEDIR':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,78,80,82,85,90,92,93,98,99,102,106,107,108,109,110,113,114,121,122,125,126,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-30,-32,-34,-37,26,-24,-25,-31,-33,-22,-23,-26,-27,-28,-29,26,26,-35,-36,-20,-21,]),'PLACE':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,78,80,82,85,90,92,93,98,99,102,106,107,108,109,110,113,114,121,122,125,126,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-30,-32,-34,-37,27,-24,-25,-31,-33,-22,-23,-26,-27,-28,-29,27,27,-35,-36,-20,-21,]),'HIGH':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,78,80,82,85,90,92,93,98,99,102,106,107,108,109,110,113,114,121,122,125,126,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,-30,-32,-34,-37,28,-24,-25,-31,-33,-22,-23,-26,-27,-28,-29,28,28,-35,-36,-20,-21,]),'PUT':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,78,80,82,85,90,92,93,98,99,102,106,107,108,109,110,113,114,121,122,125,126,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,-30,-32,-34,-37,29,-24,-25,-31,-33,-22,-23,-26,-27,-28,-29,29,29,-35,-36,-20,-21,]),'POS':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,78,80,82,85,90,92,93,98,99,102,106,107,108,109,110,113,114,121,122,125,126,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-30,-32,-34,-37,30,-24,-25,-31,-33,-22,-23,-26,-27,-28,-29,30,30,-35,-36,-20,-21,]),'POSSTART':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,78,80,82,85,90,92,93,98,99,102,106,107,108,109,110,113,114,121,122,125,126,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-30,-32,-34,-37,31,-24,-25,-31,-33,-22,-23,-26,-27,-28,-29,31,31,-35,-36,-20,-21,]),'CALL':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,78,80,82,85,90,92,93,98,99,102,106,107,108,109,110,113,114,121,122,125,126,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-30,-32,-34,-37,32,-24,-25,-31,-33,-22,-23,-26,-27,-28,-29,32,32,-35,-36,-20,-21,]),'KEEP':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,78,80,82,85,90,92,93,98,99,102,106,107,108,109,110,113,114,121,122,125,126,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-30,-32,-34,-37,33,-24,-25,-31,-33,-22,-23,-26,-27,-28,-29,33,33,-35,-36,-20,-21,]),'FOR':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,78,80,82,85,90,92,93,98,99,102,106,107,108,109,110,113,114,121,122,125,126,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-30,-32,-34,-37,34,-24,-25,-31,-33,-22,-23,-26,-27,-28,-29,34,34,-35,-36,-20,-21,]),'WHEN':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,78,80,82,85,90,92,93,98,99,102,106,107,108,109,110,113,114,121,122,125,126,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-30,-32,-34,-37,35,-24,-25,-31,-33,-22,-23,-26,-27,-28,-29,35,35,-35,-36,-20,-21,]),'END':([4,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,39,40,41,42,43,44,45,46,47,48,49,50,51,52,70,78,80,82,85,92,93,98,99,102,106,107,108,109,110,121,122,125,126,],[-40,38,-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-19,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-40,-18,-17,-30,-32,-34,-37,-24,-25,-31,-33,-22,-23,-26,-27,-28,-29,-35,-36,-20,-21,]),'ASSIGN':([6,53,64,65,],[36,71,87,88,]),'SEMICOLON':([6,20,57,58,59,62,66,72,73,79,81,86,91,94,95,96,97,115,116,117,123,124,],[37,51,78,80,82,85,89,92,93,98,99,102,106,107,108,109,110,120,121,122,125,126,]),'KEND':([8,9,10,11,12,13,14,15,16,17,18,19,21,22,33,39,40,41,42,43,44,45,46,47,48,49,50,51,52,63,70,78,80,82,85,92,93,98,99,102,106,107,108,109,110,121,122,125,126,],[-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-19,-40,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-40,-18,86,-17,-30,-32,-34,-37,-24,-25,-31,-33,-22,-23,-26,-27,-28,-29,-35,-36,-20,-21,]),'ENDPROC':([8,9,10,11,12,13,14,15,16,17,18,19,21,22,39,40,41,42,43,44,45,46,47,48,49,50,51,52,70,78,80,82,85,90,92,93,98,99,102,105,106,107,108,109,110,121,122,125,126,],[-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-19,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-40,-18,-17,-30,-32,-34,-37,-40,-24,-25,-31,-33,-22,115,-23,-26,-27,-28,-29,-35,-36,-20,-21,]),'FEND':([8,9,10,11,12,13,14,15,16,17,18,19,21,22,39,40,41,42,43,44,45,46,47,48,49,50,51,52,70,78,80,82,85,92,93,98,99,102,106,107,108,109,110,113,118,121,122,125,126,],[-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-19,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-40,-18,-17,-30,-32,-34,-37,-24,-25,-31,-33,-22,-23,-26,-27,-28,-29,-40,123,-35,-36,-20,-21,]),'WHEND':([8,9,10,11,12,13,14,15,16,17,18,19,21,22,39,40,41,42,43,44,45,46,47,48,49,50,51,52,70,78,80,82,85,92,93,98,99,102,106,107,108,109,110,114,119,121,122,125,126,],[-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-40,-19,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-40,-18,-17,-30,-32,-34,-37,-24,-25,-31,-33,-22,-23,-26,-27,-28,-29,-40,124,-35,-36,-20,-21,]),'SUM':([24,25,],[54,55,]),'LPAR':([26,30,31,],[56,60,61,]),'BLOCK':([27,28,],[57,58,]),'LIGHT':([29,],[59,]),'NUM':([36,57,58,60,61,71,87,88,100,101,],[66,79,81,83,84,91,103,104,111,112,]),'PROC':([38,],[68,]),'LEFT':([56,],[74,]),'RIGHT':([56,],[75,]),'BACK':([56,],[76,]),'SAME':([56,],[77,]),'RPAR':([74,75,76,77,111,112,],[94,95,96,97,116,117,]),'COMMA':([83,84,],[100,101,]),'TIMES':([103,],[113,]),'THEN':([104,],[114,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'programa':([0,],[1,]),'variable':([0,],[2,]),'variable1':([3,],[5,]),'expresiones':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,90,113,114,],[7,39,40,41,42,43,44,45,46,47,48,49,50,52,63,70,105,118,119,]),'asignar':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,90,113,114,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'actualizar':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,90,113,114,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'cambiar_direccion':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,90,113,114,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'colocar':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,90,113,114,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'elevar':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,90,113,114,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'encender':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,90,113,114,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'mover':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,90,113,114,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'pos_inicio':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,90,113,114,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'llamar':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,90,113,114,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'c_keep':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,90,113,114,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'c_for':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,90,113,114,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'c_when':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,51,90,113,114,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'epsilon':([4,8,9,10,11,12,13,14,15,16,17,18,19,21,33,38,51,90,113,114,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,69,22,22,22,22,]),'procedimientos':([38,],[67,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> programa","S'",1,None,None,None),
  ('programa -> variable BEGIN expresiones END procedimientos','programa',5,'p_programa','AnalizadorSintactico.py',42),
  ('variable -> VAR variable1','variable',2,'p_variable','AnalizadorSintactico.py',47),
  ('variable1 -> ID ASSIGN NUM SEMICOLON','variable1',4,'p_variable1','AnalizadorSintactico.py',51),
  ('variable1 -> ID SEMICOLON','variable1',2,'p_variable1_1','AnalizadorSintactico.py',59),
  ('expresiones -> asignar expresiones','expresiones',2,'p_expresiones1','AnalizadorSintactico.py',70),
  ('expresiones -> actualizar expresiones','expresiones',2,'p_expresiones2','AnalizadorSintactico.py',73),
  ('expresiones -> cambiar_direccion expresiones','expresiones',2,'p_expresiones3','AnalizadorSintactico.py',76),
  ('expresiones -> colocar expresiones','expresiones',2,'p_expresiones4','AnalizadorSintactico.py',80),
  ('expresiones -> elevar expresiones','expresiones',2,'p_expresiones5','AnalizadorSintactico.py',84),
  ('expresiones -> encender expresiones','expresiones',2,'p_expresiones6','AnalizadorSintactico.py',87),
  ('expresiones -> mover expresiones','expresiones',2,'p_expresiones7','AnalizadorSintactico.py',91),
  ('expresiones -> pos_inicio expresiones','expresiones',2,'p_expresiones8','AnalizadorSintactico.py',94),
  ('expresiones -> llamar expresiones','expresiones',2,'p_expresiones9','AnalizadorSintactico.py',98),
  ('expresiones -> c_keep expresiones','expresiones',2,'p_expresiones10','AnalizadorSintactico.py',101),
  ('expresiones -> c_for expresiones','expresiones',2,'p_expresiones11','AnalizadorSintactico.py',104),
  ('expresiones -> c_when expresiones','expresiones',2,'p_expresiones12','AnalizadorSintactico.py',107),
  ('expresiones -> SKIP SEMICOLON expresiones','expresiones',3,'p_expresiones13','AnalizadorSintactico.py',110),
  ('expresiones -> COMMENT expresiones','expresiones',2,'p_expresiones14','AnalizadorSintactico.py',113),
  ('expresiones -> epsilon','expresiones',1,'p_expresionesEpsilon','AnalizadorSintactico.py',116),
  ('c_for -> FOR ID ASSIGN NUM TIMES expresiones FEND SEMICOLON','c_for',8,'p_cicloFor','AnalizadorSintactico.py',119),
  ('c_when -> WHEN ID ASSIGN NUM THEN expresiones WHEND SEMICOLON','c_when',8,'p_cicloWhen','AnalizadorSintactico.py',125),
  ('c_keep -> KEEP expresiones KEND SEMICOLON','c_keep',4,'p_cicloKeep','AnalizadorSintactico.py',130),
  ('asignar -> SET ID ASSIGN NUM SEMICOLON','asignar',5,'p_asignar','AnalizadorSintactico.py',136),
  ('actualizar -> ADD SUM ID SEMICOLON','actualizar',4,'p_actualizar','AnalizadorSintactico.py',145),
  ('actualizar -> LESS SUM ID SEMICOLON','actualizar',4,'p_actualizar_1','AnalizadorSintactico.py',151),
  ('cambiar_direccion -> CHANGEDIR LPAR LEFT RPAR SEMICOLON','cambiar_direccion',5,'p_cambiar_direccion1','AnalizadorSintactico.py',157),
  ('cambiar_direccion -> CHANGEDIR LPAR RIGHT RPAR SEMICOLON','cambiar_direccion',5,'p_cambiar_direccion2','AnalizadorSintactico.py',166),
  ('cambiar_direccion -> CHANGEDIR LPAR BACK RPAR SEMICOLON','cambiar_direccion',5,'p_cambiar_direccion3','AnalizadorSintactico.py',174),
  ('cambiar_direccion -> CHANGEDIR LPAR SAME RPAR SEMICOLON','cambiar_direccion',5,'p_cambiar_direccion4','AnalizadorSintactico.py',182),
  ('colocar -> PLACE BLOCK SEMICOLON','colocar',3,'p_colocar1','AnalizadorSintactico.py',190),
  ('colocar -> PLACE BLOCK NUM SEMICOLON','colocar',4,'p_colocar1_2','AnalizadorSintactico.py',198),
  ('elevar -> HIGH BLOCK SEMICOLON','elevar',3,'p_elevar1','AnalizadorSintactico.py',216),
  ('elevar -> HIGH BLOCK NUM SEMICOLON','elevar',4,'p_elevarr1_2','AnalizadorSintactico.py',223),
  ('encender -> PUT LIGHT SEMICOLON','encender',3,'p_encender','AnalizadorSintactico.py',230),
  ('mover -> POS LPAR NUM COMMA NUM RPAR SEMICOLON','mover',7,'p_mover','AnalizadorSintactico.py',236),
  ('pos_inicio -> POSSTART LPAR NUM COMMA NUM RPAR SEMICOLON','pos_inicio',7,'p_pos_inicio','AnalizadorSintactico.py',241),
  ('llamar -> CALL ID SEMICOLON','llamar',3,'p_llamar','AnalizadorSintactico.py',246),
  ('procedimientos -> PROC ID expresiones ENDPROC SEMICOLON','procedimientos',5,'p_procedimientos_1','AnalizadorSintactico.py',249),
  ('procedimientos -> epsilon','procedimientos',1,'p_procedimientos_2','AnalizadorSintactico.py',252),
  ('epsilon -> <empty>','epsilon',0,'p_epsilon','AnalizadorSintactico.py',255),
]
