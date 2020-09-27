class Automata:
    def __init__(self, transition_table_dict):
        self.state = 0
        self.transition_table_dict = transition_table_dict
        self.transition_table = create_transition_table(transition_table_dict)

    def state_transition(self, input):
        pass

    def reset_state(self):
        pass

def create_transition_table(table):
    pass
