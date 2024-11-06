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
        4,1,22,81,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,0,5,0,24,8,0,10,0,12,0,27,9,
        0,1,1,1,1,3,1,31,8,1,1,2,1,2,1,2,1,2,3,2,37,8,2,1,2,1,2,1,2,1,2,
        5,2,43,8,2,10,2,12,2,46,9,2,1,3,1,3,1,3,1,3,1,3,1,3,3,3,54,8,3,1,
        4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,
        9,1,9,5,9,74,8,9,10,9,12,9,77,9,9,1,9,1,9,1,9,0,1,4,10,0,2,4,6,8,
        10,12,14,16,18,0,3,1,0,2,6,1,0,7,11,1,0,15,18,78,0,25,1,0,0,0,2,
        30,1,0,0,0,4,36,1,0,0,0,6,53,1,0,0,0,8,55,1,0,0,0,10,59,1,0,0,0,
        12,63,1,0,0,0,14,65,1,0,0,0,16,67,1,0,0,0,18,69,1,0,0,0,20,21,3,
        2,1,0,21,22,5,20,0,0,22,24,1,0,0,0,23,20,1,0,0,0,24,27,1,0,0,0,25,
        23,1,0,0,0,25,26,1,0,0,0,26,1,1,0,0,0,27,25,1,0,0,0,28,31,3,4,2,
        0,29,31,3,6,3,0,30,28,1,0,0,0,30,29,1,0,0,0,31,3,1,0,0,0,32,33,6,
        2,-1,0,33,37,3,8,4,0,34,37,3,16,8,0,35,37,5,19,0,0,36,32,1,0,0,0,
        36,34,1,0,0,0,36,35,1,0,0,0,37,44,1,0,0,0,38,39,10,3,0,0,39,40,3,
        12,6,0,40,41,3,4,2,4,41,43,1,0,0,0,42,38,1,0,0,0,43,46,1,0,0,0,44,
        42,1,0,0,0,44,45,1,0,0,0,45,5,1,0,0,0,46,44,1,0,0,0,47,48,3,4,2,
        0,48,49,3,12,6,0,49,50,3,4,2,0,50,54,1,0,0,0,51,54,3,16,8,0,52,54,
        5,19,0,0,53,47,1,0,0,0,53,51,1,0,0,0,53,52,1,0,0,0,54,7,1,0,0,0,
        55,56,5,19,0,0,56,57,5,1,0,0,57,58,3,4,2,0,58,9,1,0,0,0,59,60,5,
        19,0,0,60,61,3,14,7,0,61,62,3,6,3,0,62,11,1,0,0,0,63,64,7,0,0,0,
        64,13,1,0,0,0,65,66,7,1,0,0,66,15,1,0,0,0,67,68,7,2,0,0,68,17,1,
        0,0,0,69,70,5,12,0,0,70,75,3,16,8,0,71,72,5,13,0,0,72,74,3,16,8,
        0,73,71,1,0,0,0,74,77,1,0,0,0,75,73,1,0,0,0,75,76,1,0,0,0,76,78,
        1,0,0,0,77,75,1,0,0,0,78,79,5,14,0,0,79,19,1,0,0,0,6,25,30,36,44,
        53,75
    ]

class PythonParserParser ( Parser ):

    grammarFileName = "PythonParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'+='", "'-='", "'*='", "'/='", "'%='", "'['", "','", 
                     "']'", "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'\\t'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "INT", "FLOAT", 
                      "BOOL", "STRING", "VARNAME", "NEWLINE", "INDENT", 
                      "WS" ]

    RULE_program = 0
    RULE_begin = 1
    RULE_expr = 2
    RULE_simple_expr = 3
    RULE_var_assign = 4
    RULE_operator_assign = 5
    RULE_operator = 6
    RULE_op_equals = 7
    RULE_vartype = 8
    RULE_array = 9

    ruleNames =  [ "program", "begin", "expr", "simple_expr", "var_assign", 
                   "operator_assign", "operator", "op_equals", "vartype", 
                   "array" ]

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
    T__13=14
    INT=15
    FLOAT=16
    BOOL=17
    STRING=18
    VARNAME=19
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1015808) != 0):
                self.state = 20
                self.begin()
                self.state = 21
                self.match(PythonParserParser.NEWLINE)
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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

        def expr(self):
            return self.getTypedRuleContext(PythonParserParser.ExprContext,0)


        def simple_expr(self):
            return self.getTypedRuleContext(PythonParserParser.Simple_exprContext,0)


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
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.simple_expr()
                pass


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

        def var_assign(self):
            return self.getTypedRuleContext(PythonParserParser.Var_assignContext,0)


        def vartype(self):
            return self.getTypedRuleContext(PythonParserParser.VartypeContext,0)


        def VARNAME(self):
            return self.getToken(PythonParserParser.VARNAME, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.ExprContext,i)


        def operator(self):
            return self.getTypedRuleContext(PythonParserParser.OperatorContext,0)


        def getRuleIndex(self):
            return PythonParserParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PythonParserParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 33
                self.var_assign()
                pass

            elif la_ == 2:
                self.state = 34
                self.vartype()
                pass

            elif la_ == 3:
                self.state = 35
                self.match(PythonParserParser.VARNAME)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 44
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PythonParserParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 38
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 39
                    self.operator()
                    self.state = 40
                    self.expr(4) 
                self.state = 46
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Simple_exprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PythonParserParser.ExprContext)
            else:
                return self.getTypedRuleContext(PythonParserParser.ExprContext,i)


        def operator(self):
            return self.getTypedRuleContext(PythonParserParser.OperatorContext,0)


        def vartype(self):
            return self.getTypedRuleContext(PythonParserParser.VartypeContext,0)


        def VARNAME(self):
            return self.getToken(PythonParserParser.VARNAME, 0)

        def getRuleIndex(self):
            return PythonParserParser.RULE_simple_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSimple_expr" ):
                listener.enterSimple_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSimple_expr" ):
                listener.exitSimple_expr(self)




    def simple_expr(self):

        localctx = PythonParserParser.Simple_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_simple_expr)
        try:
            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.expr(0)
                self.state = 48
                self.operator()
                self.state = 49
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.vartype()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.match(PythonParserParser.VARNAME)
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
        self.enterRule(localctx, 8, self.RULE_var_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.match(PythonParserParser.VARNAME)
            self.state = 56
            self.match(PythonParserParser.T__0)
            self.state = 57
            self.expr(0)
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


        def simple_expr(self):
            return self.getTypedRuleContext(PythonParserParser.Simple_exprContext,0)


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
        self.enterRule(localctx, 10, self.RULE_operator_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(PythonParserParser.VARNAME)
            self.state = 60
            self.op_equals()
            self.state = 61
            self.simple_expr()
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
            self.state = 63
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
            self.state = 65
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3968) != 0)):
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
            self.state = 67
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 491520) != 0)):
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
            self.state = 69
            self.match(PythonParserParser.T__11)
            self.state = 70
            self.vartype()
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==13:
                self.state = 71
                self.match(PythonParserParser.T__12)
                self.state = 72
                self.vartype()
                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 78
            self.match(PythonParserParser.T__13)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         




