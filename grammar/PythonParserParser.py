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
        4,1,22,89,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,1,0,1,0,5,0,26,8,0,10,0,
        12,0,29,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,41,8,1,1,
        2,1,2,1,2,3,2,46,8,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,5,1,5,1,5,
        1,5,5,5,60,8,5,10,5,12,5,63,9,5,1,6,1,6,1,6,3,6,68,8,6,1,7,1,7,1,
        8,1,8,1,9,1,9,1,10,1,10,3,10,78,8,10,1,10,1,10,5,10,82,8,10,10,10,
        12,10,85,9,10,1,10,1,10,1,10,0,0,11,0,2,4,6,8,10,12,14,16,18,20,
        0,3,1,0,2,6,1,0,16,19,1,0,10,14,87,0,27,1,0,0,0,2,40,1,0,0,0,4,45,
        1,0,0,0,6,47,1,0,0,0,8,51,1,0,0,0,10,55,1,0,0,0,12,67,1,0,0,0,14,
        69,1,0,0,0,16,71,1,0,0,0,18,73,1,0,0,0,20,75,1,0,0,0,22,23,3,4,2,
        0,23,24,5,20,0,0,24,26,1,0,0,0,25,22,1,0,0,0,26,29,1,0,0,0,27,25,
        1,0,0,0,27,28,1,0,0,0,28,30,1,0,0,0,29,27,1,0,0,0,30,31,3,2,1,0,
        31,1,1,0,0,0,32,33,3,4,2,0,33,34,5,20,0,0,34,35,5,0,0,1,35,41,1,
        0,0,0,36,37,3,4,2,0,37,38,5,0,0,1,38,41,1,0,0,0,39,41,5,0,0,1,40,
        32,1,0,0,0,40,36,1,0,0,0,40,39,1,0,0,0,41,3,1,0,0,0,42,46,3,6,3,
        0,43,46,3,8,4,0,44,46,3,10,5,0,45,42,1,0,0,0,45,43,1,0,0,0,45,44,
        1,0,0,0,46,5,1,0,0,0,47,48,5,15,0,0,48,49,5,1,0,0,49,50,3,10,5,0,
        50,7,1,0,0,0,51,52,5,15,0,0,52,53,3,16,8,0,53,54,3,10,5,0,54,9,1,
        0,0,0,55,61,3,12,6,0,56,57,3,14,7,0,57,58,3,12,6,0,58,60,1,0,0,0,
        59,56,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,11,1,
        0,0,0,63,61,1,0,0,0,64,68,3,18,9,0,65,68,5,15,0,0,66,68,3,20,10,
        0,67,64,1,0,0,0,67,65,1,0,0,0,67,66,1,0,0,0,68,13,1,0,0,0,69,70,
        7,0,0,0,70,15,1,0,0,0,71,72,7,1,0,0,72,17,1,0,0,0,73,74,7,2,0,0,
        74,19,1,0,0,0,75,77,5,7,0,0,76,78,3,18,9,0,77,76,1,0,0,0,77,78,1,
        0,0,0,78,83,1,0,0,0,79,80,5,8,0,0,80,82,3,18,9,0,81,79,1,0,0,0,82,
        85,1,0,0,0,83,81,1,0,0,0,83,84,1,0,0,0,84,86,1,0,0,0,85,83,1,0,0,
        0,86,87,5,9,0,0,87,21,1,0,0,0,7,27,40,45,61,67,77,83
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
    RULE_endl = 1
    RULE_begin = 2
    RULE_var_assign = 3
    RULE_operator_assign = 4
    RULE_expr = 5
    RULE_unit = 6
    RULE_operator = 7
    RULE_op_equals = 8
    RULE_vartype = 9
    RULE_array = 10

    ruleNames =  [ "program", "endl", "begin", "var_assign", "operator_assign", 
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

        def endl(self):
            return self.getTypedRuleContext(PythonParserParser.EndlContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 22
                    self.begin()
                    self.state = 23
                    self.match(PythonParserParser.NEWLINE) 
                self.state = 29
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 30
            self.endl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EndlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def begin(self):
            return self.getTypedRuleContext(PythonParserParser.BeginContext,0)


        def NEWLINE(self):
            return self.getToken(PythonParserParser.NEWLINE, 0)

        def EOF(self):
            return self.getToken(PythonParserParser.EOF, 0)

        def getRuleIndex(self):
            return PythonParserParser.RULE_endl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEndl" ):
                listener.enterEndl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEndl" ):
                listener.exitEndl(self)




    def endl(self):

        localctx = PythonParserParser.EndlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_endl)
        try:
            self.state = 40
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.begin()
                self.state = 33
                self.match(PythonParserParser.NEWLINE)
                self.state = 34
                self.match(PythonParserParser.EOF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.begin()
                self.state = 37
                self.match(PythonParserParser.EOF)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 39
                self.match(PythonParserParser.EOF)
                pass


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
        self.enterRule(localctx, 4, self.RULE_begin)
        try:
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.var_assign()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.operator_assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 44
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
        self.enterRule(localctx, 6, self.RULE_var_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(PythonParserParser.VARNAME)
            self.state = 48
            self.match(PythonParserParser.T__0)
            self.state = 49
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
        self.enterRule(localctx, 8, self.RULE_operator_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(PythonParserParser.VARNAME)
            self.state = 52
            self.op_equals()
            self.state = 53
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
        self.enterRule(localctx, 10, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.unit()
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 124) != 0):
                self.state = 56
                self.operator()
                self.state = 57
                self.unit()
                self.state = 63
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
        self.enterRule(localctx, 12, self.RULE_unit)
        try:
            self.state = 67
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 12, 13, 14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.vartype()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.match(PythonParserParser.VARNAME)
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 3)
                self.state = 66
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
        self.enterRule(localctx, 14, self.RULE_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
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
        self.enterRule(localctx, 16, self.RULE_op_equals)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
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
        self.enterRule(localctx, 18, self.RULE_vartype)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
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
        self.enterRule(localctx, 20, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(PythonParserParser.T__6)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31744) != 0):
                self.state = 76
                self.vartype()


            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==8:
                self.state = 79
                self.match(PythonParserParser.T__7)
                self.state = 80
                self.vartype()
                self.state = 85
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 86
            self.match(PythonParserParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





