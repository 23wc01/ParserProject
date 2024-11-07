grammar PythonParser;

program: (begin NEWLINE)* EOF;


begin: var_assign
        | operator_assign
        | expr
        ;

// Assignment
var_assign: VARNAME '=' expr ;
operator_assign: VARNAME op_equals expr;

// Expressions
expr: unit (operator unit)* ;


// These are the basic components that can't be simplified
unit: vartype
    | VARNAME
    | array
    ;


// Operations
operator: ('+'|'-'|'*'|'/'|'%');
op_equals: (PLUSEQ | MINUSEQ | MULTEQ | DIVEQ);


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

//Define multi-character tokens
PLUSEQ: '+=';
MINUSEQ: '-=';
MULTEQ: '*=';
DIVEQ: '/=';

// Syntax
NEWLINE: [\r\n]+;
INDENT: '\t';
WS : [ \t]+ -> skip ;

