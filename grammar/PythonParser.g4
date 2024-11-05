grammar PythonParser;


program:	'def main():'  expr  EOF;

endExpr: expr '\t'|'\n' ;

expr: assignmentExpr | assignmentExpr arithmeticExpr;

arithmeticExpr: expr ('+' | '-' | '*' | '/' | '%') expr   
    | VARNAME                                
    | INT ;                                      

assignmentExpr: VARNAME ( '=' | '+=' | '-=' | '*=' | '/=' ) arithmeticExpr ;

INT:	[+-]?[0-9]+;
FLOAT: [+-]?[0-9]*'.'[0-9]+;
VARNAME: [+-]?[a-zA-Z_]+[a-zA-Z_0-9]*;


WS:	[ \t\r\n]+ -> skip;


/*
This doesn't quite work, but I think the logic is at least close!
1:10 token recognition error at: ':'
5:6 token recognition error at: '+'
1:0 mismatched input 'def' expecting 'def' 
*/