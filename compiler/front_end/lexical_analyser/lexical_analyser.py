from compiler.symbol_table import symbol_table
import compiler.front_end.lexical_analyser.mgol_automaton as mgol_a
import re
from compiler.utils.automata_class import Automata


# global variable: split code
split_code = []


# code splitter function:
def code_splitter(path):
    # opens and reads the directory given, as a list of strings
    file = open(path, 'r')
    for line in file:
        split_code.append(line)
    # remember to close file after  you're done
    file.close()

    for line_number, line in enumerate(split_code):
        # first, trim the text from \n and trailing \s characters
        new_line = re.sub(r".*\\n$", "", line)
        # new_line = re.sub("\\\\n", "\\n", new_line)
        new_line = new_line.strip()

        # use an exclusive combination of characters as a temporary separator
        temp_separator = "SPACE"

        # Detect special symbols, such as (, ), +, *, ;, etc (look up in the tokens table),
        # then insert a blank space before and after them.
        # this ensures these symbols are isolated, when the code is split by "\s"
        special_symbols = ["<=", "<>", "<-", "=", "<", ">", "+", "-", "*", "/", ")", "(", ";"]
        for symbol_index, symbol in enumerate(special_symbols):
            new_line = re.sub(re.escape(symbol), f" {temp_separator}{symbol_index}{temp_separator} ", new_line)
        for symbol_index, symbol in enumerate(special_symbols):
            new_line = re.sub(str(f"{temp_separator}{symbol_index}{temp_separator}"), f" {symbol} ", new_line)

        # then detect comments and erases spaces, to make sure they count as a single word during compilation.
        # do the same with strings. Remember that the content of neither should be altered
        string_list = re.findall(r"\".*\"|{.*}", new_line)
        if string_list:
            for match in string_list:
                match_altered = re.sub(r" ", temp_separator, match)
                new_line = new_line.replace(match, match_altered)

        # then detect exponents and erases spaces, to make sure they count as a single word during compilation.
        string_list = re.findall(r"\d+\.?\d*\s*[Ee]\s*[+-]?\s*\d+", new_line)
        if string_list:
            for match in string_list:
                match_altered = re.sub(r" ", temp_separator, match)
                new_line = new_line.replace(match, match_altered)

        # turn that list of string into a list of lists of words, separating the strings on the list by blank space
        new_line = new_line.split()

        # now look for comments and strings, and turn the temp_separator back into blank spaces
        for word_index, word in enumerate(new_line):
            new_line[word_index] = re.sub(temp_separator, " ", word)

        # finally, append the new line to the split_code
        split_code[line_number] = new_line


# return a line of the split code
def code_line(index):
    return split_code[index]


# character classifier function:
# takes a character as argument
def character_classifier(character):
    # classifies the character as letter,  digit,  or special symbol
    alphabet = 'abcdfghijklmnopqrstuvwxyzãõáíóúâîôûüç'
    alphabet = alphabet + alphabet.upper()
    numbers = '1234567890'
    # checks all possibilities on a stream of if else,  and returns the type as a corresponding number.
    # if it's a letter, L
    if character in alphabet:
        return 'L'
    # if it's a digit, return D
    elif character in numbers:
        return 'D'
    # if it's a point, return P
    elif character == '.':
        return 'P'
    else:
    # else, return the character itself (implies it's a ;, ), (,  etc).
        return character


# automaton function:
# receives the word as an argument
def automaton_function(automaton, word):
    # loops through each character in the word
    for character in word:
        # calls the character classifier function for the character,
        char_input = character_classifier(character)
        # runs the character's class,  into the automata,  as a transition of state
        automaton.state_transition(char_input=char_input)
    # gets the final state of the automaton
    final_state = automaton.finish()
    # throws an error if the state it ends on isn't a final state (Exception)
    if final_state == 'ERROR':
        raise Exception
    else:
        # otherwise, returns the final state
        return final_state


RESERVED_WORDS = ['inicio', 'varinicio', 'varfim', 'escreva', 'leia', 'se', 'entao',
                  'fimse', 'fim', 'lit', 'real', 'inteiro']


def generate_token(final_state, word):
    c_dict = {"q1": "id", "q2": "num", "q4": "num", "q7": "num", "q9": "comment", "q10": "opr", "q11": "opr",
              "q12": "opr", "q13": "rcb", "q14": "opr", "q15": "opr", "q16": "opr", "q17": "opm", "q18": "opm",
              "q19": "opm", "q20": "opm", "q21": "pt_v", "q22": "fc_p", "q23": "ab_p", "q26": "literal"}

    final_state = c_dict[final_state]

    # given the final state of the automaton, determine token
    # tuple in the form (lexeme, token, type='') the last parameter should be null, as required
    # if the token is a reserved word, the token will be a ('word', 'word', '')
    if word in RESERVED_WORDS:
        return word, word, ''
    # if the token is an id, verify if the lexeme is already in the symbol table
    # if so, return the token that is already on the table
    # otherwise, create a new token in the end
    if final_state == 'id':
        for token in symbol_table:
            if token[0] == word:
                return token
    # if it's a comment, return an empty token
    if final_state == 'comment':
        return '', '', ''
    # if it's anything else, return the word and the final_state

    return word, final_state, ''


# analyser function:
def lexical_analyser_function():
    # sets up the automaton
    automaton = Automata(transition_table_dict=mgol_a.transition_table,
                         initial_state=mgol_a.initial_state,
                         final_states=mgol_a.final_states)
    # uses a generator
    # loops through each line on the split code (with the number of the line)
    line_number = 0
    word_number = 0
    for ln, line in enumerate(split_code):
        line_number = ln
        # loops through each word on the line
        for wn, word in enumerate(line):
            word_number = wn
            #  wrap in try catch
            # noinspection PyBroadException
            try:
                # calls the automaton function for that word
                final_state = automaton_function(automaton, word)
                # generates token based on the final state of the automata
                token = generate_token(final_state, word)
            #  if the automaton throws an Exception,  the token will be:
            # ("ERROR", f"ERROR: invalid symbol at {line_number}: "{word}"", "{line_number}, {word_number}")
            except Exception:
                error_message = f"ERROR: invalid symbol at {line_number}: \"{word}\""
                token = ("ERROR", error_message, f'line:{line_number} word:{word_number}')
                #  also print: f"ERROR: invalid symbol at {line_number}: "{word}""
                print(error_message)
            # yields the token tuple
            # unless the token is a comment, in which case, just continue to the next word
            if token[1] == "":
                continue
            else:
                if token[1] == 'id' or token[1] in RESERVED_WORDS:
                    symbol_table.append(token)
                # always return the token, the line number and the word number for the syntactical_analyser
                yield token, line_number, word_number
            # return that the line (buffer) has ended, by sending the $ symbol at the end of the sentence
            # if token[1] == 'pt_v':
            #     token = ('$', '$', '')
            #     yield token, line_number, word_number
    # as soon as the loop ends,  generate token ("EOF", "", "")
    token = ("", "eof", "")
    # yields the token tuple
    yield token, line_number, word_number
