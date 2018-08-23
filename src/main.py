
import parser
import lexer


def main():
    #Head the currente flow source code in test.lang and store it in varible
    with open('test.lang') as file:
        content = file.read()

        #
        # Lexer
        #

        lex = lexer.Lexer(content)
        tokens = lex.tokensize()


        #
        # Parser
        #
        parse = parser.Parser(tokens)
        parse.parse()




main()