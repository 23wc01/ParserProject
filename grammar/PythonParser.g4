grammar Sample;

program: (begin NEWLINE)* endl ;

endl: begin NEWLINE EOF | begin EOF | EOF;  // Handles last line of program

begin: var_assign
        | operator_assign
        | expr
        | conditional_statement
        ;
// Define conditionals
conditional: 'if' | 'elif';
ext_condition: 'and' | 'or';

// Assignment
var_assign: VARNAME '=' expr ;
operator_assign: VARNAME op_equals expr;

// Conditional
condition: expr op_compare expr; 
conditional_statement: conditional ('not')? condition (ext_condition condition)* ':'
        ((NEWLINE INDENT begin)+ | 'pass') (NEWLINE 'else:' ((NEWLINE INDENT begin)+ | 'pass'))?;

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
op_compare: (GT | LT | GTE | LTE | EQ);

// Data types
vartype: INT | FLOAT| BOOL | STRING | CHAR;
array: '[' vartype? (',' vartype)* ']' ;

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

GT: '>';
GTE: '>=';
LT: '<';
LTE: '<=';
EQ: '==';
NEQ: '!=';



// Syntax
NEWLINE: [\r\n]+;
INDENT: '\t';
WS : [ \t]+ -> skip ;