
import re

class Lexer(object):

    def __init__(self, source_code):
        self.source_code = source_code

    def tokensize(self):

        # Aqui se almacenan todos los tokens creados por el lexer
        tokens = []

        # Crea una lista de palabras a partir del source code
        source_code = self.source_code.split()

        # Se utiliza para mantener un seguimiento de las palabras en el source code
        source_index = 0

        # Loop en donde cada palabra se utiliza para generar los tokens
        while source_index < len(source_code):

            word = source_code[source_index]
            
            # Aqui se reconoce si se da una declaracion de variables
            if word == "var":
                tokens.append(["VAR_DECLERATION", word])
            
            # Se crea el token para una palabra que no sea reservada
            elif re.match('[a-z]', word) or re.match('[A-Z]', word):
                if word[len(word) - 1] == ";":
                    tokens.append(['IDENTIFIER', word[0:len(word) - 1]])
                else:
                    tokens.append(['IDENTIFIER', word])
            
            # Se crea el token para un numero
            elif re.match('[0-9]', word):
                if word[len(word) - 1] == ";":
                    tokens.append(['INTEGER', word[0:len(word) - 1]])
                else:
                    tokens.append(['INTEGER', word])

            # Token de operadores
            elif word in "=/*-+":
                tokens.append(['OPERATOR', word])

            # Si se encuentra (;) se crea el token STATEMENT_END
            if word[len(word) - 1] == ";":
                tokens.append(['STATEMENT_END', ';'])

            # Se aumenta el index para avanzar a la siguiente palabra
            source_index += 1
        
        return tokens