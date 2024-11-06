grammar PythonParser;

// I don't know if this is needed
begin: expr | simple_expr;


expr: var_assign | expr operator expr | VARTYPE | VARNAME ;
simple_expr:  expr operator expr | VARTYPE | VARNAME; // This catches op assignments so no invalid syntax


// Assignment
var_assign: VARNAME '=' expr NEWLINE;
operator_assign: VARNAME op_equals simple_expr;

// Operations
operator: ('+'|'-'|'*'|'/'|'%');
op_equals: ('+='|'-='|'*='|'/='|'%=');


// Data types

VARTYPE: INT | FLOAT| BOOL | STRING;
ARRAY: '[' VARTYPE (','VARTYPE)* ']' ;


INT:	[+-]?[0-9]+;
FLOAT: [+-]?[0-9]*'.'[0-9]+;
BOOL: 'True'|'False';
STRING: '"' [a-zA-Z_0-9]* '"' ;

VARNAME: [a-zA-Z_]+[a-zA-Z_0-9]*;

// Syntax
NEWLINE: '\r'? '\n';
INDENT: '\t';
WS : [ \t\r\n]+ -> skip ;




// // Structure
// outer_block: 'def' VARNAME '():' NEWLINE inner_block; // Can add loop and other control statements later -- functions or control loops
// inner_block: INDENT expr;