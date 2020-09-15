# imports the symbol_table

# global variable: split code
split_code = []
# code splitter function:


def code_splitter(path):
    # opens and reads the directory given,  as a list of strings
    file = open(path, 'r')

    # first,  detect special symbols using regex, such as (, ), +, *, ;, etc (look up in the tokens table),
    # also insert a blank space before and after them.
    # this ensures these symbols are isolated,  when the code is split by "\s"
    # splits the text into a matrix of strings (words)
        # then detect comments and erases spaces, to make sure they count as a single word during compilation.
        # create a list of strings, separating the code by new line
        # turn that list of string into a list of lists of words, separating the strings on the list by blank space
    # remember to close file after  you're done
    file.close()

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
    # throws an error if the state it ends on isn't a final state (RejectionException)
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
                        # if so,  return the token that is already on the table
                #  if the automaton throws RejectionException,  the token will be:
                # ("ERROR", f"ERROR: invalid symbol at {line_number}: "{word}"", "{line_number}, {word_number}")
                    #  also print: f"ERROR: invalid symbol at {line_number}: "{word}""
                #  yields the token tuple
        # as soon as the loop ends,  generate token ("EOF", "", "")
            # yields the token tuple
