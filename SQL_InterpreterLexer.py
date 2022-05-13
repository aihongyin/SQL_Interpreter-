# Generated from SQL_Interpreter.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2*")
        buf.write("\u01b8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\3\2\3\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3")
        buf.write("!\3!\3\"\3\"\3#\3#\3$\3$\3$\3%\3%\3&\3&\3&\3&\3\'\6\'")
        buf.write("\u016c\n\'\r\'\16\'\u016d\3(\6(\u0171\n(\r(\16(\u0172")
        buf.write("\3(\3(\6(\u0177\n(\r(\16(\u0178\3)\3)\6)\u017d\n)\r)\16")
        buf.write(")\u017e\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3")
        buf.write(">\3>\3?\3?\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\2\2F\3")
        buf.write("\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16")
        buf.write("\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61")
        buf.write("\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*")
        buf.write("S\2U\2W\2Y\2[\2]\2_\2a\2c\2e\2g\2i\2k\2m\2o\2q\2s\2u\2")
        buf.write("w\2y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087\2\u0089")
        buf.write("\2\3\2!\4\2))bb\5\2\13\f\17\17\"\"\3\2c|\5\2\62;aac|\3")
        buf.write("\2\62;\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2GGgg\4\2HHh")
        buf.write("h\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4\2NNnn\4\2")
        buf.write("OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTtt\4\2UUuu\4")
        buf.write("\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2[[{{\4\2\\\\")
        buf.write("||\2\u019f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\3\u008b\3\2\2\2\5\u0092\3\2\2\2\7\u0098\3\2\2\2\t")
        buf.write("\u009d\3\2\2\2\13\u00a2\3\2\2\2\r\u00a9\3\2\2\2\17\u00b0")
        buf.write("\3\2\2\2\21\u00b5\3\2\2\2\23\u00bc\3\2\2\2\25\u00c3\3")
        buf.write("\2\2\2\27\u00c8\3\2\2\2\31\u00ce\3\2\2\2\33\u00d6\3\2")
        buf.write("\2\2\35\u00da\3\2\2\2\37\u00e3\3\2\2\2!\u00eb\3\2\2\2")
        buf.write("#\u00f4\3\2\2\2%\u00fc\3\2\2\2\'\u0101\3\2\2\2)\u0108")
        buf.write("\3\2\2\2+\u0110\3\2\2\2-\u0122\3\2\2\2/\u0127\3\2\2\2")
        buf.write("\61\u0130\3\2\2\2\63\u013a\3\2\2\2\65\u013f\3\2\2\2\67")
        buf.write("\u0148\3\2\2\29\u0150\3\2\2\2;\u0155\3\2\2\2=\u0157\3")
        buf.write("\2\2\2?\u0159\3\2\2\2A\u015b\3\2\2\2C\u015d\3\2\2\2E\u015f")
        buf.write("\3\2\2\2G\u0161\3\2\2\2I\u0164\3\2\2\2K\u0166\3\2\2\2")
        buf.write("M\u016b\3\2\2\2O\u0170\3\2\2\2Q\u017a\3\2\2\2S\u0180\3")
        buf.write("\2\2\2U\u0182\3\2\2\2W\u0184\3\2\2\2Y\u0186\3\2\2\2[\u0188")
        buf.write("\3\2\2\2]\u018a\3\2\2\2_\u018c\3\2\2\2a\u018e\3\2\2\2")
        buf.write("c\u0190\3\2\2\2e\u0192\3\2\2\2g\u0194\3\2\2\2i\u0196\3")
        buf.write("\2\2\2k\u0198\3\2\2\2m\u019a\3\2\2\2o\u019c\3\2\2\2q\u019e")
        buf.write("\3\2\2\2s\u01a0\3\2\2\2u\u01a2\3\2\2\2w\u01a4\3\2\2\2")
        buf.write("y\u01a6\3\2\2\2{\u01a8\3\2\2\2}\u01aa\3\2\2\2\177\u01ac")
        buf.write("\3\2\2\2\u0081\u01ae\3\2\2\2\u0083\u01b0\3\2\2\2\u0085")
        buf.write("\u01b2\3\2\2\2\u0087\u01b4\3\2\2\2\u0089\u01b6\3\2\2\2")
        buf.write("\u008b\u008c\5[.\2\u008c\u008d\5y=\2\u008d\u008e\5_\60")
        buf.write("\2\u008e\u008f\5W,\2\u008f\u0090\5}?\2\u0090\u0091\5_")
        buf.write("\60\2\u0091\4\3\2\2\2\u0092\u0093\5}?\2\u0093\u0094\5")
        buf.write("W,\2\u0094\u0095\5Y-\2\u0095\u0096\5m\67\2\u0096\u0097")
        buf.write("\5_\60\2\u0097\6\3\2\2\2\u0098\u0099\5]/\2\u0099\u009a")
        buf.write("\5y=\2\u009a\u009b\5s:\2\u009b\u009c\5u;\2\u009c\b\3\2")
        buf.write("\2\2\u009d\u009e\5{>\2\u009e\u009f\5e\63\2\u009f\u00a0")
        buf.write("\5s:\2\u00a0\u00a1\5\u0083B\2\u00a1\n\3\2\2\2\u00a2\u00a3")
        buf.write("\5}?\2\u00a3\u00a4\5W,\2\u00a4\u00a5\5Y-\2\u00a5\u00a6")
        buf.write("\5m\67\2\u00a6\u00a7\5_\60\2\u00a7\u00a8\5{>\2\u00a8\f")
        buf.write("\3\2\2\2\u00a9\u00aa\5g\64\2\u00aa\u00ab\5q9\2\u00ab\u00ac")
        buf.write("\5{>\2\u00ac\u00ad\5_\60\2\u00ad\u00ae\5y=\2\u00ae\u00af")
        buf.write("\5}?\2\u00af\16\3\2\2\2\u00b0\u00b1\5g\64\2\u00b1\u00b2")
        buf.write("\5q9\2\u00b2\u00b3\5}?\2\u00b3\u00b4\5s:\2\u00b4\20\3")
        buf.write("\2\2\2\u00b5\u00b6\5\u0081A\2\u00b6\u00b7\5W,\2\u00b7")
        buf.write("\u00b8\5m\67\2\u00b8\u00b9\5\177@\2\u00b9\u00ba\5_\60")
        buf.write("\2\u00ba\u00bb\5{>\2\u00bb\22\3\2\2\2\u00bc\u00bd\5{>")
        buf.write("\2\u00bd\u00be\5_\60\2\u00be\u00bf\5m\67\2\u00bf\u00c0")
        buf.write("\5_\60\2\u00c0\u00c1\5[.\2\u00c1\u00c2\5}?\2\u00c2\24")
        buf.write("\3\2\2\2\u00c3\u00c4\5a\61\2\u00c4\u00c5\5y=\2\u00c5\u00c6")
        buf.write("\5s:\2\u00c6\u00c7\5o8\2\u00c7\26\3\2\2\2\u00c8\u00c9")
        buf.write("\5\u0083B\2\u00c9\u00ca\5e\63\2\u00ca\u00cb\5_\60\2\u00cb")
        buf.write("\u00cc\5y=\2\u00cc\u00cd\5_\60\2\u00cd\30\3\2\2\2\u00ce")
        buf.write("\u00cf\5g\64\2\u00cf\u00d0\5q9\2\u00d0\u00d1\5}?\2\u00d1")
        buf.write("\u00d2\5_\60\2\u00d2\u00d3\5c\62\2\u00d3\u00d4\5_\60\2")
        buf.write("\u00d4\u00d5\5y=\2\u00d5\32\3\2\2\2\u00d6\u00d7\5g\64")
        buf.write("\2\u00d7\u00d8\5q9\2\u00d8\u00d9\5}?\2\u00d9\34\3\2\2")
        buf.write("\2\u00da\u00db\5{>\2\u00db\u00dc\5o8\2\u00dc\u00dd\5W")
        buf.write(",\2\u00dd\u00de\5m\67\2\u00de\u00df\5m\67\2\u00df\u00e0")
        buf.write("\5g\64\2\u00e0\u00e1\5q9\2\u00e1\u00e2\5}?\2\u00e2\36")
        buf.write("\3\2\2\2\u00e3\u00e4\5}?\2\u00e4\u00e5\5g\64\2\u00e5\u00e6")
        buf.write("\5q9\2\u00e6\u00e7\5\u0087D\2\u00e7\u00e8\5g\64\2\u00e8")
        buf.write("\u00e9\5q9\2\u00e9\u00ea\5}?\2\u00ea \3\2\2\2\u00eb\u00ec")
        buf.write("\5\177@\2\u00ec\u00ed\5q9\2\u00ed\u00ee\5{>\2\u00ee\u00ef")
        buf.write("\5g\64\2\u00ef\u00f0\5c\62\2\u00f0\u00f1\5q9\2\u00f1\u00f2")
        buf.write("\5_\60\2\u00f2\u00f3\5]/\2\u00f3\"\3\2\2\2\u00f4\u00f5")
        buf.write("\5q9\2\u00f5\u00f6\5\177@\2\u00f6\u00f7\5o8\2\u00f7\u00f8")
        buf.write("\5_\60\2\u00f8\u00f9\5y=\2\u00f9\u00fa\5g\64\2\u00fa\u00fb")
        buf.write("\5[.\2\u00fb$\3\2\2\2\u00fc\u00fd\5q9\2\u00fd\u00fe\5")
        buf.write("\177@\2\u00fe\u00ff\5m\67\2\u00ff\u0100\5m\67\2\u0100")
        buf.write("&\3\2\2\2\u0101\u0102\5{>\2\u0102\u0103\5}?\2\u0103\u0104")
        buf.write("\5y=\2\u0104\u0105\5g\64\2\u0105\u0106\5q9\2\u0106\u0107")
        buf.write("\5c\62\2\u0107(\3\2\2\2\u0108\u0109\5\u0081A\2\u0109\u010a")
        buf.write("\5W,\2\u010a\u010b\5y=\2\u010b\u010c\5[.\2\u010c\u010d")
        buf.write("\5e\63\2\u010d\u010e\5W,\2\u010e\u010f\5y=\2\u010f*\3")
        buf.write("\2\2\2\u0110\u0111\5[.\2\u0111\u0112\5e\63\2\u0112\u0113")
        buf.write("\5W,\2\u0113\u0114\5y=\2\u0114\u0115\5W,\2\u0115\u0116")
        buf.write("\5[.\2\u0116\u0117\5}?\2\u0117\u0118\5_\60\2\u0118\u0119")
        buf.write("\5y=\2\u0119\u011a\7\"\2\2\u011a\u011b\5\u0081A\2\u011b")
        buf.write("\u011c\5W,\2\u011c\u011d\5y=\2\u011d\u011e\5\u0087D\2")
        buf.write("\u011e\u011f\5g\64\2\u011f\u0120\5q9\2\u0120\u0121\5c")
        buf.write("\62\2\u0121,\3\2\2\2\u0122\u0123\5[.\2\u0123\u0124\5e")
        buf.write("\63\2\u0124\u0125\5W,\2\u0125\u0126\5y=\2\u0126.\3\2\2")
        buf.write("\2\u0127\u0128\5]/\2\u0128\u0129\5W,\2\u0129\u012a\5}")
        buf.write("?\2\u012a\u012b\5_\60\2\u012b\u012c\5}?\2\u012c\u012d")
        buf.write("\5g\64\2\u012d\u012e\5o8\2\u012e\u012f\5_\60\2\u012f\60")
        buf.write("\3\2\2\2\u0130\u0131\5}?\2\u0131\u0132\5g\64\2\u0132\u0133")
        buf.write("\5o8\2\u0133\u0134\5_\60\2\u0134\u0135\5{>\2\u0135\u0136")
        buf.write("\5}?\2\u0136\u0137\5W,\2\u0137\u0138\5o8\2\u0138\u0139")
        buf.write("\5u;\2\u0139\62\3\2\2\2\u013a\u013b\5Y-\2\u013b\u013c")
        buf.write("\5m\67\2\u013c\u013d\5s:\2\u013d\u013e\5Y-\2\u013e\64")
        buf.write("\3\2\2\2\u013f\u0140\5{>\2\u0140\u0141\5\177@\2\u0141")
        buf.write("\u0142\5Y-\2\u0142\u0143\5S*\2\u0143\u0144\5}?\2\u0144")
        buf.write("\u0145\5\u0087D\2\u0145\u0146\5u;\2\u0146\u0147\5_\60")
        buf.write("\2\u0147\66\3\2\2\2\u0148\u0149\5]/\2\u0149\u014a\5_\60")
        buf.write("\2\u014a\u014b\5[.\2\u014b\u014c\5g\64\2\u014c\u014d\5")
        buf.write("o8\2\u014d\u014e\5W,\2\u014e\u014f\5m\67\2\u014f8\3\2")
        buf.write("\2\2\u0150\u0151\5\u0087D\2\u0151\u0152\5_\60\2\u0152")
        buf.write("\u0153\5W,\2\u0153\u0154\5y=\2\u0154:\3\2\2\2\u0155\u0156")
        buf.write("\t\2\2\2\u0156<\3\2\2\2\u0157\u0158\7*\2\2\u0158>\3\2")
        buf.write("\2\2\u0159\u015a\7+\2\2\u015a@\3\2\2\2\u015b\u015c\7.")
        buf.write("\2\2\u015cB\3\2\2\2\u015d\u015e\7=\2\2\u015eD\3\2\2\2")
        buf.write("\u015f\u0160\7?\2\2\u0160F\3\2\2\2\u0161\u0162\7<\2\2")
        buf.write("\u0162\u0163\7<\2\2\u0163H\3\2\2\2\u0164\u0165\7,\2\2")
        buf.write("\u0165J\3\2\2\2\u0166\u0167\t\3\2\2\u0167\u0168\3\2\2")
        buf.write("\2\u0168\u0169\b&\2\2\u0169L\3\2\2\2\u016a\u016c\5U+\2")
        buf.write("\u016b\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d\u016b\3")
        buf.write("\2\2\2\u016d\u016e\3\2\2\2\u016eN\3\2\2\2\u016f\u0171")
        buf.write("\5U+\2\u0170\u016f\3\2\2\2\u0171\u0172\3\2\2\2\u0172\u0170")
        buf.write("\3\2\2\2\u0172\u0173\3\2\2\2\u0173\u0174\3\2\2\2\u0174")
        buf.write("\u0176\7\60\2\2\u0175\u0177\5U+\2\u0176\u0175\3\2\2\2")
        buf.write("\u0177\u0178\3\2\2\2\u0178\u0176\3\2\2\2\u0178\u0179\3")
        buf.write("\2\2\2\u0179P\3\2\2\2\u017a\u017c\t\4\2\2\u017b\u017d")
        buf.write("\t\5\2\2\u017c\u017b\3\2\2\2\u017d\u017e\3\2\2\2\u017e")
        buf.write("\u017c\3\2\2\2\u017e\u017f\3\2\2\2\u017fR\3\2\2\2\u0180")
        buf.write("\u0181\7a\2\2\u0181T\3\2\2\2\u0182\u0183\t\6\2\2\u0183")
        buf.write("V\3\2\2\2\u0184\u0185\t\7\2\2\u0185X\3\2\2\2\u0186\u0187")
        buf.write("\t\b\2\2\u0187Z\3\2\2\2\u0188\u0189\t\t\2\2\u0189\\\3")
        buf.write("\2\2\2\u018a\u018b\t\n\2\2\u018b^\3\2\2\2\u018c\u018d")
        buf.write("\t\13\2\2\u018d`\3\2\2\2\u018e\u018f\t\f\2\2\u018fb\3")
        buf.write("\2\2\2\u0190\u0191\t\r\2\2\u0191d\3\2\2\2\u0192\u0193")
        buf.write("\t\16\2\2\u0193f\3\2\2\2\u0194\u0195\t\17\2\2\u0195h\3")
        buf.write("\2\2\2\u0196\u0197\t\20\2\2\u0197j\3\2\2\2\u0198\u0199")
        buf.write("\t\21\2\2\u0199l\3\2\2\2\u019a\u019b\t\22\2\2\u019bn\3")
        buf.write("\2\2\2\u019c\u019d\t\23\2\2\u019dp\3\2\2\2\u019e\u019f")
        buf.write("\t\24\2\2\u019fr\3\2\2\2\u01a0\u01a1\t\25\2\2\u01a1t\3")
        buf.write("\2\2\2\u01a2\u01a3\t\26\2\2\u01a3v\3\2\2\2\u01a4\u01a5")
        buf.write("\t\27\2\2\u01a5x\3\2\2\2\u01a6\u01a7\t\30\2\2\u01a7z\3")
        buf.write("\2\2\2\u01a8\u01a9\t\31\2\2\u01a9|\3\2\2\2\u01aa\u01ab")
        buf.write("\t\32\2\2\u01ab~\3\2\2\2\u01ac\u01ad\t\33\2\2\u01ad\u0080")
        buf.write("\3\2\2\2\u01ae\u01af\t\34\2\2\u01af\u0082\3\2\2\2\u01b0")
        buf.write("\u01b1\t\35\2\2\u01b1\u0084\3\2\2\2\u01b2\u01b3\t\36\2")
        buf.write("\2\u01b3\u0086\3\2\2\2\u01b4\u01b5\t\37\2\2\u01b5\u0088")
        buf.write("\3\2\2\2\u01b6\u01b7\t \2\2\u01b7\u008a\3\2\2\2\7\2\u016d")
        buf.write("\u0172\u0178\u017e\3\b\2\2")
        return buf.getvalue()


class SQL_InterpreterLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    CREATE = 1
    TABLE = 2
    DROP = 3
    SHOW = 4
    TABLES = 5
    INSERT = 6
    INTO = 7
    VALUES = 8
    SELECT = 9
    FROM = 10
    WHERE = 11
    INTEGER = 12
    INT = 13
    SMALLINT = 14
    TINYINT = 15
    UNSIGNED = 16
    NUMERIC = 17
    NULL = 18
    STRING = 19
    VARCHAR = 20
    CHARVAR = 21
    CHAR = 22
    DATETIME = 23
    TIMESTAMP = 24
    BLOB = 25
    SUBTYPE = 26
    DECIMAL = 27
    YEAR = 28
    QUOTE = 29
    LPAREN = 30
    RPAREN = 31
    COMMA = 32
    SEMICOLON = 33
    EQUAL = 34
    DOUBLE_COLON = 35
    ASTERISK = 36
    SPACES = 37
    NUMBER = 38
    REAL = 39
    NAME = 40

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "','", "';'", "'='", "'::'", "'*'" ]

    symbolicNames = [ "<INVALID>",
            "CREATE", "TABLE", "DROP", "SHOW", "TABLES", "INSERT", "INTO", 
            "VALUES", "SELECT", "FROM", "WHERE", "INTEGER", "INT", "SMALLINT", 
            "TINYINT", "UNSIGNED", "NUMERIC", "NULL", "STRING", "VARCHAR", 
            "CHARVAR", "CHAR", "DATETIME", "TIMESTAMP", "BLOB", "SUBTYPE", 
            "DECIMAL", "YEAR", "QUOTE", "LPAREN", "RPAREN", "COMMA", "SEMICOLON", 
            "EQUAL", "DOUBLE_COLON", "ASTERISK", "SPACES", "NUMBER", "REAL", 
            "NAME" ]

    ruleNames = [ "CREATE", "TABLE", "DROP", "SHOW", "TABLES", "INSERT", 
                  "INTO", "VALUES", "SELECT", "FROM", "WHERE", "INTEGER", 
                  "INT", "SMALLINT", "TINYINT", "UNSIGNED", "NUMERIC", "NULL", 
                  "STRING", "VARCHAR", "CHARVAR", "CHAR", "DATETIME", "TIMESTAMP", 
                  "BLOB", "SUBTYPE", "DECIMAL", "YEAR", "QUOTE", "LPAREN", 
                  "RPAREN", "COMMA", "SEMICOLON", "EQUAL", "DOUBLE_COLON", 
                  "ASTERISK", "SPACES", "NUMBER", "REAL", "NAME", "UNDER", 
                  "DIGIT", "A", "B", "C", "D", "E", "F", "G", "H", "I", 
                  "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", 
                  "U", "V", "W", "X", "Y", "Z" ]

    grammarFileName = "SQL_Interpreter.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


