# CS4450 Parser Project
This is the final project for CS4450 - Principles of Programming Langauges. This project implements a basic parser for a subset of Python using `ANTLR`. It is tested with Python.

## Getting Started
### Dependencies
* [ANTLR Parser Generator Version 4.13.2](https://www.antlr.org/download.html)
* [The latest version of Python3](https://www.python.org/downloads/)
    * After installation, run the command `pip install antlr4-python3-runtime`
### Usage
To use, firist download the source code. In your preferred terminal run:

`antlr4 -Dlanguage=Python3 PythonParser.g4`

The grammar then be compiled on your machine. Then you can run `python main.py` to generate a parse "tree". 

*Alternative way to generate parse tree...*
1. Search [lab.antlr.org](http://lab.antlr.org/)
2. Click top left "Lexer" tab
3. Delete everything in Lexer's window
4. Return to "Parser" tab
5. Copy & Paste in everything in this repository's "grammar/PythonParser.g4" file
6. Copy & Paste in any file in this repository's "grammar/example/" folder to antlr lab's right "Input" window  
7. Click run to generate a parse "tree"
   
If you'd like to try your own input file, you can create a new python file and write some code *(note that not all python syntax is supported)*, then modify main.py to run your specified file or paste this into "Input" window of lab.antlr.org website.


## Project Demo
[Demo Video](https://youtu.be/-xDXDPQzH8I)

## Authors
* Wen-Hsin Chen
* Julian Fletcher
* Braeden Songer
* Evelyn Wilbur

