# Generated from SQL_Interpreter.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SQL_InterpreterParser import SQL_InterpreterParser
else:
    from SQL_InterpreterParser import SQL_InterpreterParser

# This class defines a complete listener for a parse tree produced by SQL_InterpreterParser.
class SQL_InterpreterListener(ParseTreeListener):

    # Enter a parse tree produced by SQL_InterpreterParser#statements.
    def enterStatements(self, ctx:SQL_InterpreterParser.StatementsContext):
        pass

    # Exit a parse tree produced by SQL_InterpreterParser#statements.
    def exitStatements(self, ctx:SQL_InterpreterParser.StatementsContext):
        pass


    # Enter a parse tree produced by SQL_InterpreterParser#statement.
    def enterStatement(self, ctx:SQL_InterpreterParser.StatementContext):
        pass

    # Exit a parse tree produced by SQL_InterpreterParser#statement.
    def exitStatement(self, ctx:SQL_InterpreterParser.StatementContext):
        pass


    # Enter a parse tree produced by SQL_InterpreterParser#createStmt.
    def enterCreateStmt(self, ctx:SQL_InterpreterParser.CreateStmtContext):
        pass

    # Exit a parse tree produced by SQL_InterpreterParser#createStmt.
    def exitCreateStmt(self, ctx:SQL_InterpreterParser.CreateStmtContext):
        pass


    # Enter a parse tree produced by SQL_InterpreterParser#dropStmt.
    def enterDropStmt(self, ctx:SQL_InterpreterParser.DropStmtContext):
        pass

    # Exit a parse tree produced by SQL_InterpreterParser#dropStmt.
    def exitDropStmt(self, ctx:SQL_InterpreterParser.DropStmtContext):
        pass


    # Enter a parse tree produced by SQL_InterpreterParser#showStmt.
    def enterShowStmt(self, ctx:SQL_InterpreterParser.ShowStmtContext):
        pass

    # Exit a parse tree produced by SQL_InterpreterParser#showStmt.
    def exitShowStmt(self, ctx:SQL_InterpreterParser.ShowStmtContext):
        pass


    # Enter a parse tree produced by SQL_InterpreterParser#insertStmt.
    def enterInsertStmt(self, ctx:SQL_InterpreterParser.InsertStmtContext):
        pass

    # Exit a parse tree produced by SQL_InterpreterParser#insertStmt.
    def exitInsertStmt(self, ctx:SQL_InterpreterParser.InsertStmtContext):
        pass


    # Enter a parse tree produced by SQL_InterpreterParser#selectStmtFrom.
    def enterSelectStmtFrom(self, ctx:SQL_InterpreterParser.SelectStmtFromContext):
        pass

    # Exit a parse tree produced by SQL_InterpreterParser#selectStmtFrom.
    def exitSelectStmtFrom(self, ctx:SQL_InterpreterParser.SelectStmtFromContext):
        pass


    # Enter a parse tree produced by SQL_InterpreterParser#selectStmtStar.
    def enterSelectStmtStar(self, ctx:SQL_InterpreterParser.SelectStmtStarContext):
        pass

    # Exit a parse tree produced by SQL_InterpreterParser#selectStmtStar.
    def exitSelectStmtStar(self, ctx:SQL_InterpreterParser.SelectStmtStarContext):
        pass


    # Enter a parse tree produced by SQL_InterpreterParser#selectStmtWhere.
    def enterSelectStmtWhere(self, ctx:SQL_InterpreterParser.SelectStmtWhereContext):
        pass

    # Exit a parse tree produced by SQL_InterpreterParser#selectStmtWhere.
    def exitSelectStmtWhere(self, ctx:SQL_InterpreterParser.SelectStmtWhereContext):
        pass


    # Enter a parse tree produced by SQL_InterpreterParser#element.
    def enterElement(self, ctx:SQL_InterpreterParser.ElementContext):
        pass

    # Exit a parse tree produced by SQL_InterpreterParser#element.
    def exitElement(self, ctx:SQL_InterpreterParser.ElementContext):
        pass


    # Enter a parse tree produced by SQL_InterpreterParser#definition.
    def enterDefinition(self, ctx:SQL_InterpreterParser.DefinitionContext):
        pass

    # Exit a parse tree produced by SQL_InterpreterParser#definition.
    def exitDefinition(self, ctx:SQL_InterpreterParser.DefinitionContext):
        pass


    # Enter a parse tree produced by SQL_InterpreterParser#integerType.
    def enterIntegerType(self, ctx:SQL_InterpreterParser.IntegerTypeContext):
        pass

    # Exit a parse tree produced by SQL_InterpreterParser#integerType.
    def exitIntegerType(self, ctx:SQL_InterpreterParser.IntegerTypeContext):
        pass


    # Enter a parse tree produced by SQL_InterpreterParser#stringType.
    def enterStringType(self, ctx:SQL_InterpreterParser.StringTypeContext):
        pass

    # Exit a parse tree produced by SQL_InterpreterParser#stringType.
    def exitStringType(self, ctx:SQL_InterpreterParser.StringTypeContext):
        pass


    # Enter a parse tree produced by SQL_InterpreterParser#name.
    def enterName(self, ctx:SQL_InterpreterParser.NameContext):
        pass

    # Exit a parse tree produced by SQL_InterpreterParser#name.
    def exitName(self, ctx:SQL_InterpreterParser.NameContext):
        pass


    # Enter a parse tree produced by SQL_InterpreterParser#columnValue.
    def enterColumnValue(self, ctx:SQL_InterpreterParser.ColumnValueContext):
        pass

    # Exit a parse tree produced by SQL_InterpreterParser#columnValue.
    def exitColumnValue(self, ctx:SQL_InterpreterParser.ColumnValueContext):
        pass



del SQL_InterpreterParser