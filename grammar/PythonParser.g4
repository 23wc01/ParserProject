grammar PythonParser;

program: (NEWLINE | begin NEWLINE)* endl ;

endl: begin NEWLINE EOF | begin EOF | EOF;  // Handles last line of program

begin: var_assign
        | operator_assign
        | expr
        | conditional_statement
        | while_statement
        | for_statement
        ;

// Define conditionals
IF: 'if';
ELIF: 'elif'; 
ELSE: 'else';

// Boolean logic operators
BINARY_LOGIC: 'and' | 'or';
UNARY_LOGIC: 'not';

// Loop Structures
WHILE: 'while';
FOR: 'for';
IN: 'in';

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
WS : [ ]+ -> skip ;

// Comments
COMMENT: '#' ~[\r\n]* -> skip;
BLOCK_COMMENT: ('"""' .*? '"""' | '\'' '\'' '\'' .*? '\'' '\'' '\'') -> skip;


// Assignment
var_assign: VARNAME '=' expr ;
operator_assign: VARNAME op_equals expr;

// Conditional statement
conditional_statement: IF condition ':' (expr | NEWLINE (block)+)
    (NEWLINE ELIF condition ':' (NEWLINE)? (block)+)*
    (NEWLINE ELSE ':' (NEWLINE)? (block)+)?;
    (NEWLINE (INDENT)* ELIF condition ':' (NEWLINE)? (block)+)*
    (NEWLINE (INDENT)* ELSE ':' (NEWLINE)? (block)+)?;

// While statement
while_statement: WHILE condition ':'
    NEWLINE* block;
    (NEWLINE block*)*;

// For statement
for_statement: FOR VARNAME IN expr ':' 
    NEWLINE* block;


block: INDENT+ (begin)? NEWLINE*;


// Expressions
expr: unit | expr operator expr | func;


// These are the basic components that can't be simplified
unit: vartype
    | VARNAME
    | array
    ;


// Operations
operator: ('+'|'-'|'*'|'/'|'%');
op_equals: (PLUSEQ | MINUSEQ | MULTEQ | DIVEQ);
op_compare: (GT | LT | GTE | LTE | EQ | NEQ);

// Data types
vartype: INT | FLOAT| BOOL | STRING | CHAR;
array: '[' vartype? (',' vartype)* ']' ;

// Function calls
func: VARNAME '(' (vartype ',')* (vartype)? ')';

