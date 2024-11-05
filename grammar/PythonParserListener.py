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


    # Enter a parse tree produced by PythonParserParser#endExpr.
    def enterEndExpr(self, ctx:PythonParserParser.EndExprContext):
        pass

    # Exit a parse tree produced by PythonParserParser#endExpr.
    def exitEndExpr(self, ctx:PythonParserParser.EndExprContext):
        pass


    # Enter a parse tree produced by PythonParserParser#expr.
    def enterExpr(self, ctx:PythonParserParser.ExprContext):
        pass

    # Exit a parse tree produced by PythonParserParser#expr.
    def exitExpr(self, ctx:PythonParserParser.ExprContext):
        pass


    # Enter a parse tree produced by PythonParserParser#arithmeticExpr.
    def enterArithmeticExpr(self, ctx:PythonParserParser.ArithmeticExprContext):
        pass

    # Exit a parse tree produced by PythonParserParser#arithmeticExpr.
    def exitArithmeticExpr(self, ctx:PythonParserParser.ArithmeticExprContext):
        pass


    # Enter a parse tree produced by PythonParserParser#assignmentExpr.
    def enterAssignmentExpr(self, ctx:PythonParserParser.AssignmentExprContext):
        pass

    # Exit a parse tree produced by PythonParserParser#assignmentExpr.
    def exitAssignmentExpr(self, ctx:PythonParserParser.AssignmentExprContext):
        pass



del PythonParserParser