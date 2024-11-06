import sys
from antlr4 import *
from PythonParserLexer import PythonParserLexer
from PythonParserParser import PythonParserParser

def parse_file(file_path):
    #Read the input file
    input_stream = FileStream(file_path)
    
    #Create a lexer instance
    lexer = PythonParserLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    
    #Create a parser instance
    parser = PythonParserParser(token_stream)
    
    #Start parsing from the start rule (begin)
    tree = parser.begin()
    
    #Print the parse tree
    print(tree.toStringTree(recog=parser)) #Do we need to pass t=tree

if __name__ == "__main__":
    if len(sys.argv) < 2: #Improper inputs given
        print("Usage: python main.py <input_file>")
    else:
        parse_file(sys.argv[1])