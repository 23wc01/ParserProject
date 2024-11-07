// Generated from PythonParser.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class PythonParserLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		INT=10, FLOAT=11, BOOL=12, STRING=13, CHAR=14, VARNAME=15, PLUSEQ=16, 
		MINUSEQ=17, MULTEQ=18, DIVEQ=19, NEWLINE=20, INDENT=21, WS=22;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"INT", "FLOAT", "BOOL", "STRING", "CHAR", "VARNAME", "PLUSEQ", "MINUSEQ", 
			"MULTEQ", "DIVEQ", "NEWLINE", "INDENT", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'['", "','", "']'", 
			null, null, null, null, null, null, "'+='", "'-='", "'*='", "'/='", null, 
			"'\\t'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, "INT", "FLOAT", 
			"BOOL", "STRING", "CHAR", "VARNAME", "PLUSEQ", "MINUSEQ", "MULTEQ", "DIVEQ", 
			"NEWLINE", "INDENT", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public PythonParserLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "PythonParser.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0016\u0093\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007"+
		"\u0001\b\u0001\b\u0001\t\u0003\tA\b\t\u0001\t\u0004\tD\b\t\u000b\t\f\t"+
		"E\u0001\n\u0003\nI\b\n\u0001\n\u0005\nL\b\n\n\n\f\nO\t\n\u0001\n\u0001"+
		"\n\u0004\nS\b\n\u000b\n\f\nT\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0003"+
		"\u000b`\b\u000b\u0001\f\u0001\f\u0005\fd\b\f\n\f\f\fg\t\f\u0001\f\u0001"+
		"\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\u000e\u0004\u000ep\b\u000e\u000b"+
		"\u000e\f\u000eq\u0001\u000e\u0005\u000eu\b\u000e\n\u000e\f\u000ex\t\u000e"+
		"\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012"+
		"\u0001\u0013\u0004\u0013\u0087\b\u0013\u000b\u0013\f\u0013\u0088\u0001"+
		"\u0014\u0001\u0014\u0001\u0015\u0004\u0015\u008e\b\u0015\u000b\u0015\f"+
		"\u0015\u008f\u0001\u0015\u0001\u0015\u0001e\u0000\u0016\u0001\u0001\u0003"+
		"\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011"+
		"\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010"+
		"!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016\u0001\u0000\u0006\u0002\u0000"+
		"++--\u0001\u000009\u0003\u0000AZ__az\u0004\u000009AZ__az\u0002\u0000\n"+
		"\n\r\r\u0002\u0000\t\t  \u009d\u0000\u0001\u0001\u0000\u0000\u0000\u0000"+
		"\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000"+
		"\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b"+
		"\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001"+
		"\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001"+
		"\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001"+
		"\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001"+
		"\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001"+
		"\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000"+
		"\u0000\u0000%\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000"+
		"\u0000)\u0001\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0001-"+
		"\u0001\u0000\u0000\u0000\u0003/\u0001\u0000\u0000\u0000\u00051\u0001\u0000"+
		"\u0000\u0000\u00073\u0001\u0000\u0000\u0000\t5\u0001\u0000\u0000\u0000"+
		"\u000b7\u0001\u0000\u0000\u0000\r9\u0001\u0000\u0000\u0000\u000f;\u0001"+
		"\u0000\u0000\u0000\u0011=\u0001\u0000\u0000\u0000\u0013@\u0001\u0000\u0000"+
		"\u0000\u0015H\u0001\u0000\u0000\u0000\u0017_\u0001\u0000\u0000\u0000\u0019"+
		"a\u0001\u0000\u0000\u0000\u001bj\u0001\u0000\u0000\u0000\u001do\u0001"+
		"\u0000\u0000\u0000\u001fy\u0001\u0000\u0000\u0000!|\u0001\u0000\u0000"+
		"\u0000#\u007f\u0001\u0000\u0000\u0000%\u0082\u0001\u0000\u0000\u0000\'"+
		"\u0086\u0001\u0000\u0000\u0000)\u008a\u0001\u0000\u0000\u0000+\u008d\u0001"+
		"\u0000\u0000\u0000-.\u0005=\u0000\u0000.\u0002\u0001\u0000\u0000\u0000"+
		"/0\u0005+\u0000\u00000\u0004\u0001\u0000\u0000\u000012\u0005-\u0000\u0000"+
		"2\u0006\u0001\u0000\u0000\u000034\u0005*\u0000\u00004\b\u0001\u0000\u0000"+
		"\u000056\u0005/\u0000\u00006\n\u0001\u0000\u0000\u000078\u0005%\u0000"+
		"\u00008\f\u0001\u0000\u0000\u00009:\u0005[\u0000\u0000:\u000e\u0001\u0000"+
		"\u0000\u0000;<\u0005,\u0000\u0000<\u0010\u0001\u0000\u0000\u0000=>\u0005"+
		"]\u0000\u0000>\u0012\u0001\u0000\u0000\u0000?A\u0007\u0000\u0000\u0000"+
		"@?\u0001\u0000\u0000\u0000@A\u0001\u0000\u0000\u0000AC\u0001\u0000\u0000"+
		"\u0000BD\u0007\u0001\u0000\u0000CB\u0001\u0000\u0000\u0000DE\u0001\u0000"+
		"\u0000\u0000EC\u0001\u0000\u0000\u0000EF\u0001\u0000\u0000\u0000F\u0014"+
		"\u0001\u0000\u0000\u0000GI\u0007\u0000\u0000\u0000HG\u0001\u0000\u0000"+
		"\u0000HI\u0001\u0000\u0000\u0000IM\u0001\u0000\u0000\u0000JL\u0007\u0001"+
		"\u0000\u0000KJ\u0001\u0000\u0000\u0000LO\u0001\u0000\u0000\u0000MK\u0001"+
		"\u0000\u0000\u0000MN\u0001\u0000\u0000\u0000NP\u0001\u0000\u0000\u0000"+
		"OM\u0001\u0000\u0000\u0000PR\u0005.\u0000\u0000QS\u0007\u0001\u0000\u0000"+
		"RQ\u0001\u0000\u0000\u0000ST\u0001\u0000\u0000\u0000TR\u0001\u0000\u0000"+
		"\u0000TU\u0001\u0000\u0000\u0000U\u0016\u0001\u0000\u0000\u0000VW\u0005"+
		"T\u0000\u0000WX\u0005r\u0000\u0000XY\u0005u\u0000\u0000Y`\u0005e\u0000"+
		"\u0000Z[\u0005F\u0000\u0000[\\\u0005a\u0000\u0000\\]\u0005l\u0000\u0000"+
		"]^\u0005s\u0000\u0000^`\u0005e\u0000\u0000_V\u0001\u0000\u0000\u0000_"+
		"Z\u0001\u0000\u0000\u0000`\u0018\u0001\u0000\u0000\u0000ae\u0005\"\u0000"+
		"\u0000bd\t\u0000\u0000\u0000cb\u0001\u0000\u0000\u0000dg\u0001\u0000\u0000"+
		"\u0000ef\u0001\u0000\u0000\u0000ec\u0001\u0000\u0000\u0000fh\u0001\u0000"+
		"\u0000\u0000ge\u0001\u0000\u0000\u0000hi\u0005\"\u0000\u0000i\u001a\u0001"+
		"\u0000\u0000\u0000jk\u0005\'\u0000\u0000kl\t\u0000\u0000\u0000lm\u0005"+
		"\'\u0000\u0000m\u001c\u0001\u0000\u0000\u0000np\u0007\u0002\u0000\u0000"+
		"on\u0001\u0000\u0000\u0000pq\u0001\u0000\u0000\u0000qo\u0001\u0000\u0000"+
		"\u0000qr\u0001\u0000\u0000\u0000rv\u0001\u0000\u0000\u0000su\u0007\u0003"+
		"\u0000\u0000ts\u0001\u0000\u0000\u0000ux\u0001\u0000\u0000\u0000vt\u0001"+
		"\u0000\u0000\u0000vw\u0001\u0000\u0000\u0000w\u001e\u0001\u0000\u0000"+
		"\u0000xv\u0001\u0000\u0000\u0000yz\u0005+\u0000\u0000z{\u0005=\u0000\u0000"+
		"{ \u0001\u0000\u0000\u0000|}\u0005-\u0000\u0000}~\u0005=\u0000\u0000~"+
		"\"\u0001\u0000\u0000\u0000\u007f\u0080\u0005*\u0000\u0000\u0080\u0081"+
		"\u0005=\u0000\u0000\u0081$\u0001\u0000\u0000\u0000\u0082\u0083\u0005/"+
		"\u0000\u0000\u0083\u0084\u0005=\u0000\u0000\u0084&\u0001\u0000\u0000\u0000"+
		"\u0085\u0087\u0007\u0004\u0000\u0000\u0086\u0085\u0001\u0000\u0000\u0000"+
		"\u0087\u0088\u0001\u0000\u0000\u0000\u0088\u0086\u0001\u0000\u0000\u0000"+
		"\u0088\u0089\u0001\u0000\u0000\u0000\u0089(\u0001\u0000\u0000\u0000\u008a"+
		"\u008b\u0005\t\u0000\u0000\u008b*\u0001\u0000\u0000\u0000\u008c\u008e"+
		"\u0007\u0005\u0000\u0000\u008d\u008c\u0001\u0000\u0000\u0000\u008e\u008f"+
		"\u0001\u0000\u0000\u0000\u008f\u008d\u0001\u0000\u0000\u0000\u008f\u0090"+
		"\u0001\u0000\u0000\u0000\u0090\u0091\u0001\u0000\u0000\u0000\u0091\u0092"+
		"\u0006\u0015\u0000\u0000\u0092,\u0001\u0000\u0000\u0000\f\u0000@EHMT_"+
		"eqv\u0088\u008f\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}