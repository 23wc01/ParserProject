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
        4,1,22,75,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,5,0,24,8,0,10,0,12,0,27,9,
        0,1,0,1,0,1,1,1,1,1,1,3,1,34,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,
        1,4,1,4,1,4,1,4,5,4,48,8,4,10,4,12,4,51,9,4,1,5,1,5,1,5,3,5,56,8,
        5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,5,9,68,8,9,10,9,12,9,71,
        9,9,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,3,1,0,2,6,1,0,
        16,19,1,0,10,14,71,0,25,1,0,0,0,2,33,1,0,0,0,4,35,1,0,0,0,6,39,1,
        0,0,0,8,43,1,0,0,0,10,55,1,0,0,0,12,57,1,0,0,0,14,59,1,0,0,0,16,
        61,1,0,0,0,18,63,1,0,0,0,20,21,3,2,1,0,21,22,5,20,0,0,22,24,1,0,
        0,0,23,20,1,0,0,0,24,27,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,28,
        1,0,0,0,27,25,1,0,0,0,28,29,5,0,0,1,29,1,1,0,0,0,30,34,3,4,2,0,31,
        34,3,6,3,0,32,34,3,8,4,0,33,30,1,0,0,0,33,31,1,0,0,0,33,32,1,0,0,
        0,34,3,1,0,0,0,35,36,5,15,0,0,36,37,5,1,0,0,37,38,3,8,4,0,38,5,1,
        0,0,0,39,40,5,15,0,0,40,41,3,14,7,0,41,42,3,8,4,0,42,7,1,0,0,0,43,
        49,3,10,5,0,44,45,3,12,6,0,45,46,3,10,5,0,46,48,1,0,0,0,47,44,1,
        0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,9,1,0,0,0,51,
        49,1,0,0,0,52,56,3,16,8,0,53,56,5,15,0,0,54,56,3,18,9,0,55,52,1,
        0,0,0,55,53,1,0,0,0,55,54,1,0,0,0,56,11,1,0,0,0,57,58,7,0,0,0,58,
        13,1,0,0,0,59,60,7,1,0,0,60,15,1,0,0,0,61,62,7,2,0,0,62,17,1,0,0,
        0,63,64,5,7,0,0,64,69,3,16,8,0,65,66,5,8,0,0,66,68,3,16,8,0,67,65,
        1,0,0,0,68,71,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,72,1,0,0,0,
        71,69,1,0,0,0,72,73,5,9,0,0,73,19,1,0,0,0,5,25,33,49,55,69
    ]

class PythonParserParser ( Parser ):

    grammarFileName = "PythonParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'['", "','", "']'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'+='", "'-='", 
                     "'*='", "'/='", "<INVALID>", "'\\t'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INT", "FLOAT", "BOOL", 
                      "STRING", "CHAR", "VARNAME", "PLUSEQ", "MINUSEQ", 
                      "MULTEQ", "DIVEQ", "NEWLINE", "INDENT", "WS" ]

    RULE_program = 0
    RULE_begin = 1
    RULE_var_assign = 2
    RULE_operator_assign = 3
    RULE_expr = 4
    RULE_unit = 5
    RULE_operator = 6
    RULE_op_equals = 7
    RULE_vartype = 8
    RULE_array = 9

    ruleNames =  [ "program", "begin", "var_assign", "operator_assign", 
                   "expr", "unit", "operator", "op_equals", "vartype", "array" ]

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
    INT=10
    FLOAT=11
    BOOL=12
    STRING=13
    CHAR=14
    VARNAME=15
    PLUSEQ=16
    MINUSEQ=17
    MULTEQ=18
    DIVEQ=19
    NEWLINE=20
    INDENT=21
    WS=22

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

        def EOF(self):
            return self.getToken(PythonParserParser.EOF, 0)

        def begin(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.BeginContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.BeginContext,i)


        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(PythonParserParser.NEWLINE)
            else:
                return self.getToken(PythonParserParser.NEWLINE, i)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 64640) != 0):
                self.state = 20
                self.begin()
                self.state = 21
                self.match(PythonParserParser.NEWLINE)
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
            self.match(PythonParserParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BeginContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_assign(self):
            return self.getTypedRuleContext(PythonParserParser.Var_assignContext,0)


        def operator_assign(self):
            return self.getTypedRuleContext(PythonParserParser.Operator_assignContext,0)


        def expr(self):
            return self.getTypedRuleContext(PythonParserParser.ExprContext,0)


        def getRuleIndex(self):
            return PythonParserParser.RULE_begin

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBegin" ):
                listener.enterBegin(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBegin" ):
                listener.exitBegin(self)




    def begin(self):

        localctx = PythonParserParser.BeginContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_begin)
        try:
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 30
                self.var_assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 31
                self.operator_assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self):
            return self.getToken(PythonParserParser.VARNAME, 0)

        def expr(self):
            return self.getTypedRuleContext(PythonParserParser.ExprContext,0)


        def getRuleIndex(self):
            return PythonParserParser.RULE_var_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_assign" ):
                listener.enterVar_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_assign" ):
                listener.exitVar_assign(self)




    def var_assign(self):

        localctx = PythonParserParser.Var_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(PythonParserParser.VARNAME)
            self.state = 36
            self.match(PythonParserParser.T__0)
            self.state = 37
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Operator_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARNAME(self):
            return self.getToken(PythonParserParser.VARNAME, 0)

        def op_equals(self):
            return self.getTypedRuleContext(PythonParserParser.Op_equalsContext,0)


        def expr(self):
            return self.getTypedRuleContext(PythonParserParser.ExprContext,0)


        def getRuleIndex(self):
            return PythonParserParser.RULE_operator_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator_assign" ):
                listener.enterOperator_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator_assign" ):
                listener.exitOperator_assign(self)




    def operator_assign(self):

        localctx = PythonParserParser.Operator_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_operator_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(PythonParserParser.VARNAME)
            self.state = 40
            self.op_equals()
            self.state = 41
            self.expr()
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

        def unit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.UnitContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.UnitContext,i)


        def operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.OperatorContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.OperatorContext,i)


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
        self.enterRule(localctx, 8, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.unit()
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 124) != 0):
                self.state = 44
                self.operator()
                self.state = 45
                self.unit()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self):
            return self.getTypedRuleContext(PythonParserParser.VartypeContext,0)


        def VARNAME(self):
            return self.getToken(PythonParserParser.VARNAME, 0)

        def array(self):
            return self.getTypedRuleContext(PythonParserParser.ArrayContext,0)


        def getRuleIndex(self):
            return PythonParserParser.RULE_unit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnit" ):
                listener.enterUnit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnit" ):
                listener.exitUnit(self)




    def unit(self):

        localctx = PythonParserParser.UnitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_unit)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 12, 13, 14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.vartype()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.match(PythonParserParser.VARNAME)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.array()
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


    class OperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return PythonParserParser.RULE_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperator" ):
                listener.enterOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperator" ):
                listener.exitOperator(self)




    def operator(self):

        localctx = PythonParserParser.OperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 124) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Op_equalsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUSEQ(self):
            return self.getToken(PythonParserParser.PLUSEQ, 0)

        def MINUSEQ(self):
            return self.getToken(PythonParserParser.MINUSEQ, 0)

        def MULTEQ(self):
            return self.getToken(PythonParserParser.MULTEQ, 0)

        def DIVEQ(self):
            return self.getToken(PythonParserParser.DIVEQ, 0)

        def getRuleIndex(self):
            return PythonParserParser.RULE_op_equals

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOp_equals" ):
                listener.enterOp_equals(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOp_equals" ):
                listener.exitOp_equals(self)




    def op_equals(self):

        localctx = PythonParserParser.Op_equalsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_op_equals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 983040) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VartypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(PythonParserParser.INT, 0)

        def FLOAT(self):
            return self.getToken(PythonParserParser.FLOAT, 0)

        def BOOL(self):
            return self.getToken(PythonParserParser.BOOL, 0)

        def STRING(self):
            return self.getToken(PythonParserParser.STRING, 0)

        def CHAR(self):
            return self.getToken(PythonParserParser.CHAR, 0)

        def getRuleIndex(self):
            return PythonParserParser.RULE_vartype

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVartype" ):
                listener.enterVartype(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVartype" ):
                listener.exitVartype(self)




    def vartype(self):

        localctx = PythonParserParser.VartypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_vartype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31744) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def vartype(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.VartypeContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.VartypeContext,i)


        def getRuleIndex(self):
            return PythonParserParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = PythonParserParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(PythonParserParser.T__6)
            self.state = 64
            self.vartype()
            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 65
                self.match(PythonParserParser.T__7)
                self.state = 66
                self.vartype()
                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
            self.match(PythonParserParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





