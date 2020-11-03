# imports the symbol table
# imports the lexical analyser (LA) as a function
# imports the code_splitter
# from compiler.front_end import lexical_analyser as LA
from compiler.front_end.lexical_analyser.lexical_analyser import lexical_analyser_function as laf
from compiler.front_end.lexical_analyser.lexical_analyser import code_splitter
from compiler.symbol_table import symbol_table


def syntactical_analyser_function(input_path):
    # wraps in a try catch block
    try:
        # calls the code_splitter function
        code_splitter(input_path)
        # catch error if the file path is invalid.
        # wraps in a while loop
        analyser = laf()
        token = ("", "", "")
        while token[1] != 'EOF':
            # calls the next() on the lexical analyser function
            # finishes when the lexical analyser returns the END_OF_FILE token
            token = next(analyser)
            # appends tuple to the symbol table
            print(token)
        # if an error is thrown by the LA, display error message and continue
    except FileNotFoundError:
        print("ERROR: invalid file path")

    print(symbol_table)


# receber o próximo token
    # deve também receber a linha e a coluna do token recebido, para mostrar em caso de erro
# passar token pelo autômato
    # autômato retorna o novo estado e a ação a ser realizada
# realizar a ação na pilha
# repetir até chegar no token EOF

if __name__ == "__main__":
    path = "/compiler/test/test_file.txt"
    syntactical_analyser_function(input_path=path)
