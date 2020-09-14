#imports the symbol_table
#import re (regex module)

#code splitter function:
#splits the text into a matrix of strings (words)
#global variable: splitted code
    #first, detect special symbols using regex, such as (,),+,*,;, etc (look up in the tokens table), and insert a blank space before and after them.
    #this ensures these symbols are isolated, when the code is splitted by "\s"
    #then detect comments and erases spaces, to make sure they count as a single word during compilation.
    #create a list of strings, separating the code by new line
    #turn that list of string into a list of lists of words, separating the strings on the list by blank space

#character classifier function:
    #classifies the character as letter, digit, or special symbol using regex
    #checks all possibilities on a stream of ifelse, and returns the type as a corresponding number.

#automaton function:
#receives the word as an argument
    #loops thru each character in the word
        #calls the character classifier function for the character, and returns the character's class
        #runs the character's class, into the automata, as a transition of state
    #generates token based on the final state of the automata
        #given the final state of the automaton, determine token
        #tuple in the form (token,word,attributes)
        #appends tuple to the symbol table
    #returns the tuple

#analyser function:
    #uses a generator
    #loops thru each line on the splitted code
        #loops thru each word on the line
            #calls the automaton function for that word
            #yields the token tuple
