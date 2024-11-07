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
	 * Enter a parse tree produced by {@link PythonParserParser#begin}.
	 * @param ctx the parse tree
	 */
	void enterBegin(PythonParserParser.BeginContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParserParser#begin}.
	 * @param ctx the parse tree
	 */
	void exitBegin(PythonParserParser.BeginContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParserParser#var_assign}.
	 * @param ctx the parse tree
	 */
	void enterVar_assign(PythonParserParser.Var_assignContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParserParser#var_assign}.
	 * @param ctx the parse tree
	 */
	void exitVar_assign(PythonParserParser.Var_assignContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParserParser#operator_assign}.
	 * @param ctx the parse tree
	 */
	void enterOperator_assign(PythonParserParser.Operator_assignContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParserParser#operator_assign}.
	 * @param ctx the parse tree
	 */
	void exitOperator_assign(PythonParserParser.Operator_assignContext ctx);
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
	 * Enter a parse tree produced by {@link PythonParserParser#unit}.
	 * @param ctx the parse tree
	 */
	void enterUnit(PythonParserParser.UnitContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParserParser#unit}.
	 * @param ctx the parse tree
	 */
	void exitUnit(PythonParserParser.UnitContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParserParser#operator}.
	 * @param ctx the parse tree
	 */
	void enterOperator(PythonParserParser.OperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParserParser#operator}.
	 * @param ctx the parse tree
	 */
	void exitOperator(PythonParserParser.OperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParserParser#op_equals}.
	 * @param ctx the parse tree
	 */
	void enterOp_equals(PythonParserParser.Op_equalsContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParserParser#op_equals}.
	 * @param ctx the parse tree
	 */
	void exitOp_equals(PythonParserParser.Op_equalsContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParserParser#vartype}.
	 * @param ctx the parse tree
	 */
	void enterVartype(PythonParserParser.VartypeContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParserParser#vartype}.
	 * @param ctx the parse tree
	 */
	void exitVartype(PythonParserParser.VartypeContext ctx);
	/**
	 * Enter a parse tree produced by {@link PythonParserParser#array}.
	 * @param ctx the parse tree
	 */
	void enterArray(PythonParserParser.ArrayContext ctx);
	/**
	 * Exit a parse tree produced by {@link PythonParserParser#array}.
	 * @param ctx the parse tree
	 */
	void exitArray(PythonParserParser.ArrayContext ctx);
}