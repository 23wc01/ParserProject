# Generated from PythonParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .PythonParserParser import PythonParserParser
else:
    from PythonParserParser import PythonParserParser

# This class defines a complete listener for a parse tree produced by PythonParserParser.
class PythonParserListener(ParseTreeListener):

    # Enter a parse tree produced by PythonParserParser#program.
    def enterProgram(self, ctx:PythonParserParser.ProgramContext):
        pass

    # Exit a parse tree produced by PythonParserParser#program.
    def exitProgram(self, ctx:PythonParserParser.ProgramContext):
        pass


    # Enter a parse tree produced by PythonParserParser#endl.
    def enterEndl(self, ctx:PythonParserParser.EndlContext):
        pass

    # Exit a parse tree produced by PythonParserParser#endl.
    def exitEndl(self, ctx:PythonParserParser.EndlContext):
        pass


    # Enter a parse tree produced by PythonParserParser#begin.
    def enterBegin(self, ctx:PythonParserParser.BeginContext):
        pass

    # Exit a parse tree produced by PythonParserParser#begin.
    def exitBegin(self, ctx:PythonParserParser.BeginContext):
        pass


    # Enter a parse tree produced by PythonParserParser#var_assign.
    def enterVar_assign(self, ctx:PythonParserParser.Var_assignContext):
        pass

    # Exit a parse tree produced by PythonParserParser#var_assign.
    def exitVar_assign(self, ctx:PythonParserParser.Var_assignContext):
        pass


    # Enter a parse tree produced by PythonParserParser#operator_assign.
    def enterOperator_assign(self, ctx:PythonParserParser.Operator_assignContext):
        pass

    # Exit a parse tree produced by PythonParserParser#operator_assign.
    def exitOperator_assign(self, ctx:PythonParserParser.Operator_assignContext):
        pass


    # Enter a parse tree produced by PythonParserParser#conditional_statement.
    def enterConditional_statement(self, ctx:PythonParserParser.Conditional_statementContext):
        pass

    # Exit a parse tree produced by PythonParserParser#conditional_statement.
    def exitConditional_statement(self, ctx:PythonParserParser.Conditional_statementContext):
        pass


    # Enter a parse tree produced by PythonParserParser#while_statement.
    def enterWhile_statement(self, ctx:PythonParserParser.While_statementContext):
        pass

    # Exit a parse tree produced by PythonParserParser#while_statement.
    def exitWhile_statement(self, ctx:PythonParserParser.While_statementContext):
        pass


    # Enter a parse tree produced by PythonParserParser#for_statement.
    def enterFor_statement(self, ctx:PythonParserParser.For_statementContext):
        pass

    # Exit a parse tree produced by PythonParserParser#for_statement.
    def exitFor_statement(self, ctx:PythonParserParser.For_statementContext):
        pass


    # Enter a parse tree produced by PythonParserParser#condition.
    def enterCondition(self, ctx:PythonParserParser.ConditionContext):
        pass

    # Exit a parse tree produced by PythonParserParser#condition.
    def exitCondition(self, ctx:PythonParserParser.ConditionContext):
        pass


    # Enter a parse tree produced by PythonParserParser#block.
    def enterBlock(self, ctx:PythonParserParser.BlockContext):
        pass

    # Exit a parse tree produced by PythonParserParser#block.
    def exitBlock(self, ctx:PythonParserParser.BlockContext):
        pass


    # Enter a parse tree produced by PythonParserParser#expr.
    def enterExpr(self, ctx:PythonParserParser.ExprContext):
        pass

    # Exit a parse tree produced by PythonParserParser#expr.
    def exitExpr(self, ctx:PythonParserParser.ExprContext):
        pass


    # Enter a parse tree produced by PythonParserParser#unit.
    def enterUnit(self, ctx:PythonParserParser.UnitContext):
        pass

    # Exit a parse tree produced by PythonParserParser#unit.
    def exitUnit(self, ctx:PythonParserParser.UnitContext):
        pass


    # Enter a parse tree produced by PythonParserParser#operator.
    def enterOperator(self, ctx:PythonParserParser.OperatorContext):
        pass

    # Exit a parse tree produced by PythonParserParser#operator.
    def exitOperator(self, ctx:PythonParserParser.OperatorContext):
        pass


    # Enter a parse tree produced by PythonParserParser#op_equals.
    def enterOp_equals(self, ctx:PythonParserParser.Op_equalsContext):
        pass

    # Exit a parse tree produced by PythonParserParser#op_equals.
    def exitOp_equals(self, ctx:PythonParserParser.Op_equalsContext):
        pass


    # Enter a parse tree produced by PythonParserParser#op_compare.
    def enterOp_compare(self, ctx:PythonParserParser.Op_compareContext):
        pass

    # Exit a parse tree produced by PythonParserParser#op_compare.
    def exitOp_compare(self, ctx:PythonParserParser.Op_compareContext):
        pass


    # Enter a parse tree produced by PythonParserParser#vartype.
    def enterVartype(self, ctx:PythonParserParser.VartypeContext):
        pass

    # Exit a parse tree produced by PythonParserParser#vartype.
    def exitVartype(self, ctx:PythonParserParser.VartypeContext):
        pass


    # Enter a parse tree produced by PythonParserParser#array.
    def enterArray(self, ctx:PythonParserParser.ArrayContext):
        pass

    # Exit a parse tree produced by PythonParserParser#array.
    def exitArray(self, ctx:PythonParserParser.ArrayContext):
        pass



del PythonParserParser