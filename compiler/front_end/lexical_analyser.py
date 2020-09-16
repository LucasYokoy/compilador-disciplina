# imports the symbol_table
from compiler.symbol_table import symbol_table
import re


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
        new_line = line.replace("\n", "")
        new_line = re.sub("\\\\n", "\\n", new_line)
        new_line = new_line.strip()

        # Detect special symbols, such as (, ), +, *, ;, etc (look up in the tokens table),
        # then insert a blank space before and after them.
        # this ensures these symbols are isolated, when the code is split by "\s"
        special_symbols = ["<=", "<>", "<-", "=", "<", ">", "+", "-", "*", "/", ")", "(", ";"]
        for symbol_index, symbol in enumerate(special_symbols):
            new_line = re.sub(re.escape(symbol), f" {hex(symbol_index)} ", new_line)
        for symbol_index, symbol in enumerate(special_symbols):
            new_line = re.sub(str(hex(symbol_index)), f" {symbol} ", new_line)

        # then detect comments and erases spaces, to make sure they count as a single word during compilation.
        # use "\\\\n" as temporary separator, because this character was excluded in the second operation of this loop
        temporary_separator = "\\\\n"
        if re.search(r"{.*}", new_line):
            new_line = re.sub(" ", temporary_separator, new_line)
        # do the same with strings. But strings shouldn't be altered
        string_list = re.findall(r"\".*\"", new_line)
        if string_list:
            for string in string_list:
                new_line = re.sub(string, string.replace(" ", temporary_separator), new_line)
        # turn that list of string into a list of lists of words, separating the strings on the list by blank space
        new_line = new_line.split()

        # now look for comments and strings, and turn the temporary_separator back into blank spaces
        for word_index, word in enumerate(new_line):
            new_line[word_index] = re.sub(temporary_separator, " ", word)

        # finally, append the new line to the split_code
        split_code[line_number] = new_line

    print(split_code)


# character classifier function:
# takes a character as argument
    # classifies the character as letter,  digit,  or special symbol
    # checks all possibilities on a stream of if else,  and returns the type as a corresponding number.
        # if it's a letter,  or a digit,  return D our L
        # else,  return the character itself (implies it's a ;, ), (,  etc).

# automaton function:
# receives the word as an argument
    # loops through each character in the word
        # calls the character classifier function for the character,
        # and returns the character's class (a corresponding numeric code)
        # runs the character's class,  into the automata,  as a transition of state
    # throws an error if the state it ends on isn't a final state (Exception)
    # generates token based on the final state of the automata
        # given the final state of the automaton,  determine token
        # tuple in the form (token, word, attributes)
    # returns the tuple


# analyser function:
def lexical_analyser_function():
    for i in range(10):
        yield "stub", "", ""
    yield "EOF", "", ""
    # uses a generator
        # loops through each line on the split code (with the number of the line)
            # loops through each word on the line
                #  wrap in try catch
                    # calls the automaton function for that word
                    # if the token is an id,  verify if it's already in the symbol table
                        # if so, return the token that is already on the table
                #  if the automaton throws an Exception,  the token will be:
                # ("ERROR", f"ERROR: invalid symbol at {line_number}: "{word}"", "{line_number}, {word_number}")
                    #  also print: f"ERROR: invalid symbol at {line_number}: "{word}""
                #  yields the token tuple
        # as soon as the loop ends,  generate token ("EOF", "", "")
            # yields the token tuple
