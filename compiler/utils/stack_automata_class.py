class Stack:
    def __init__(self):
        self.__list = []

    def push(self, key):
        self.__list.append(key)

    def pop(self, n=0):
        return self.__list.pop(n)

    def top(self):
        return self.__list[-1]

    def size(self):
        return len(self.__list)

    def is_empty(self):
        return len(self.__list) == 0

    def reset(self):
        self.__list = []


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
        self.state = _initial_state
        self.initial_state = _initial_state
        self.stack = Stack()
        self.syntactic_table = _table

    def automata_goto(self, char_input):
        # makes the transition to the next state
        # then return the new state (it'll be useful for the syntactic analyser)
        self.state = self.syntactic_table.goto(state=self.state, symbol=char_input)
        return self.state

    def stack_action(self, char_input):
        # perform a stack action
        # first look up the action table, given the state and the input
        # then perform the action on the stack
        action = self.syntactic_table.action(state=self.state, symbol=char_input)
        # there are 4 possible values for action:
            # shift
            # reduce
            # error
            # accept

    def reset(self):
        # resets state back to the initial state
        self.state = self.initial_state
        self.stack.reset()

    def get_state(self):
        # return the current state
        return self.state

