/* Generated By:JavaCC: Do not edit this line. ParserTokenManager.java */
import java.io.*;

/** Token Manager. */
public class ParserTokenManager implements ParserConstants
{

  /** Debug output. */
  public static  java.io.PrintStream debugStream = System.out;
  /** Set debug output. */
  public static  void setDebugStream(java.io.PrintStream ds) { debugStream = ds; }
private static final int jjStopStringLiteralDfa_0(int pos, long active0)
{
   switch (pos)
   {
      case 0:
         if ((active0 & 0x100000000004L) != 0L)
         {
            jjmatchedKind = 52;
            return 10;
         }
         if ((active0 & 0x218080000000L) != 0L)
            return 11;
         if ((active0 & 0x20e0000000000L) != 0L)
            return 9;
         if ((active0 & 0x9c077600000f0L) != 0L)
         {
            jjmatchedKind = 54;
            return 9;
         }
         return -1;
      case 1:
         if ((active0 & 0xbb2f720000094L) != 0L)
         {
            jjmatchedKind = 54;
            jjmatchedPos = 1;
            return 9;
         }
         if ((active0 & 0x4000c0000060L) != 0L)
            return 9;
         return -1;
      case 2:
         if ((active0 & 0x3b07300000010L) != 0L)
         {
            jjmatchedKind = 54;
            jjmatchedPos = 2;
            return 9;
         }
         if ((active0 & 0x8028420000084L) != 0L)
            return 9;
         return -1;
      case 3:
         if ((active0 & 0x2805000000010L) != 0L)
         {
            jjmatchedKind = 54;
            jjmatchedPos = 3;
            return 9;
         }
         if ((active0 & 0x1302300000000L) != 0L)
            return 9;
         return -1;
      case 4:
         if ((active0 & 0x805000000000L) != 0L)
         {
            jjmatchedKind = 54;
            jjmatchedPos = 4;
            return 9;
         }
         if ((active0 & 0x2000000000010L) != 0L)
            return 9;
         return -1;
      default :
         return -1;
   }
}
private static final int jjStartNfa_0(int pos, long active0)
{
   return jjMoveNfa_0(jjStopStringLiteralDfa_0(pos, active0), pos + 1);
}
static private int jjStopAtPos(int pos, int kind)
{
   jjmatchedKind = kind;
   jjmatchedPos = pos;
   return pos + 1;
}
static private int jjMoveStringLiteralDfa0_0()
{
   switch(curChar)
   {
      case 33:
         return jjStopAtPos(0, 35);
      case 38:
         return jjMoveStringLiteralDfa1_0(0x10000000L);
      case 40:
         return jjStopAtPos(0, 17);
      case 41:
         return jjStopAtPos(0, 18);
      case 42:
         return jjStopAtPos(0, 10);
      case 43:
         return jjStopAtPos(0, 8);
      case 44:
         return jjStopAtPos(0, 23);
      case 45:
         return jjStopAtPos(0, 9);
      case 46:
         return jjStopAtPos(0, 26);
      case 58:
         jjmatchedKind = 25;
         return jjMoveStringLiteralDfa1_0(0x8000000L);
      case 59:
         return jjStopAtPos(0, 24);
      case 60:
         jjmatchedKind = 13;
         return jjMoveStringLiteralDfa1_0(0x5000L);
      case 61:
         return jjStopAtPos(0, 11);
      case 62:
         jjmatchedKind = 15;
         return jjMoveStringLiteralDfa1_0(0x10000L);
      case 91:
         return jjStopAtPos(0, 19);
      case 93:
         return jjStopAtPos(0, 20);
      case 97:
         return jjMoveStringLiteralDfa1_0(0x4000000000L);
      case 98:
         jjmatchedKind = 42;
         return jjMoveStringLiteralDfa1_0(0x2020000000000L);
      case 99:
         return jjMoveStringLiteralDfa1_0(0x1000000000000L);
      case 100:
         return jjMoveStringLiteralDfa1_0(0x20L);
      case 101:
         return jjMoveStringLiteralDfa1_0(0x200000080L);
      case 102:
         jjmatchedKind = 40;
         return jjMoveStringLiteralDfa1_0(0x208080000000L);
      case 105:
         return jjMoveStringLiteralDfa1_0(0x400040000000L);
      case 110:
         return jjMoveStringLiteralDfa1_0(0x400000000L);
      case 111:
         return jjMoveStringLiteralDfa1_0(0x40L);
      case 112:
         return jjMoveStringLiteralDfa1_0(0x100000000004L);
      case 113:
         return jjStartNfaWithStates_0(0, 43, 9);
      case 114:
         return jjMoveStringLiteralDfa1_0(0x8801000000000L);
      case 115:
         return jjMoveStringLiteralDfa1_0(0x2000000000L);
      case 116:
         return jjMoveStringLiteralDfa1_0(0x100000000L);
      case 118:
         return jjMoveStringLiteralDfa1_0(0x20000000L);
      case 119:
         return jjMoveStringLiteralDfa1_0(0x10L);
      case 123:
         return jjStopAtPos(0, 21);
      case 124:
         return jjMoveStringLiteralDfa1_0(0x4000000000000L);
      case 125:
         return jjStopAtPos(0, 22);
      default :
         return jjMoveNfa_0(0, 0);
   }
}
static private int jjMoveStringLiteralDfa1_0(long active0)
{
   try { curChar = input_stream.readChar(); }
   catch(java.io.IOException e) {
      jjStopStringLiteralDfa_0(0, active0);
      return 1;
   }
   switch(curChar)
   {
      case 38:
         if ((active0 & 0x10000000L) != 0L)
            return jjStopAtPos(1, 28);
         break;
      case 61:
         if ((active0 & 0x4000L) != 0L)
            return jjStopAtPos(1, 14);
         else if ((active0 & 0x10000L) != 0L)
            return jjStopAtPos(1, 16);
         else if ((active0 & 0x8000000L) != 0L)
            return jjStopAtPos(1, 27);
         break;
      case 62:
         if ((active0 & 0x1000L) != 0L)
            return jjStopAtPos(1, 12);
         break;
      case 97:
         return jjMoveStringLiteralDfa2_0(active0, 0x9000020000004L);
      case 100:
         if ((active0 & 0x40L) != 0L)
            return jjStartNfaWithStates_0(1, 6, 9);
         break;
      case 101:
         return jjMoveStringLiteralDfa2_0(active0, 0x2801000000000L);
      case 102:
         if ((active0 & 0x40000000L) != 0L)
            return jjStartNfaWithStates_0(1, 30, 9);
         break;
      case 104:
         return jjMoveStringLiteralDfa2_0(active0, 0x100000010L);
      case 105:
         if ((active0 & 0x80000000L) != 0L)
            return jjStartNfaWithStates_0(1, 31, 9);
         break;
      case 107:
         return jjMoveStringLiteralDfa2_0(active0, 0x2000000000L);
      case 108:
         return jjMoveStringLiteralDfa2_0(active0, 0x200000000L);
      case 110:
         return jjMoveStringLiteralDfa2_0(active0, 0x80L);
      case 111:
         if ((active0 & 0x20L) != 0L)
            return jjStartNfaWithStates_0(1, 5, 9);
         return jjMoveStringLiteralDfa2_0(active0, 0x400000000L);
      case 114:
         return jjMoveStringLiteralDfa2_0(active0, 0x100000000000L);
      case 115:
         if ((active0 & 0x400000000000L) != 0L)
            return jjStartNfaWithStates_0(1, 46, 9);
         return jjMoveStringLiteralDfa2_0(active0, 0x4000000000L);
      case 117:
         return jjMoveStringLiteralDfa2_0(active0, 0x200000000000L);
      case 119:
         return jjMoveStringLiteralDfa2_0(active0, 0x28000000000L);
      case 124:
         if ((active0 & 0x4000000000000L) != 0L)
            return jjStopAtPos(1, 50);
         break;
      default :
         break;
   }
   return jjStartNfa_0(0, active0);
}
static private int jjMoveStringLiteralDfa2_0(long old0, long active0)
{
   if (((active0 &= old0)) == 0L)
      return jjStartNfa_0(0, old0);
   try { curChar = input_stream.readChar(); }
   catch(java.io.IOException e) {
      jjStopStringLiteralDfa_0(1, active0);
      return 2;
   }
   switch(curChar)
   {
      case 100:
         if ((active0 & 0x80L) != 0L)
            return jjStartNfaWithStates_0(2, 7, 9);
         else if ((active0 & 0x8000000000L) != 0L)
            return jjStartNfaWithStates_0(2, 39, 9);
         else if ((active0 & 0x20000000000L) != 0L)
            return jjStartNfaWithStates_0(2, 41, 9);
         break;
      case 101:
         return jjMoveStringLiteralDfa3_0(active0, 0x100000000L);
      case 103:
         return jjMoveStringLiteralDfa3_0(active0, 0x2000000000000L);
      case 105:
         return jjMoveStringLiteralDfa3_0(active0, 0x2000000010L);
      case 108:
         return jjMoveStringLiteralDfa3_0(active0, 0x1000000000000L);
      case 109:
         return jjMoveStringLiteralDfa3_0(active0, 0x1000000000L);
      case 110:
         return jjMoveStringLiteralDfa3_0(active0, 0x200000000000L);
      case 111:
         return jjMoveStringLiteralDfa3_0(active0, 0x100000000000L);
      case 112:
         if ((active0 & 0x400000000L) != 0L)
            return jjStartNfaWithStates_0(2, 34, 9);
         else if ((active0 & 0x8000000000000L) != 0L)
            return jjStartNfaWithStates_0(2, 51, 9);
         break;
      case 114:
         if ((active0 & 0x4L) != 0L)
            return jjStartNfaWithStates_0(2, 2, 9);
         else if ((active0 & 0x20000000L) != 0L)
            return jjStartNfaWithStates_0(2, 29, 9);
         break;
      case 115:
         return jjMoveStringLiteralDfa3_0(active0, 0x4200000000L);
      case 116:
         return jjMoveStringLiteralDfa3_0(active0, 0x800000000000L);
      default :
         break;
   }
   return jjStartNfa_0(1, active0);
}
static private int jjMoveStringLiteralDfa3_0(long old0, long active0)
{
   if (((active0 &= old0)) == 0L)
      return jjStartNfa_0(1, old0);
   try { curChar = input_stream.readChar(); }
   catch(java.io.IOException e) {
      jjStopStringLiteralDfa_0(2, active0);
      return 3;
   }
   switch(curChar)
   {
      case 99:
         if ((active0 & 0x100000000000L) != 0L)
            return jjStartNfaWithStates_0(3, 44, 9);
         else if ((active0 & 0x200000000000L) != 0L)
            return jjStartNfaWithStates_0(3, 45, 9);
         break;
      case 101:
         if ((active0 & 0x200000000L) != 0L)
            return jjStartNfaWithStates_0(3, 33, 9);
         return jjMoveStringLiteralDfa4_0(active0, 0x4000000000L);
      case 105:
         return jjMoveStringLiteralDfa4_0(active0, 0x2000000000000L);
      case 108:
         if ((active0 & 0x1000000000000L) != 0L)
            return jjStartNfaWithStates_0(3, 48, 9);
         return jjMoveStringLiteralDfa4_0(active0, 0x10L);
      case 110:
         if ((active0 & 0x100000000L) != 0L)
            return jjStartNfaWithStates_0(3, 32, 9);
         break;
      case 111:
         return jjMoveStringLiteralDfa4_0(active0, 0x1000000000L);
      case 112:
         if ((active0 & 0x2000000000L) != 0L)
            return jjStartNfaWithStates_0(3, 37, 9);
         break;
      case 117:
         return jjMoveStringLiteralDfa4_0(active0, 0x800000000000L);
      default :
         break;
   }
   return jjStartNfa_0(2, active0);
}
static private int jjMoveStringLiteralDfa4_0(long old0, long active0)
{
   if (((active0 &= old0)) == 0L)
      return jjStartNfa_0(2, old0);
   try { curChar = input_stream.readChar(); }
   catch(java.io.IOException e) {
      jjStopStringLiteralDfa_0(3, active0);
      return 4;
   }
   switch(curChar)
   {
      case 101:
         if ((active0 & 0x10L) != 0L)
            return jjStartNfaWithStates_0(4, 4, 9);
         break;
      case 110:
         if ((active0 & 0x2000000000000L) != 0L)
            return jjStartNfaWithStates_0(4, 49, 9);
         break;
      case 114:
         return jjMoveStringLiteralDfa5_0(active0, 0x804000000000L);
      case 118:
         return jjMoveStringLiteralDfa5_0(active0, 0x1000000000L);
      default :
         break;
   }
   return jjStartNfa_0(3, active0);
}
static private int jjMoveStringLiteralDfa5_0(long old0, long active0)
{
   if (((active0 &= old0)) == 0L)
      return jjStartNfa_0(3, old0);
   try { curChar = input_stream.readChar(); }
   catch(java.io.IOException e) {
      jjStopStringLiteralDfa_0(4, active0);
      return 5;
   }
   switch(curChar)
   {
      case 101:
         if ((active0 & 0x1000000000L) != 0L)
            return jjStartNfaWithStates_0(5, 36, 9);
         break;
      case 110:
         if ((active0 & 0x800000000000L) != 0L)
            return jjStartNfaWithStates_0(5, 47, 9);
         break;
      case 116:
         if ((active0 & 0x4000000000L) != 0L)
            return jjStartNfaWithStates_0(5, 38, 9);
         break;
      default :
         break;
   }
   return jjStartNfa_0(4, active0);
}
static private int jjStartNfaWithStates_0(int pos, int kind, int state)
{
   jjmatchedKind = kind;
   jjmatchedPos = pos;
   try { curChar = input_stream.readChar(); }
   catch(java.io.IOException e) { return pos + 1; }
   return jjMoveNfa_0(state, pos + 1);
}
static private int jjMoveNfa_0(int startState, int curPos)
{
   int startsAt = 0;
   jjnewStateCnt = 10;
   int i = 1;
   jjstateSet[0] = startState;
   int kind = 0x7fffffff;
   for (;;)
   {
      if (++jjround == 0x7fffffff)
         ReInitRounds();
      if (curChar < 64)
      {
         long l = 1L << curChar;
         do
         {
            switch(jjstateSet[--i])
            {
               case 11:
                  if ((0x3ff000000000000L & l) != 0L)
                  {
                     if (kind > 54)
                        kind = 54;
                     jjCheckNAdd(9);
                  }
                  if ((0x3ff000000000000L & l) != 0L)
                  {
                     if (kind > 53)
                        kind = 53;
                     jjCheckNAdd(7);
                  }
                  break;
               case 10:
                  if ((0x3ff000000000000L & l) != 0L)
                  {
                     if (kind > 54)
                        kind = 54;
                     jjCheckNAdd(9);
                  }
                  if ((0x3ff000000000000L & l) != 0L)
                  {
                     if (kind > 52)
                        kind = 52;
                     jjCheckNAdd(5);
                  }
                  break;
               case 0:
                  if ((0x3ff000000000000L & l) != 0L)
                  {
                     if (kind > 3)
                        kind = 3;
                  }
                  else if ((0x100002600L & l) != 0L)
                  {
                     if (kind > 1)
                        kind = 1;
                  }
                  if ((0x3fe000000000000L & l) != 0L)
                  {
                     if (kind > 3)
                        kind = 3;
                     jjCheckNAdd(3);
                  }
                  break;
               case 1:
                  if ((0x3ff000000000000L & l) != 0L && kind > 3)
                     kind = 3;
                  break;
               case 2:
                  if ((0x3fe000000000000L & l) == 0L)
                     break;
                  if (kind > 3)
                     kind = 3;
                  jjCheckNAdd(3);
                  break;
               case 3:
                  if ((0x3ff000000000000L & l) == 0L)
                     break;
                  if (kind > 3)
                     kind = 3;
                  jjCheckNAdd(3);
                  break;
               case 5:
                  if ((0x3ff000000000000L & l) == 0L)
                     break;
                  if (kind > 52)
                     kind = 52;
                  jjCheckNAdd(5);
                  break;
               case 7:
                  if ((0x3ff000000000000L & l) == 0L)
                     break;
                  if (kind > 53)
                     kind = 53;
                  jjCheckNAdd(7);
                  break;
               case 9:
                  if ((0x3ff000000000000L & l) == 0L)
                     break;
                  if (kind > 54)
                     kind = 54;
                  jjCheckNAdd(9);
                  break;
               default : break;
            }
         } while(i != startsAt);
      }
      else if (curChar < 128)
      {
         long l = 1L << (curChar & 077);
         do
         {
            switch(jjstateSet[--i])
            {
               case 11:
               case 9:
                  if ((0x7fffffe07fffffeL & l) == 0L)
                     break;
                  if (kind > 54)
                     kind = 54;
                  jjCheckNAdd(9);
                  break;
               case 10:
                  if ((0x7fffffe07fffffeL & l) == 0L)
                     break;
                  if (kind > 54)
                     kind = 54;
                  jjCheckNAdd(9);
                  break;
               case 0:
                  if ((0x7fffffe07fffffeL & l) != 0L)
                  {
                     if (kind > 54)
                        kind = 54;
                     jjCheckNAdd(9);
                  }
                  if (curChar == 102)
                  {
                     if (kind > 53)
                        kind = 53;
                     jjstateSet[jjnewStateCnt++] = 7;
                  }
                  else if (curChar == 112)
                  {
                     if (kind > 52)
                        kind = 52;
                     jjstateSet[jjnewStateCnt++] = 5;
                  }
                  break;
               case 4:
                  if (curChar != 112)
                     break;
                  if (kind > 52)
                     kind = 52;
                  jjstateSet[jjnewStateCnt++] = 5;
                  break;
               case 6:
                  if (curChar != 102)
                     break;
                  if (kind > 53)
                     kind = 53;
                  jjstateSet[jjnewStateCnt++] = 7;
                  break;
               case 8:
                  if ((0x7fffffe07fffffeL & l) == 0L)
                     break;
                  if (kind > 54)
                     kind = 54;
                  jjCheckNAdd(9);
                  break;
               default : break;
            }
         } while(i != startsAt);
      }
      else
      {
         int i2 = (curChar & 0xff) >> 6;
         long l2 = 1L << (curChar & 077);
         do
         {
            switch(jjstateSet[--i])
            {
               default : break;
            }
         } while(i != startsAt);
      }
      if (kind != 0x7fffffff)
      {
         jjmatchedKind = kind;
         jjmatchedPos = curPos;
         kind = 0x7fffffff;
      }
      ++curPos;
      if ((i = jjnewStateCnt) == (startsAt = 10 - (jjnewStateCnt = startsAt)))
         return curPos;
      try { curChar = input_stream.readChar(); }
      catch(java.io.IOException e) { return curPos; }
   }
}
static final int[] jjnextStates = {
};

/** Token literal values. */
public static final String[] jjstrLiteralImages = {
"", null, "\160\141\162", null, "\167\150\151\154\145", "\144\157", 
"\157\144", "\145\156\144", "\53", "\55", "\52", "\75", "\74\76", "\74", "\74\75", "\76", 
"\76\75", "\50", "\51", "\133", "\135", "\173", "\175", "\54", "\73", "\72", "\56", 
"\72\75", "\46\46", "\166\141\162", "\151\146", "\146\151", "\164\150\145\156", 
"\145\154\163\145", "\156\157\160", "\41", "\162\145\155\157\166\145", "\163\153\151\160", 
"\141\163\163\145\162\164", "\146\167\144", "\146", "\142\167\144", "\142", "\161", "\160\162\157\143", 
"\146\165\156\143", "\151\163", "\162\145\164\165\162\156", "\143\141\154\154", 
"\142\145\147\151\156", "\174\174", "\162\141\160", null, null, null, };

/** Lexer state names. */
public static final String[] lexStateNames = {
   "DEFAULT",
};
static final long[] jjtoToken = {
   0x7ffffffffffffdL, 
};
static final long[] jjtoSkip = {
   0x2L, 
};
static protected SimpleCharStream input_stream;
static private final int[] jjrounds = new int[10];
static private final int[] jjstateSet = new int[20];
static protected char curChar;
/** Constructor. */
public ParserTokenManager(SimpleCharStream stream){
   if (input_stream != null)
      throw new TokenMgrError("ERROR: Second call to constructor of static lexer. You must use ReInit() to initialize the static variables.", TokenMgrError.STATIC_LEXER_ERROR);
   input_stream = stream;
}

/** Constructor. */
public ParserTokenManager(SimpleCharStream stream, int lexState){
   this(stream);
   SwitchTo(lexState);
}

/** Reinitialise parser. */
static public void ReInit(SimpleCharStream stream)
{
   jjmatchedPos = jjnewStateCnt = 0;
   curLexState = defaultLexState;
   input_stream = stream;
   ReInitRounds();
}
static private void ReInitRounds()
{
   int i;
   jjround = 0x80000001;
   for (i = 10; i-- > 0;)
      jjrounds[i] = 0x80000000;
}

/** Reinitialise parser. */
static public void ReInit(SimpleCharStream stream, int lexState)
{
   ReInit(stream);
   SwitchTo(lexState);
}

/** Switch to specified lex state. */
static public void SwitchTo(int lexState)
{
   if (lexState >= 1 || lexState < 0)
      throw new TokenMgrError("Error: Ignoring invalid lexical state : " + lexState + ". State unchanged.", TokenMgrError.INVALID_LEXICAL_STATE);
   else
      curLexState = lexState;
}

static protected Token jjFillToken()
{
   final Token t;
   final String curTokenImage;
   final int beginLine;
   final int endLine;
   final int beginColumn;
   final int endColumn;
   String im = jjstrLiteralImages[jjmatchedKind];
   curTokenImage = (im == null) ? input_stream.GetImage() : im;
   beginLine = input_stream.getBeginLine();
   beginColumn = input_stream.getBeginColumn();
   endLine = input_stream.getEndLine();
   endColumn = input_stream.getEndColumn();
   t = Token.newToken(jjmatchedKind, curTokenImage);

   t.beginLine = beginLine;
   t.endLine = endLine;
   t.beginColumn = beginColumn;
   t.endColumn = endColumn;

   return t;
}

static int curLexState = 0;
static int defaultLexState = 0;
static int jjnewStateCnt;
static int jjround;
static int jjmatchedPos;
static int jjmatchedKind;

/** Get the next Token. */
public static Token getNextToken() 
{
  Token matchedToken;
  int curPos = 0;

  EOFLoop :
  for (;;)
  {
   try
   {
      curChar = input_stream.BeginToken();
   }
   catch(java.io.IOException e)
   {
      jjmatchedKind = 0;
      matchedToken = jjFillToken();
      return matchedToken;
   }

   jjmatchedKind = 0x7fffffff;
   jjmatchedPos = 0;
   curPos = jjMoveStringLiteralDfa0_0();
   if (jjmatchedKind != 0x7fffffff)
   {
      if (jjmatchedPos + 1 < curPos)
         input_stream.backup(curPos - jjmatchedPos - 1);
      if ((jjtoToken[jjmatchedKind >> 6] & (1L << (jjmatchedKind & 077))) != 0L)
      {
         matchedToken = jjFillToken();
         return matchedToken;
      }
      else
      {
         continue EOFLoop;
      }
   }
   int error_line = input_stream.getEndLine();
   int error_column = input_stream.getEndColumn();
   String error_after = null;
   boolean EOFSeen = false;
   try { input_stream.readChar(); input_stream.backup(1); }
   catch (java.io.IOException e1) {
      EOFSeen = true;
      error_after = curPos <= 1 ? "" : input_stream.GetImage();
      if (curChar == '\n' || curChar == '\r') {
         error_line++;
         error_column = 0;
      }
      else
         error_column++;
   }
   if (!EOFSeen) {
      input_stream.backup(1);
      error_after = curPos <= 1 ? "" : input_stream.GetImage();
   }
   throw new TokenMgrError(EOFSeen, curLexState, error_line, error_column, error_after, curChar, TokenMgrError.LEXICAL_ERROR);
  }
}

static private void jjCheckNAdd(int state)
{
   if (jjrounds[state] != jjround)
   {
      jjstateSet[jjnewStateCnt++] = state;
      jjrounds[state] = jjround;
   }
}
static private void jjAddStates(int start, int end)
{
   do {
      jjstateSet[jjnewStateCnt++] = jjnextStates[start];
   } while (start++ != end);
}
static private void jjCheckNAddTwoStates(int state1, int state2)
{
   jjCheckNAdd(state1);
   jjCheckNAdd(state2);
}

}