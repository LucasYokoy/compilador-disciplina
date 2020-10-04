class Automata:
    def __init__(self, transition_table_dict, initial_state, final_states):
        # estado inicial deve ser uma string
        # estado final deve ser uma lista de strings, cada uma com os nomes dos estados finais
        # transition_table_dict deve ser um dicionário de dicionários de strings para strings
        # na seguinte forma: tabela[estado_atual][input] => 'estado_futuro'
        # na tabela de transição, sempre deve haver um estado chamado 'pit', que é o "calabouço"
        # o calabouço deve ter o formato 'pit': {'.': 'pit'} pois não se pode sair dele
        self.state = initial_state
        self.initial_state = initial_state
        self.final_states = final_states
        self.transition_table = transition_table_dict
        self.transition_table['pit'] = {'.': 'pit'}

    def state_transition(self, char_input):
        # makes the transition to the next state
        # if the character read is invalid, jump to pit state and proceed
        try:
            if list(self.transition_table[self.state].keys())[0] == '.':
                self.state = self.transition_table[self.state]['.']
            else:
                self.state = self.transition_table[self.state][char_input]
        except:
            self.state = 'pit'

    def reset_state(self):
        # resets state back to the initial state
        self.state = self.initial_state

    def finish(self):
        # gives the final state or an error
        if self.state in self.final_states:
            final_state = self.get_state()
            self.reset_state()
            return final_state
        else:
            self.reset_state()
            return 'ERROR'

    def get_state(self):
        # return the current state
        return self.state
