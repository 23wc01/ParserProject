grammar PythonParser;

program: (begin NEWLINE)* EOF;
// begin: expr | simple_expr;

begin: var_assign
        | operator_assign
        | expr
        ;

// Assignment
var_assign: VARNAME '=' expr ;
operator_assign: VARNAME op_equals expr;

// Expressions
expr: unit (operator unit)* ;
// expr: var_assign | expr operator expr | vartype | VARNAME ;
// simple_expr:  expr operator expr | vartype | VARNAME; // This catches op assignments so no invalid syntax

// These are the basic components that can't be simplified
unit: vartype
    | VARNAME
    | array
    ;


// Operations
operator: ('+'|'-'|'*'|'/'|'%');
op_equals: ('+='|'-='|'*='|'/='|'%=');


// Data types
vartype: INT | FLOAT| BOOL | STRING | CHAR;
array: '[' vartype (',' vartype)* ']' ;

// Primitives
INT:	[+-]?[0-9]+;
FLOAT: [+-]?[0-9]*'.'[0-9]+;
BOOL: 'True' | 'False';
STRING: '"' .*? '"' ;
CHAR: '\'' . '\'' ;
VARNAME: [a-zA-Z_]+[a-zA-Z_0-9]*;

// Syntax
NEWLINE: [\r\n]+;
INDENT: '\t';
WS : [ \t]+ -> skip ;

//Still some issues with whitespace, esp with +=