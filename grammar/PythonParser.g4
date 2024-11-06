grammar PythonParser;


outer_block: 'def' VARNAME '():' NEWLINE inner_block; // Can add loop and other control statements later -- functions or control loops
inner_block: INDENT expr;

expr:	assignment
	| expr ('+'|'-') expr
	| expr ('*'|'/') expr
	| INT 
	| FLOAT;

assignment:	VARNAME '=' expr NEWLINE
	| VARNAME '+=' expr;

 

// Data types
INT:	[+-]?[0-9]+;
FLOAT: [+-]?[0-9]*'.'[0-9]+;
VARNAME: [a-zA-Z_]+[a-zA-Z_0-9]*;

// Syntax
NEWLINE: '\r'? '\n';
INDENT: '\t';
WS : [ \t\r\n]+ -> skip ;