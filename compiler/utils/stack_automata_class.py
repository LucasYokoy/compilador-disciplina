class _Stack:
    def __init__(self, initial_state):
        self.__empty_stack = [initial_state]
        self.__list = self.__empty_stack

    def shift(self, value):
        self.__list.append(value)

    def reduce(self, n=1):
        del self.__list[-n:]

    def top(self):
        return self.__list[-1]

    def size(self):
        return len(self.__list)

    def is_empty(self):
        return len(self.__list) == 0

    def reset_stack(self):
        self.__list = self.__empty_stack


class SyntacticTable:
    def __init__(self, _action_table, _goto_table):
        self.__action_table = _action_table
        self.__goto_table = _goto_table

    def action(self, state, symbol):
        try:
            return self.__action_table[(state, symbol)]
        except KeyError:
            return 'ERROR'

    def goto(self, state, symbol):
        try:
            return self.__goto_table[(state, symbol)]
        except KeyError:
            return 'ERROR'


class StackAutomata:
    def __init__(self, _table, _initial_state):
        # as tabelas de transição devem ser inseridas da mesma forma que no autômato finito
        # mas não há calabouço, apenas estados de erro definidos na própria definição da tabela sintática
        # também não há a necessidade de implementar a transição '.'
        # também não há função finish que retorna o estado final, apenas as funções reset e get_state
        self.stack = _Stack(_initial_state)
        self.syntactic_table = _table

    def automata_goto(self, state, char_input):
        # takes the input and searches for the goto state on the goto_list
        return self.syntactic_table.goto(state=state, symbol=char_input)

    def automata_action(self, state, char_input):
        # takes the input and searches for the action on the action_list
        return self.syntactic_table.action(state=state, symbol=char_input)
        # there are 4 possible values for action: shift, reduce, error, accept
        # they each must have their own function, except accept and error

    def stack_shift(self, value):
        # shifts a value into the stack
        self.stack.shift(value)

    def stack_reduce(self, n):
        # pops n items from the stack
        self.stack.reduce(n)

    def reset(self):
        # resets state back to the initial state
        self.stack.reset_stack()

    def get_state(self):
        # return the current state
        return self.stack.top()
