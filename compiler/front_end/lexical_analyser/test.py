from compiler.front_end.lexical_analyser.lexical_analyser import Automata

transition_table = {
    'q0': {'a': 'q1'},
    'q1': {'b': 'q2'},
    'q2': {'c': 'q3', 'a': 'q4'},
    'q3': {'d': 'q4'},
    'q4': {'a': 'q3'},
    'pit': {},
}
initial_state = 'q0'
final_state = ['q2', 'q4']
automaton = Automata(transition_table, initial_state, final_state)

automaton.state_transition('a')
automaton.state_transition('b')
automaton.state_transition('c')
automaton.state_transition('d')
final_state = automaton.finish()
print(final_state)

automaton.state_transition('a')
automaton.state_transition('b')
automaton.state_transition('c')
automaton.state_transition('d')
automaton.state_transition('a')
final_state = automaton.finish()
print(final_state)

automaton.state_transition('a')
automaton.state_transition('b')
final_state = automaton.finish()
print(final_state)

automaton.state_transition('a')
final_state = automaton.finish()
print(final_state)

automaton.state_transition('§')
final_state = automaton.finish()
print(final_state)