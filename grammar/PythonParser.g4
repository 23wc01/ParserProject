grammar PythonParser; // Change to "grammar Sample;" if pasting into lab.antlr.org


program: (NEWLINE | begin NEWLINE)* endl ;

endl: begin NEWLINE EOF | begin EOF | EOF;  // Handles last line of program

begin: var_assign
        | operator_assign
        | expr
        | conditional_statement
        | outer
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
INT:    [+-]?[0-9]+;
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
INDENT: '\t'+;
WS : [ ]+ -> skip ;

// Comments
COMMENT: '#' ~[\r\n]* -> skip;
BLOCK_COMMENT: ('"""' .*? '"""' | '\'' '\'' '\'' .*? '\'' '\'' '\'') -> skip;


// Assignment
var_assign: VARNAME '=' expr ;
operator_assign: VARNAME op_equals expr;

// While statement
while_statement: WHILE condition ':'
    (NEWLINE inner)*;

// For statement
for_statement: FOR VARNAME IN expr ':' 
    (NEWLINE inner)*;

outer: for_statement | while_statement | inner;

// Conditional statement
conditional_statement: IF condition ':'
    (NEWLINE inner)*
    (INDENT* ELIF condition ':' (NEWLINE inner)*)*
    (INDENT* ELSE ':' ((NEWLINE inner)*))?;

condition: '('? (UNARY_LOGIC)? expr (op_compare (UNARY_LOGIC)? expr)? ')'? (BINARY_LOGIC condition)*; 



// Expressions
expr: unit | expr operator expr |func;


// These are the basic components that can't be simplified
unit: vartype
    | VARNAME
    | array
    ;


// Block statements

inner: INDENT+ begin NEWLINE* ;



// Operations
operator: ('+'|'-'|'*'|'/'|'%');
op_equals: (PLUSEQ | MINUSEQ | MULTEQ | DIVEQ);
op_compare: (GT | LT | GTE | LTE | EQ | NEQ);

// Data types
vartype: INT | FLOAT| BOOL | STRING | CHAR;
array: '[' vartype? (',' vartype)* ']' ;

// Function calls
func: VARNAME '(' (vartype ',')* (vartype)? ')';
