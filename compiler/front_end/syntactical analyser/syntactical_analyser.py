# imports the symbol table
# imports the lexical analyser (LA) as a function
# imports the code_splitter
# from compiler.front_end import lexical_analyser as LA
from compiler.front_end.lexical_analyser.lexical_analyser import lexical_analyser_function as laf
from compiler.front_end.lexical_analyser.lexical_analyser import code_splitter
from compiler.symbol_table import symbol_table
from .lr_automaton import lr_automaton

"""
construir a tabela shift-reduce:
criar a gramática livre de context aumentada, caso necessário
Enumerar a gramática;
Criar o autômato LR(0) de itens pontilhados para a formação da tabela sintática;
CGerar os conjuntos primeiro e seguinte dos não terminais da gramática
Construir a tabela sintática

Implementar o algoritmo para análise sintática LR baseado na tabela de análise desenvolvida atra´ves dos itens de a:

"""


def generate_lexical(input_path):
    # abrir o código fonte e retornar o gerador de tokens.
    try:
        # calls the code_splitter function
        code_splitter(input_path)
        # catch error if the file path is invalid.
        # wraps in a while loop
        analyser = laf()
        # return token generator
        return analyser
    except FileNotFoundError:
        print("ERROR: invalid file path")


def automaton_function(_automaton, token):
    _automaton.state_transition(char_input=token[1])
    return _automaton.get_state()


def lr_analyser(_stack, _state, _input):
    # pseudocódigo do livro do dragão
    pass


def syntactical_analyser_function(_automaton, input_path):
    generator = generate_lexical(input_path)
    last_token = ('', '', '')
    _automaton.reset()
    while last_token[1] != 'EOF':
        # receber o próximo token
            # deve também receber a linha e a coluna do token recebido, para mostrar em caso de erro
        token, line_number, word_number = next(generator)
        # passar token pelo autômato
            # autômato retorna o novo estado e a ação a ser realizada
        # realizar a ação na pilha
            # usar classe customizada como stack
    
    # repetir até chegar no token EOF


if __name__ == "__main__":
    path = "/compiler/test/test_file.txt"
    syntactical_analyser_function(_automaton=lr_automaton, input_path=path)
