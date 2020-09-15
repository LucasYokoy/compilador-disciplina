#imports the symbol_table
#import re (regex module)

#global variable: splitted code
splitted_code = []
#code splitter function:
def code_splitter(path):
    #opens and reads the directory given on the string.
    file = open(path,'r')

    #splits the text into a matrix of strings (words)
        #first, detect special symbols using regex, such as (,),+,*,;, etc (look up in the tokens table), and insert a blank space before and after them.
        #this ensures these symbols are isolated, when the code is splitted by "\s"
        #then detect comments and erases spaces, to make sure they count as a single word during compilation.
        #create a list of strings, separating the code by new line
        #turn that list of string into a list of lists of words, separating the strings on the list by blank space
    #remember to close file after  you're done
    file.close()

#character classifier function:
    #classifies the character as letter, digit, or special symbol using regex
    #checks all possibilities on a stream of ifelse, and returns the type as a corresponding number.

#automaton function:
#receives the word as an argument
    #loops thru each character in the word
        #calls the character classifier function for the character, and returns the character's class
        #runs the character's class, into the automata, as a transition of state
    #throws an error if the state it ends on isn't a final state (RejectionException)
    #generates token based on the final state of the automata
        #given the final state of the automaton, determine token
        #tuple in the form (token,word,attributes)
        #appends tuple to the symbol table
    #returns the tuple

#analyser function:
def lexical_analyser_function():
    yield "stub"
    #uses a generator
    #wrap in try catch
    #loops thru each line on the splitted code
        #loops thru each word on the line
            #calls the automaton function for that word
            #yields the token tuple
    #throws an error if the automaton function throws an error (use raise Exception() statement)
        #error message contains: f"ERROR: invalid symbol at {line}: "{word}""