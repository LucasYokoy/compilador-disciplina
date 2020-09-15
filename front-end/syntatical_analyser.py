#imports the lexical analyser (LA) as a function
#imports the code_splitter
from .lexical_analyser import lexical_analyser_function as LAF
from .lexical_analyser import code_splitter

path = ""
#syntatical analyser function
def syntatical_analyser(path):
    #wraps in a try catch block
    try:
        #calls the code_splitter function
        code_splitter(path)
        #catch error if the file path is invalid.
        # wraps in a do while loop
        analyser = LAF(path)
        token = ("","","")
        while token[0] != 'EOF':
            # calls the next() on the lexical analyser function
            token = analyser.next()
            # finishes when the lexical analyser returns the END_OF_FILE token
        # if an error is thrown by the LA, display error message and shut down
    except FileNotFoundError:
        print("ERROR: invalid file path")
    except Exception as e:
        print(e.message)