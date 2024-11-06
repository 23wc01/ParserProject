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
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, INT=15, FLOAT=16, BOOL=17, 
		STRING=18, VARNAME=19, NEWLINE=20, INDENT=21, WS=22;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "T__12", "T__13", "INT", "FLOAT", "BOOL", "STRING", 
			"VARNAME", "NEWLINE", "INDENT", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'+='", "'-='", "'*='", 
			"'/='", "'%='", "'['", "','", "']'", null, null, null, null, null, null, 
			"'\\t'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, "INT", "FLOAT", "BOOL", "STRING", "VARNAME", "NEWLINE", 
			"INDENT", "WS"
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
		"\u0004\u0000\u0016\u0092\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004"+
		"\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007"+
		"\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001"+
		"\t\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001"+
		"\r\u0001\r\u0001\u000e\u0003\u000eP\b\u000e\u0001\u000e\u0004\u000eS\b"+
		"\u000e\u000b\u000e\f\u000eT\u0001\u000f\u0003\u000fX\b\u000f\u0001\u000f"+
		"\u0005\u000f[\b\u000f\n\u000f\f\u000f^\t\u000f\u0001\u000f\u0001\u000f"+
		"\u0004\u000fb\b\u000f\u000b\u000f\f\u000fc\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001"+
		"\u0010\u0003\u0010o\b\u0010\u0001\u0011\u0001\u0011\u0005\u0011s\b\u0011"+
		"\n\u0011\f\u0011v\t\u0011\u0001\u0011\u0001\u0011\u0001\u0012\u0004\u0012"+
		"{\b\u0012\u000b\u0012\f\u0012|\u0001\u0012\u0005\u0012\u0080\b\u0012\n"+
		"\u0012\f\u0012\u0083\t\u0012\u0001\u0013\u0004\u0013\u0086\b\u0013\u000b"+
		"\u0013\f\u0013\u0087\u0001\u0014\u0001\u0014\u0001\u0015\u0004\u0015\u008d"+
		"\b\u0015\u000b\u0015\f\u0015\u008e\u0001\u0015\u0001\u0015\u0000\u0000"+
		"\u0016\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006"+
		"\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e"+
		"\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014)\u0015+\u0016\u0001"+
		"\u0000\u0006\u0002\u0000++--\u0001\u000009\u0004\u000009AZ__az\u0003\u0000"+
		"AZ__az\u0002\u0000\n\n\r\r\u0002\u0000\t\t  \u009c\u0000\u0001\u0001\u0000"+
		"\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000\u0000\u0005\u0001\u0000"+
		"\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000\u0000\t\u0001\u0000\u0000"+
		"\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000\r\u0001\u0000\u0000\u0000"+
		"\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011\u0001\u0000\u0000\u0000"+
		"\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015\u0001\u0000\u0000\u0000"+
		"\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019\u0001\u0000\u0000\u0000"+
		"\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d\u0001\u0000\u0000\u0000"+
		"\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001\u0000\u0000\u0000\u0000"+
		"#\u0001\u0000\u0000\u0000\u0000%\u0001\u0000\u0000\u0000\u0000\'\u0001"+
		"\u0000\u0000\u0000\u0000)\u0001\u0000\u0000\u0000\u0000+\u0001\u0000\u0000"+
		"\u0000\u0001-\u0001\u0000\u0000\u0000\u0003/\u0001\u0000\u0000\u0000\u0005"+
		"1\u0001\u0000\u0000\u0000\u00073\u0001\u0000\u0000\u0000\t5\u0001\u0000"+
		"\u0000\u0000\u000b7\u0001\u0000\u0000\u0000\r9\u0001\u0000\u0000\u0000"+
		"\u000f<\u0001\u0000\u0000\u0000\u0011?\u0001\u0000\u0000\u0000\u0013B"+
		"\u0001\u0000\u0000\u0000\u0015E\u0001\u0000\u0000\u0000\u0017H\u0001\u0000"+
		"\u0000\u0000\u0019J\u0001\u0000\u0000\u0000\u001bL\u0001\u0000\u0000\u0000"+
		"\u001dO\u0001\u0000\u0000\u0000\u001fW\u0001\u0000\u0000\u0000!n\u0001"+
		"\u0000\u0000\u0000#p\u0001\u0000\u0000\u0000%z\u0001\u0000\u0000\u0000"+
		"\'\u0085\u0001\u0000\u0000\u0000)\u0089\u0001\u0000\u0000\u0000+\u008c"+
		"\u0001\u0000\u0000\u0000-.\u0005=\u0000\u0000.\u0002\u0001\u0000\u0000"+
		"\u0000/0\u0005+\u0000\u00000\u0004\u0001\u0000\u0000\u000012\u0005-\u0000"+
		"\u00002\u0006\u0001\u0000\u0000\u000034\u0005*\u0000\u00004\b\u0001\u0000"+
		"\u0000\u000056\u0005/\u0000\u00006\n\u0001\u0000\u0000\u000078\u0005%"+
		"\u0000\u00008\f\u0001\u0000\u0000\u00009:\u0005+\u0000\u0000:;\u0005="+
		"\u0000\u0000;\u000e\u0001\u0000\u0000\u0000<=\u0005-\u0000\u0000=>\u0005"+
		"=\u0000\u0000>\u0010\u0001\u0000\u0000\u0000?@\u0005*\u0000\u0000@A\u0005"+
		"=\u0000\u0000A\u0012\u0001\u0000\u0000\u0000BC\u0005/\u0000\u0000CD\u0005"+
		"=\u0000\u0000D\u0014\u0001\u0000\u0000\u0000EF\u0005%\u0000\u0000FG\u0005"+
		"=\u0000\u0000G\u0016\u0001\u0000\u0000\u0000HI\u0005[\u0000\u0000I\u0018"+
		"\u0001\u0000\u0000\u0000JK\u0005,\u0000\u0000K\u001a\u0001\u0000\u0000"+
		"\u0000LM\u0005]\u0000\u0000M\u001c\u0001\u0000\u0000\u0000NP\u0007\u0000"+
		"\u0000\u0000ON\u0001\u0000\u0000\u0000OP\u0001\u0000\u0000\u0000PR\u0001"+
		"\u0000\u0000\u0000QS\u0007\u0001\u0000\u0000RQ\u0001\u0000\u0000\u0000"+
		"ST\u0001\u0000\u0000\u0000TR\u0001\u0000\u0000\u0000TU\u0001\u0000\u0000"+
		"\u0000U\u001e\u0001\u0000\u0000\u0000VX\u0007\u0000\u0000\u0000WV\u0001"+
		"\u0000\u0000\u0000WX\u0001\u0000\u0000\u0000X\\\u0001\u0000\u0000\u0000"+
		"Y[\u0007\u0001\u0000\u0000ZY\u0001\u0000\u0000\u0000[^\u0001\u0000\u0000"+
		"\u0000\\Z\u0001\u0000\u0000\u0000\\]\u0001\u0000\u0000\u0000]_\u0001\u0000"+
		"\u0000\u0000^\\\u0001\u0000\u0000\u0000_a\u0005.\u0000\u0000`b\u0007\u0001"+
		"\u0000\u0000a`\u0001\u0000\u0000\u0000bc\u0001\u0000\u0000\u0000ca\u0001"+
		"\u0000\u0000\u0000cd\u0001\u0000\u0000\u0000d \u0001\u0000\u0000\u0000"+
		"ef\u0005T\u0000\u0000fg\u0005r\u0000\u0000gh\u0005u\u0000\u0000ho\u0005"+
		"e\u0000\u0000ij\u0005F\u0000\u0000jk\u0005a\u0000\u0000kl\u0005l\u0000"+
		"\u0000lm\u0005s\u0000\u0000mo\u0005e\u0000\u0000ne\u0001\u0000\u0000\u0000"+
		"ni\u0001\u0000\u0000\u0000o\"\u0001\u0000\u0000\u0000pt\u0005\"\u0000"+
		"\u0000qs\u0007\u0002\u0000\u0000rq\u0001\u0000\u0000\u0000sv\u0001\u0000"+
		"\u0000\u0000tr\u0001\u0000\u0000\u0000tu\u0001\u0000\u0000\u0000uw\u0001"+
		"\u0000\u0000\u0000vt\u0001\u0000\u0000\u0000wx\u0005\"\u0000\u0000x$\u0001"+
		"\u0000\u0000\u0000y{\u0007\u0003\u0000\u0000zy\u0001\u0000\u0000\u0000"+
		"{|\u0001\u0000\u0000\u0000|z\u0001\u0000\u0000\u0000|}\u0001\u0000\u0000"+
		"\u0000}\u0081\u0001\u0000\u0000\u0000~\u0080\u0007\u0002\u0000\u0000\u007f"+
		"~\u0001\u0000\u0000\u0000\u0080\u0083\u0001\u0000\u0000\u0000\u0081\u007f"+
		"\u0001\u0000\u0000\u0000\u0081\u0082\u0001\u0000\u0000\u0000\u0082&\u0001"+
		"\u0000\u0000\u0000\u0083\u0081\u0001\u0000\u0000\u0000\u0084\u0086\u0007"+
		"\u0004\u0000\u0000\u0085\u0084\u0001\u0000\u0000\u0000\u0086\u0087\u0001"+
		"\u0000\u0000\u0000\u0087\u0085\u0001\u0000\u0000\u0000\u0087\u0088\u0001"+
		"\u0000\u0000\u0000\u0088(\u0001\u0000\u0000\u0000\u0089\u008a\u0005\t"+
		"\u0000\u0000\u008a*\u0001\u0000\u0000\u0000\u008b\u008d\u0007\u0005\u0000"+
		"\u0000\u008c\u008b\u0001\u0000\u0000\u0000\u008d\u008e\u0001\u0000\u0000"+
		"\u0000\u008e\u008c\u0001\u0000\u0000\u0000\u008e\u008f\u0001\u0000\u0000"+
		"\u0000\u008f\u0090\u0001\u0000\u0000\u0000\u0090\u0091\u0006\u0015\u0000"+
		"\u0000\u0091,\u0001\u0000\u0000\u0000\f\u0000OTW\\cnt|\u0081\u0087\u008e"+
		"\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}