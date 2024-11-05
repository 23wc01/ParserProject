// Generated from PythonParser.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link PythonParserParser}.
 */
public interface PythonParserListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link PythonParserParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(PythonParserParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParserParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(PythonParserParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParserParser#endExpr}.
	 * @param ctx the parse tree
	 */
	void enterEndExpr(PythonParserParser.EndExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParserParser#endExpr}.
	 * @param ctx the parse tree
	 */
	void exitEndExpr(PythonParserParser.EndExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParserParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExpr(PythonParserParser.ExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParserParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExpr(PythonParserParser.ExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParserParser#arithmeticExpr}.
	 * @param ctx the parse tree
	 */
	void enterArithmeticExpr(PythonParserParser.ArithmeticExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParserParser#arithmeticExpr}.
	 * @param ctx the parse tree
	 */
	void exitArithmeticExpr(PythonParserParser.ArithmeticExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParserParser#assignmentExpr}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentExpr(PythonParserParser.AssignmentExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParserParser#assignmentExpr}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentExpr(PythonParserParser.AssignmentExprContext ctx);
}