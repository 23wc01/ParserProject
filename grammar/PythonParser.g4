grammar PythonParser;

program: (begin NEWLINE)* ;
begin: expr | simple_expr;


expr: var_assign | expr operator expr | vartype | VARNAME ;
simple_expr:  expr operator expr | vartype | VARNAME; // This catches op assignments so no invalid syntax


// Assignment
var_assign: VARNAME '=' expr ;
operator_assign: VARNAME op_equals simple_expr;

// Operations
operator: ('+'|'-'|'*'|'/'|'%');
op_equals: ('+='|'-='|'*='|'/='|'%=');


// Data types

vartype: INT | FLOAT| BOOL | STRING;
array: '[' vartype (','vartype)* ']' ;


INT:	[+-]?[0-9]+;
FLOAT: [+-]?[0-9]*'.'[0-9]+;
BOOL: 'True'|'False';
STRING: '"' [a-zA-Z_0-9]* '"' ;

VARNAME: [a-zA-Z_]+[a-zA-Z_0-9]*;

// Syntax
NEWLINE: [\r\n]+;
INDENT: '\t';
WS : [ \t]+ -> skip ;

//Still some issues with whitespace, esp with +=