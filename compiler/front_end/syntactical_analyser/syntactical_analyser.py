# imports the symbol table
# imports the lexical analyser (LA) as a function
# imports the code_splitter
# from compiler.front_end import lexical_analyser as LA
from compiler.front_end.lexical_analyser.lexical_analyser import code_line
from compiler.front_end.lexical_analyser.lexical_analyser import code_splitter
from compiler.front_end.lexical_analyser.lexical_analyser import lexical_analyser_function as laf
from compiler.front_end.syntactical_analyser.lr_automaton import lr_automaton
from compiler.front_end.syntactical_analyser.mgol_grammar import production_rule

"""
construir a tabela shift-reduce:
criar a gramática livre de context aumentada, caso necessário
Enumerar a gramática;
Criar o autômato LR(0) de ítens pontilhados para a formação da tabela sintática;
CGerar os conjuntos primeiro e seguinte dos não terminais da gramática
Construir a tabela sintática

Implementar o algoritmo para análise sintática LR baseado na tabela de análise desenvolvida através dos ítens de a:

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


def error_recovery(_generator, _token, _line_number, _word_number):
    # retorne True se o erro não tiver sido recuperado e a análise desse buffer for terminada, e False se não.
    # modo pânico: chamar todos os próximos tokens, até encontrar um token de sincronização ';'
    # caso não seja encontrado, o erro não foi recuperado
    # primeiramente, indicar que houve um erro na linha e coluna atual, depois tentar recuperar
    # depois, retornar o próximo token viável (atual, se a=='eof', próximo se a=='pt_v')
    print(f'Syntax error: erro sintático na linha {_line_number}, na posição {_word_number}:'
          f' \"{" ".join(code_line(_line_number))}\" sintaxe inválida em {_token[0]}')
    a = ''
    while a not in ['eof', 'pt_v']:
        a, token, line_number, word_number = new_token(_generator)
    if a == 'pt_v':
        a, token, line_number, word_number = new_token(_generator)
    # retornar o próximo token viável para continuar a análise

    return a, token, line_number, word_number


def get_prod_rule(_grammar, _index):
    return _grammar[_index]


def new_token(_generator):
    token = ('', '', '')
    while token == ('', '', ''):
        token, line_number, word_number = next(_generator)
    a = token[1]
    return a, token, line_number, word_number


def syntactical_analyser_function(_automaton, _grammar, _input_path):
    generator = generate_lexical(_input_path)
    last_token = ''
    _automaton.reset()
    # repetir até chegar no token EOF
    # pseucódigo do livro do dragão
    # seja a o primeiro símbolo de w$ no começo da análise
    a, token, line_number, word_number = new_token(generator)
    while last_token != 'eof':
        #   seja s o estado no topo da pilha;
        s = _automaton.get_state()
        #    if(ACTION[s,a] = shift t){
        action = _automaton.automata_action(s, a)
        if action[0] == 'S':
    #        empilhe t;
            t = action[1:]
            _automaton.stack_shift(t)
    #        a recebe o próximo símbolo da entrada;
            a, token, line_number, word_number = new_token(generator)
    #    } else if (ACTION[s,a] = reduce A->b){
        elif action[0] == 'R':
    #       verificar quais são os valores de A e b no arquivo mgol_grammar.py
            index = action[1:]
            a_rule, b = get_prod_rule(_grammar=_grammar, _index=index)
    #        desempilha len(b) símbolos da pilha;
            _automaton.stack_reduce(len(b))
    #        seja t o novo topo da pilha;
            t = _automaton.get_state()
    #        empilhe GOTO[t,A];
            goto = _automaton.automata_goto(t, a_rule)
            if goto != 'ERROR':
                _automaton.stack_shift(goto)
    #        imprima a produção A->b
            print(f'{a_rule} -> {" ".join(b)}')
    #    } else if (ACTION[s,a] = accept) {
        elif action[0] == 'A':
    #        a análise terminou e foi bem sucedida
            break
    #    } else chame rotina de recuperação de erro
        else:
    #        retornar a próxima posição viável para continuar a análise
            last_token, token, line_number, word_number = error_recovery(generator, token, line_number, word_number)
            # # resetar autômato para continuar a análise
            # _automaton.reset()
        # }
        # atualizar o valor de last_token
        last_token = token[1]


if __name__ == "__main__":
    path = "D:\\Documentos\\Compilador\\compiler\\test\\test_file.txt"
    syntactical_analyser_function(_automaton=lr_automaton, _grammar=production_rule, _input_path=path)
