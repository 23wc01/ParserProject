// Generated from PythonParser.G4 by ANTLR 4.13.2
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
		STRING=18, CHAR=19, VARNAME=20, NEWLINE=21, INDENT=22, WS=23;
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
			"CHAR", "VARNAME", "NEWLINE", "INDENT", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'='", "'+'", "'-'", "'*'", "'/'", "'%'", "'+='", "'-='", "'*='", 
			"'/='", "'%='", "'['", "','", "']'", null, null, null, null, null, null, 
			null, "'\\t'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, "INT", "FLOAT", "BOOL", "STRING", "CHAR", "VARNAME", 
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
	public String getGrammarFileName() { return "PythonParser.G4"; }

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
		"\u0004\u0000\u0017\u0098\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011"+
		"\u0002\u0012\u0007\u0012\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014"+
		"\u0002\u0015\u0007\u0015\u0002\u0016\u0007\u0016\u0001\u0000\u0001\u0000"+
		"\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003"+
		"\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001"+
		"\b\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\u000b\u0001\u000b"+
		"\u0001\f\u0001\f\u0001\r\u0001\r\u0001\u000e\u0003\u000eR\b\u000e\u0001"+
		"\u000e\u0004\u000eU\b\u000e\u000b\u000e\f\u000eV\u0001\u000f\u0003\u000f"+
		"Z\b\u000f\u0001\u000f\u0005\u000f]\b\u000f\n\u000f\f\u000f`\t\u000f\u0001"+
		"\u000f\u0001\u000f\u0004\u000fd\b\u000f\u000b\u000f\f\u000fe\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0010\u0001\u0010\u0003\u0010q\b\u0010\u0001\u0011\u0001\u0011"+
		"\u0005\u0011u\b\u0011\n\u0011\f\u0011x\t\u0011\u0001\u0011\u0001\u0011"+
		"\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0013\u0004\u0013"+
		"\u0081\b\u0013\u000b\u0013\f\u0013\u0082\u0001\u0013\u0005\u0013\u0086"+
		"\b\u0013\n\u0013\f\u0013\u0089\t\u0013\u0001\u0014\u0004\u0014\u008c\b"+
		"\u0014\u000b\u0014\f\u0014\u008d\u0001\u0015\u0001\u0015\u0001\u0016\u0004"+
		"\u0016\u0093\b\u0016\u000b\u0016\f\u0016\u0094\u0001\u0016\u0001\u0016"+
		"\u0001v\u0000\u0017\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t"+
		"\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f"+
		"\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011#\u0012%\u0013\'\u0014"+
		")\u0015+\u0016-\u0017\u0001\u0000\u0006\u0002\u0000++--\u0001\u000009"+
		"\u0003\u0000AZ__az\u0004\u000009AZ__az\u0002\u0000\n\n\r\r\u0002\u0000"+
		"\t\t  \u00a2\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000"+
		"\u0000\u0000\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000"+
		"\u0000\u0000\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000"+
		"\u0000\u0000\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000"+
		"\u0000\u0011\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000"+
		"\u0000\u0015\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000"+
		"\u0000\u0019\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000"+
		"\u0000\u001d\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000"+
		"\u0000!\u0001\u0000\u0000\u0000\u0000#\u0001\u0000\u0000\u0000\u0000%"+
		"\u0001\u0000\u0000\u0000\u0000\'\u0001\u0000\u0000\u0000\u0000)\u0001"+
		"\u0000\u0000\u0000\u0000+\u0001\u0000\u0000\u0000\u0000-\u0001\u0000\u0000"+
		"\u0000\u0001/\u0001\u0000\u0000\u0000\u00031\u0001\u0000\u0000\u0000\u0005"+
		"3\u0001\u0000\u0000\u0000\u00075\u0001\u0000\u0000\u0000\t7\u0001\u0000"+
		"\u0000\u0000\u000b9\u0001\u0000\u0000\u0000\r;\u0001\u0000\u0000\u0000"+
		"\u000f>\u0001\u0000\u0000\u0000\u0011A\u0001\u0000\u0000\u0000\u0013D"+
		"\u0001\u0000\u0000\u0000\u0015G\u0001\u0000\u0000\u0000\u0017J\u0001\u0000"+
		"\u0000\u0000\u0019L\u0001\u0000\u0000\u0000\u001bN\u0001\u0000\u0000\u0000"+
		"\u001dQ\u0001\u0000\u0000\u0000\u001fY\u0001\u0000\u0000\u0000!p\u0001"+
		"\u0000\u0000\u0000#r\u0001\u0000\u0000\u0000%{\u0001\u0000\u0000\u0000"+
		"\'\u0080\u0001\u0000\u0000\u0000)\u008b\u0001\u0000\u0000\u0000+\u008f"+
		"\u0001\u0000\u0000\u0000-\u0092\u0001\u0000\u0000\u0000/0\u0005=\u0000"+
		"\u00000\u0002\u0001\u0000\u0000\u000012\u0005+\u0000\u00002\u0004\u0001"+
		"\u0000\u0000\u000034\u0005-\u0000\u00004\u0006\u0001\u0000\u0000\u0000"+
		"56\u0005*\u0000\u00006\b\u0001\u0000\u0000\u000078\u0005/\u0000\u0000"+
		"8\n\u0001\u0000\u0000\u00009:\u0005%\u0000\u0000:\f\u0001\u0000\u0000"+
		"\u0000;<\u0005+\u0000\u0000<=\u0005=\u0000\u0000=\u000e\u0001\u0000\u0000"+
		"\u0000>?\u0005-\u0000\u0000?@\u0005=\u0000\u0000@\u0010\u0001\u0000\u0000"+
		"\u0000AB\u0005*\u0000\u0000BC\u0005=\u0000\u0000C\u0012\u0001\u0000\u0000"+
		"\u0000DE\u0005/\u0000\u0000EF\u0005=\u0000\u0000F\u0014\u0001\u0000\u0000"+
		"\u0000GH\u0005%\u0000\u0000HI\u0005=\u0000\u0000I\u0016\u0001\u0000\u0000"+
		"\u0000JK\u0005[\u0000\u0000K\u0018\u0001\u0000\u0000\u0000LM\u0005,\u0000"+
		"\u0000M\u001a\u0001\u0000\u0000\u0000NO\u0005]\u0000\u0000O\u001c\u0001"+
		"\u0000\u0000\u0000PR\u0007\u0000\u0000\u0000QP\u0001\u0000\u0000\u0000"+
		"QR\u0001\u0000\u0000\u0000RT\u0001\u0000\u0000\u0000SU\u0007\u0001\u0000"+
		"\u0000TS\u0001\u0000\u0000\u0000UV\u0001\u0000\u0000\u0000VT\u0001\u0000"+
		"\u0000\u0000VW\u0001\u0000\u0000\u0000W\u001e\u0001\u0000\u0000\u0000"+
		"XZ\u0007\u0000\u0000\u0000YX\u0001\u0000\u0000\u0000YZ\u0001\u0000\u0000"+
		"\u0000Z^\u0001\u0000\u0000\u0000[]\u0007\u0001\u0000\u0000\\[\u0001\u0000"+
		"\u0000\u0000]`\u0001\u0000\u0000\u0000^\\\u0001\u0000\u0000\u0000^_\u0001"+
		"\u0000\u0000\u0000_a\u0001\u0000\u0000\u0000`^\u0001\u0000\u0000\u0000"+
		"ac\u0005.\u0000\u0000bd\u0007\u0001\u0000\u0000cb\u0001\u0000\u0000\u0000"+
		"de\u0001\u0000\u0000\u0000ec\u0001\u0000\u0000\u0000ef\u0001\u0000\u0000"+
		"\u0000f \u0001\u0000\u0000\u0000gh\u0005T\u0000\u0000hi\u0005r\u0000\u0000"+
		"ij\u0005u\u0000\u0000jq\u0005e\u0000\u0000kl\u0005F\u0000\u0000lm\u0005"+
		"a\u0000\u0000mn\u0005l\u0000\u0000no\u0005s\u0000\u0000oq\u0005e\u0000"+
		"\u0000pg\u0001\u0000\u0000\u0000pk\u0001\u0000\u0000\u0000q\"\u0001\u0000"+
		"\u0000\u0000rv\u0005\"\u0000\u0000su\t\u0000\u0000\u0000ts\u0001\u0000"+
		"\u0000\u0000ux\u0001\u0000\u0000\u0000vw\u0001\u0000\u0000\u0000vt\u0001"+
		"\u0000\u0000\u0000wy\u0001\u0000\u0000\u0000xv\u0001\u0000\u0000\u0000"+
		"yz\u0005\"\u0000\u0000z$\u0001\u0000\u0000\u0000{|\u0005\'\u0000\u0000"+
		"|}\t\u0000\u0000\u0000}~\u0005\'\u0000\u0000~&\u0001\u0000\u0000\u0000"+
		"\u007f\u0081\u0007\u0002\u0000\u0000\u0080\u007f\u0001\u0000\u0000\u0000"+
		"\u0081\u0082\u0001\u0000\u0000\u0000\u0082\u0080\u0001\u0000\u0000\u0000"+
		"\u0082\u0083\u0001\u0000\u0000\u0000\u0083\u0087\u0001\u0000\u0000\u0000"+
		"\u0084\u0086\u0007\u0003\u0000\u0000\u0085\u0084\u0001\u0000\u0000\u0000"+
		"\u0086\u0089\u0001\u0000\u0000\u0000\u0087\u0085\u0001\u0000\u0000\u0000"+
		"\u0087\u0088\u0001\u0000\u0000\u0000\u0088(\u0001\u0000\u0000\u0000\u0089"+
		"\u0087\u0001\u0000\u0000\u0000\u008a\u008c\u0007\u0004\u0000\u0000\u008b"+
		"\u008a\u0001\u0000\u0000\u0000\u008c\u008d\u0001\u0000\u0000\u0000\u008d"+
		"\u008b\u0001\u0000\u0000\u0000\u008d\u008e\u0001\u0000\u0000\u0000\u008e"+
		"*\u0001\u0000\u0000\u0000\u008f\u0090\u0005\t\u0000\u0000\u0090,\u0001"+
		"\u0000\u0000\u0000\u0091\u0093\u0007\u0005\u0000\u0000\u0092\u0091\u0001"+
		"\u0000\u0000\u0000\u0093\u0094\u0001\u0000\u0000\u0000\u0094\u0092\u0001"+
		"\u0000\u0000\u0000\u0094\u0095\u0001\u0000\u0000\u0000\u0095\u0096\u0001"+
		"\u0000\u0000\u0000\u0096\u0097\u0006\u0016\u0000\u0000\u0097.\u0001\u0000"+
		"\u0000\u0000\f\u0000QVY^epv\u0082\u0087\u008d\u0094\u0001\u0006\u0000"+
		"\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}