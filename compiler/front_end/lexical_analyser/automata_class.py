class Automata:
    def __init__(self, transition_table_dict, initial_state, final_states):
        # estado inicial deve ser uma string
        # estado final deve ser uma lista de strings, cada uma com os nomes dos estados finais
        # transition_table_dict deve ser um dicionário de dicionários de strings para strings
        # na seguinte forma: tabela[estado_atual][input] => 'estado_futuro'
        # caso a transição do estado 's' seja do tipo '.' para x exceto 'a' para 'xa', 'b' para 'xb'...;
        # a tabela deve ser no formato: 's': {'.': 'x', 'a': 'xa', 'b': 'xb', ...}
        self.state = initial_state
        self.initial_state = initial_state
        self.final_states = final_states
        self.transition_table = transition_table_dict
        self.transition_table['pit'] = {'.': 'pit'}

    def state_transition(self, char_input):
        # makes the transition to the next state
        # if the character read is invalid, jump to pit state and proceed
        try:
            accepted_inputs = list(self.transition_table[self.state].keys())
            possible_transitions = self.transition_table[self.state]
            if '.' in accepted_inputs:
                if char_input in accepted_inputs:
                    self.state = possible_transitions[char_input]
                else:
                    self.state = possible_transitions['.']
            else:
                self.state = possible_transitions[char_input]
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
