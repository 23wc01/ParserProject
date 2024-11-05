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
		T__9=10, T__10=11, T__11=12, T__12=13, INT=14, FLOAT=15, VARNAME=16, WS=17;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
			"T__9", "T__10", "T__11", "T__12", "INT", "FLOAT", "VARNAME", "WS"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'def main():'", "'\\t'", "'\\n'", "'+'", "'-'", "'*'", "'/'", 
			"'%'", "'='", "'+='", "'-='", "'*='", "'/='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, "INT", "FLOAT", "VARNAME", "WS"
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
		"\u0004\u0000\u0011w\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002\u0001"+
		"\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004"+
		"\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007"+
		"\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b"+
		"\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002"+
		"\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001"+
		"\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\u000b"+
		"\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\r\u0003\rM\b\r"+
		"\u0001\r\u0004\rP\b\r\u000b\r\f\rQ\u0001\u000e\u0003\u000eU\b\u000e\u0001"+
		"\u000e\u0005\u000eX\b\u000e\n\u000e\f\u000e[\t\u000e\u0001\u000e\u0001"+
		"\u000e\u0004\u000e_\b\u000e\u000b\u000e\f\u000e`\u0001\u000f\u0003\u000f"+
		"d\b\u000f\u0001\u000f\u0004\u000fg\b\u000f\u000b\u000f\f\u000fh\u0001"+
		"\u000f\u0005\u000fl\b\u000f\n\u000f\f\u000fo\t\u000f\u0001\u0010\u0004"+
		"\u0010r\b\u0010\u000b\u0010\f\u0010s\u0001\u0010\u0001\u0010\u0000\u0000"+
		"\u0011\u0001\u0001\u0003\u0002\u0005\u0003\u0007\u0004\t\u0005\u000b\u0006"+
		"\r\u0007\u000f\b\u0011\t\u0013\n\u0015\u000b\u0017\f\u0019\r\u001b\u000e"+
		"\u001d\u000f\u001f\u0010!\u0011\u0001\u0000\u0005\u0002\u0000++--\u0001"+
		"\u000009\u0003\u0000AZ__az\u0004\u000009AZ__az\u0003\u0000\t\n\r\r  \u007f"+
		"\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000"+
		"\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000"+
		"\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000"+
		"\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011"+
		"\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015"+
		"\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019"+
		"\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d"+
		"\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001"+
		"\u0000\u0000\u0000\u0001#\u0001\u0000\u0000\u0000\u0003/\u0001\u0000\u0000"+
		"\u0000\u00051\u0001\u0000\u0000\u0000\u00073\u0001\u0000\u0000\u0000\t"+
		"5\u0001\u0000\u0000\u0000\u000b7\u0001\u0000\u0000\u0000\r9\u0001\u0000"+
		"\u0000\u0000\u000f;\u0001\u0000\u0000\u0000\u0011=\u0001\u0000\u0000\u0000"+
		"\u0013?\u0001\u0000\u0000\u0000\u0015B\u0001\u0000\u0000\u0000\u0017E"+
		"\u0001\u0000\u0000\u0000\u0019H\u0001\u0000\u0000\u0000\u001bL\u0001\u0000"+
		"\u0000\u0000\u001dT\u0001\u0000\u0000\u0000\u001fc\u0001\u0000\u0000\u0000"+
		"!q\u0001\u0000\u0000\u0000#$\u0005d\u0000\u0000$%\u0005e\u0000\u0000%"+
		"&\u0005f\u0000\u0000&\'\u0005 \u0000\u0000\'(\u0005m\u0000\u0000()\u0005"+
		"a\u0000\u0000)*\u0005i\u0000\u0000*+\u0005n\u0000\u0000+,\u0005(\u0000"+
		"\u0000,-\u0005)\u0000\u0000-.\u0005:\u0000\u0000.\u0002\u0001\u0000\u0000"+
		"\u0000/0\u0005\t\u0000\u00000\u0004\u0001\u0000\u0000\u000012\u0005\n"+
		"\u0000\u00002\u0006\u0001\u0000\u0000\u000034\u0005+\u0000\u00004\b\u0001"+
		"\u0000\u0000\u000056\u0005-\u0000\u00006\n\u0001\u0000\u0000\u000078\u0005"+
		"*\u0000\u00008\f\u0001\u0000\u0000\u00009:\u0005/\u0000\u0000:\u000e\u0001"+
		"\u0000\u0000\u0000;<\u0005%\u0000\u0000<\u0010\u0001\u0000\u0000\u0000"+
		"=>\u0005=\u0000\u0000>\u0012\u0001\u0000\u0000\u0000?@\u0005+\u0000\u0000"+
		"@A\u0005=\u0000\u0000A\u0014\u0001\u0000\u0000\u0000BC\u0005-\u0000\u0000"+
		"CD\u0005=\u0000\u0000D\u0016\u0001\u0000\u0000\u0000EF\u0005*\u0000\u0000"+
		"FG\u0005=\u0000\u0000G\u0018\u0001\u0000\u0000\u0000HI\u0005/\u0000\u0000"+
		"IJ\u0005=\u0000\u0000J\u001a\u0001\u0000\u0000\u0000KM\u0007\u0000\u0000"+
		"\u0000LK\u0001\u0000\u0000\u0000LM\u0001\u0000\u0000\u0000MO\u0001\u0000"+
		"\u0000\u0000NP\u0007\u0001\u0000\u0000ON\u0001\u0000\u0000\u0000PQ\u0001"+
		"\u0000\u0000\u0000QO\u0001\u0000\u0000\u0000QR\u0001\u0000\u0000\u0000"+
		"R\u001c\u0001\u0000\u0000\u0000SU\u0007\u0000\u0000\u0000TS\u0001\u0000"+
		"\u0000\u0000TU\u0001\u0000\u0000\u0000UY\u0001\u0000\u0000\u0000VX\u0007"+
		"\u0001\u0000\u0000WV\u0001\u0000\u0000\u0000X[\u0001\u0000\u0000\u0000"+
		"YW\u0001\u0000\u0000\u0000YZ\u0001\u0000\u0000\u0000Z\\\u0001\u0000\u0000"+
		"\u0000[Y\u0001\u0000\u0000\u0000\\^\u0005.\u0000\u0000]_\u0007\u0001\u0000"+
		"\u0000^]\u0001\u0000\u0000\u0000_`\u0001\u0000\u0000\u0000`^\u0001\u0000"+
		"\u0000\u0000`a\u0001\u0000\u0000\u0000a\u001e\u0001\u0000\u0000\u0000"+
		"bd\u0007\u0000\u0000\u0000cb\u0001\u0000\u0000\u0000cd\u0001\u0000\u0000"+
		"\u0000df\u0001\u0000\u0000\u0000eg\u0007\u0002\u0000\u0000fe\u0001\u0000"+
		"\u0000\u0000gh\u0001\u0000\u0000\u0000hf\u0001\u0000\u0000\u0000hi\u0001"+
		"\u0000\u0000\u0000im\u0001\u0000\u0000\u0000jl\u0007\u0003\u0000\u0000"+
		"kj\u0001\u0000\u0000\u0000lo\u0001\u0000\u0000\u0000mk\u0001\u0000\u0000"+
		"\u0000mn\u0001\u0000\u0000\u0000n \u0001\u0000\u0000\u0000om\u0001\u0000"+
		"\u0000\u0000pr\u0007\u0004\u0000\u0000qp\u0001\u0000\u0000\u0000rs\u0001"+
		"\u0000\u0000\u0000sq\u0001\u0000\u0000\u0000st\u0001\u0000\u0000\u0000"+
		"tu\u0001\u0000\u0000\u0000uv\u0006\u0010\u0000\u0000v\"\u0001\u0000\u0000"+
		"\u0000\n\u0000LQTY`chms\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}