# imports the symbol_table
from compiler.symbol_table import symbol_table
import re
from compiler.front_end.lexical_analyser.automata_class import Automata


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

        # turn that list of string into a list of lists of words, separating the strings on the list by blank space
        new_line = new_line.split()

        # now look for comments and strings, and turn the temp_separator back into blank spaces
        for word_index, word in enumerate(new_line):
            new_line[word_index] = re.sub(temp_separator, " ", word)

        # finally, append the new line to the split_code
        split_code[line_number] = new_line


# character classifier function:
# takes a character as argument
def character_classifier(character):
    # classifies the character as letter,  digit,  or special symbol
    alphabet = 'abcdefghijklmnopqrstuvwxyzãõáéíóúâêîôûüç'
    alphabet = alphabet + alphabet.upper()
    numbers = '1234567890'
    # checks all possibilities on a stream of if else,  and returns the type as a corresponding number.
    # if it's a letter, L
    if character in alphabet:
        return 'L'
    # if it's a digit, return D
    elif character in numbers:
        return 'D'
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
    # generates token based on the final state of the automata
        # given the final state of the automaton,  determine token
        # tuple in the form (token, word, attributes)
    # returns the tuple


# analyser function:
def lexical_analyser_function():
    for i in range(10):
        yield "stub", "", ""
    yield "EOF", "", ""
    # sets up the automaton
    automaton = Automata()
    # uses a generator
        # loops through each line on the split code (with the number of the line)
            # loops through each word on the line
                #  wrap in try catch
                    # calls the automaton function for that word
                    # if the token is an id,  verify if it's already in the symbol table
                        # if so, return the token that is already on the table
                        # remember to reset the automaton
                #  if the automaton throws an Exception,  the token will be:
                # ("ERROR", f"ERROR: invalid symbol at {line_number}: "{word}"", "{line_number}, {word_number}")
                    #  also print: f"ERROR: invalid symbol at {line_number}: "{word}""
                    # remember to reset the automaton
                #  yields the token tuple
        # as soon as the loop ends,  generate token ("EOF", "", "")
            # yields the token tuple
