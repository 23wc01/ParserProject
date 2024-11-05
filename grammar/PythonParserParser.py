# Generated from PythonParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,39,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,
        0,1,1,1,1,1,1,1,1,3,1,19,8,1,1,2,1,2,1,2,1,2,3,2,25,8,2,1,3,1,3,
        1,3,1,3,1,3,1,3,3,3,33,8,3,1,4,1,4,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,
        2,1,0,4,8,1,0,9,13,37,0,10,1,0,0,0,2,18,1,0,0,0,4,24,1,0,0,0,6,32,
        1,0,0,0,8,34,1,0,0,0,10,11,5,1,0,0,11,12,3,4,2,0,12,13,5,0,0,1,13,
        1,1,0,0,0,14,15,3,4,2,0,15,16,5,2,0,0,16,19,1,0,0,0,17,19,5,3,0,
        0,18,14,1,0,0,0,18,17,1,0,0,0,19,3,1,0,0,0,20,25,3,8,4,0,21,22,3,
        8,4,0,22,23,3,6,3,0,23,25,1,0,0,0,24,20,1,0,0,0,24,21,1,0,0,0,25,
        5,1,0,0,0,26,27,3,4,2,0,27,28,7,0,0,0,28,29,3,4,2,0,29,33,1,0,0,
        0,30,33,5,16,0,0,31,33,5,14,0,0,32,26,1,0,0,0,32,30,1,0,0,0,32,31,
        1,0,0,0,33,7,1,0,0,0,34,35,5,16,0,0,35,36,7,1,0,0,36,37,3,6,3,0,
        37,9,1,0,0,0,3,18,24,32
    ]

class PythonParserParser ( Parser ):

    grammarFileName = "PythonParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'def main():'", "'\\t'", "'\\n'", "'+'", 
                     "'-'", "'*'", "'/'", "'%'", "'='", "'+='", "'-='", 
                     "'*='", "'/='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INT", "FLOAT", "VARNAME", 
                      "WS" ]

    RULE_program = 0
    RULE_endExpr = 1
    RULE_expr = 2
    RULE_arithmeticExpr = 3
    RULE_assignmentExpr = 4

    ruleNames =  [ "program", "endExpr", "expr", "arithmeticExpr", "assignmentExpr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    INT=14
    FLOAT=15
    VARNAME=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PythonParserParser.ExprContext,0)


        def EOF(self):
            return self.getToken(PythonParserParser.EOF, 0)

        def getRuleIndex(self):
            return PythonParserParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = PythonParserParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            self.match(PythonParserParser.T__0)
            self.state = 11
            self.expr()
            self.state = 12
            self.match(PythonParserParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PythonParserParser.ExprContext,0)


        def getRuleIndex(self):
            return PythonParserParser.RULE_endExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndExpr" ):
                listener.enterEndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndExpr" ):
                listener.exitEndExpr(self)




    def endExpr(self):

        localctx = PythonParserParser.EndExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_endExpr)
        try:
            self.state = 18
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.expr()
                self.state = 15
                self.match(PythonParserParser.T__1)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.match(PythonParserParser.T__2)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentExpr(self):
            return self.getTypedRuleContext(PythonParserParser.AssignmentExprContext,0)


        def arithmeticExpr(self):
            return self.getTypedRuleContext(PythonParserParser.ArithmeticExprContext,0)


        def getRuleIndex(self):
            return PythonParserParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = PythonParserParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expr)
        try:
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.assignmentExpr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 21
                self.assignmentExpr()
                self.state = 22
                self.arithmeticExpr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArithmeticExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.ExprContext,i)


        def VARNAME(self):
            return self.getToken(PythonParserParser.VARNAME, 0)

        def INT(self):
            return self.getToken(PythonParserParser.INT, 0)

        def getRuleIndex(self):
            return PythonParserParser.RULE_arithmeticExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmeticExpr" ):
                listener.enterArithmeticExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmeticExpr" ):
                listener.exitArithmeticExpr(self)




    def arithmeticExpr(self):

        localctx = PythonParserParser.ArithmeticExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arithmeticExpr)
        self._la = 0 # Token type
        try:
            self.state = 32
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 26
                self.expr()
                self.state = 27
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 496) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 28
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.match(PythonParserParser.VARNAME)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 31
                self.match(PythonParserParser.INT)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self):
            return self.getToken(PythonParserParser.VARNAME, 0)

        def arithmeticExpr(self):
            return self.getTypedRuleContext(PythonParserParser.ArithmeticExprContext,0)


        def getRuleIndex(self):
            return PythonParserParser.RULE_assignmentExpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentExpr" ):
                listener.enterAssignmentExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentExpr" ):
                listener.exitAssignmentExpr(self)




    def assignmentExpr(self):

        localctx = PythonParserParser.AssignmentExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_assignmentExpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            self.match(PythonParserParser.VARNAME)
            self.state = 35
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15872) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 36
            self.arithmeticExpr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





