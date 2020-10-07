from compiler.front_end.lexical_analyser.automata_class import Automata

transition_table = {
    'q0': {'L': 'q1', 'E': 'q1', 'e': 'q1', 'D': 'q2', '{': 'q8', '<': 'q10', '>': 'q14', '=': 'q16', '+': 'q17',
           '-': 'q18', '*': 'q19', '/': 'q20', ';': 'q21', ')': 'q22', '(': 'q23', '"': 'q25'},
    'q1': {'L': 'q1', 'E': 'q1', 'e': 'q1', 'D': 'q1', '_': 'q1'},
    'q2': {'D': 'q2', 'P': 'q3', 'E': 'q5', 'e': 'q5'},
    'q3': {'D': 'q4'},
    'q4': {'D': 'q4'},
    'q5': {'+': 'q6', '-': 'q6', 'D': 'q7'},
    'q6': {'D': 'q7'},
    'q7': {'D': 'q7'},
    'q8': {'L': 'q8', 'E': 'q8', 'e': 'q8', 'D': 'q8', '+': 'q8', '-': 'q8', '*': 'q8', '/': 'q8', '(': 'q8', ')': 'q8',
           ';': 'q8', '<': 'q8', '>': 'q8', '=': 'q8', '{': 'q8', '"': 'q8', '_': 'q8', ' ': 'q8', ':': 'q8', '}': 'q9'},
    'q10': {'>': 'q11', '=': 'q12', '-': 'q13'},
    'q14': {'=': 'q15'},
    'q25': {'L': 'q25', 'E': 'q25', 'e': 'q25', 'D': 'q25', '+': 'q25', '-': 'q25', '*': 'q25', '/': 'q25', '(': 'q25',
            ')': 'q25', ';': 'q25', '<': 'q25', '>': 'q25', '=': 'q25', '{': 'q25', '}': 'q25', ' ': 'q25', '_': 'q25', ':': 'q25', '\\': 'q25', '"': 'q26'}
}
initial_state = 'q0'
final_states = ['q1', 'q2', 'q4', 'q7', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q26']


automaton = Automata(transition_table, initial_state, final_states)