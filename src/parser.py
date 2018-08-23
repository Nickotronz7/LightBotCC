

class Parser(object):

    def __init__(self, tokens):

            # Se almacenaran todos los tokens creados por el lexer
            self.tokens = tokens

            # Index del token que estamos parceando
            self.tokens_index = 0

    def parse(self):

        while self.tokens_index < len(self.tokens):

            # Guarda el tipo de token e.g: INTIGER
            token_type  = self.tokens[self.tokens_index][0]

            # Guarda el valor del token e.g: 5
            token_value = self.tokens[self.tokens_index][1]

            print(token_type, token_value)

            # Se avanza para analizar el siguiente token
            self.tokens_index += 1