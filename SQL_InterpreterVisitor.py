# Generated from SQL_Interpreter.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SQL_InterpreterParser import SQL_InterpreterParser
else:
    from SQL_InterpreterParser import SQL_InterpreterParser

# This class defines a complete generic visitor for a parse tree produced by SQL_InterpreterParser.

my_db = {}
my_list = []
new_db = {}
class SQL_InterpreterVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SQL_InterpreterParser#statements.
    def visitStatements(self, ctx:SQL_InterpreterParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQL_InterpreterParser#statement.
    def visitStatement(self, ctx:SQL_InterpreterParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQL_InterpreterParser#createStmt.
    def visitCreateStmt(self, ctx:SQL_InterpreterParser.CreateStmtContext):
        numOfChildren = ctx.getChildCount()
        numOfEle = int((numOfChildren - 5) / 2)

        if ctx.tableName is None:
            return

        if (ctx.LPAREN()) is None:
            return

        if (ctx.RPAREN()) is None:
            return

        if (ctx.SEMICOLON()) is None:
            print("Missing SEMICOLON()")
            return

        if ctx.tableName is not None and len(ctx.element()) != 0 and ctx.element(
                0).definition() is not None and ctx.element(
            0).getText() is not None and ctx.SEMICOLON() is not None and ctx.LPAREN() is not None and ctx.RPAREN() is not None:

            numOfElements = len(ctx.element())

            elementList = []
            for x in range(numOfElements):
                elementList.append(ctx.element(x).getText())

            if len(elementList) != len(set(elementList)):
                print("Error! There are some duplicated columns in the table! Please create a table with different "
                      "columns!")
                return

            statementString = "createtable" + str(ctx.tableName.getText()) + "();"
            if ctx.getRuleContext().getText() == statementString:
                print("Error! There is no column in the table! Need at least one column!")
                return

            # if the table name already exists, print an error
            if ctx.tableName.getText() in my_db.keys():
                print("Error, the table name already exists. Please try another table name!")
                return
            else:
                # create a new table dict if there is at least one column
                my_db[ctx.tableName.getText()] = {}

                # NEW: push the table name (as a key) to the type_db dictionary
                new_db[ctx.tableName.getText()] = []

                print("The table <" + ctx.tableName.getText() + "> is successfully created")
                # print("column name & column type: ")
                for x in range(numOfElements):
                    tableName = ctx.name().getText()
                    thisKeyName = ctx.element(x).definition().name().getText()
                    thisKeyType = ctx.element(x).definition().type().getText()

                    # New: push the type to the list
                    new_db[tableName].append(thisKeyType)

                    my_db[tableName][thisKeyName] = []
                    if (thisKeyName is not None) and thisKeyType is not None:
                        pass
                        # print(thisKeyName + " " + thisKeyType)
                    else:
                        print("Error, the table has no columns")
        else:
            return
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQL_InterpreterParser#dropStmt.
    def visitDropStmt(self, ctx:SQL_InterpreterParser.DropStmtContext):
        if ctx.tableName is None:
            return

        if (ctx.SEMICOLON()) is None:
            return

            # if the table is not here, print an error
        if ctx.tableName.getText() in my_db.keys():
            del (my_db[ctx.tableName.getText()])
            print("The table <" + ctx.tableName.getText() + "> has been successfully dropped!")
        else:
            print("Error, the table does not exist!")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQL_InterpreterParser#showStmt.
    def visitShowStmt(self, ctx:SQL_InterpreterParser.ShowStmtContext):
        if (ctx.SEMICOLON()) is None:
            return;
        if not bool(my_db):
            print("Error, no table exists!")
        else:
            for key in my_db.keys():
                print("Table: " + key)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQL_InterpreterParser#insertStmt.
    def visitInsertStmt(self, ctx:SQL_InterpreterParser.InsertStmtContext):
        if ctx.tableName is None:
            return

        if ctx.INTO() is None:
            return

        if ctx.VALUES() is None:
            return

        if (ctx.LPAREN()) is None:
            return

        if (ctx.RPAREN) is None:
            return

        if (ctx.SEMICOLON()) is None:
            return
        if (ctx.tableName.getText()) not in my_db.keys():
            print("Error! The table does not exist!")
            return

        if ctx.tableName.getText() in my_db.keys() and ctx.tableName is not None and ctx.INTO() is not None and ctx.VALUES() is not None and (
                ctx.LPAREN()) is not None and (ctx.RPAREN) is not None and ctx.SEMICOLON() is not None:

            numOfElements = len(my_db[ctx.tableName.getText()])

            # should also get the elements types
            for x in range(numOfElements):
                tableName = ctx.name().getText()

            # use a list to store the keys of a table
            key_list = list(my_db[ctx.tableName.getText()])
            # try an example, print out a key
            my_key = key_list[0]
            tempnumOfValues = int((ctx.getChildCount() - 7))
            if tempnumOfValues == 1:
                numOfValues = 1
            else:
                numOfValues = int((tempnumOfValues + 1) / 2)
            for x in range(numOfValues):
                # New:
                if (new_db[ctx.tableName.getText()][x] == 'int' and str(
                        ctx.columnValue(x).getText()).isdigit() is True) or (
                        new_db[ctx.tableName.getText()][x] == 'string' and str(
                    ctx.columnValue(x).getText()).isdigit() is False):
                    pass

                else:
                    print("Error! Values and Types do not match!")
                    return

            if numOfElements == numOfValues:
                pass
            else:
                print("Error! The number of values does not match the number of elements in the table. Please check "
                      "the number of values!")
                return

            # Try to insert values into the elements per value per element of the table.
            for x in range(numOfElements):
                my_db[ctx.tableName.getText()][key_list[x]].append(ctx.columnValue(x).getText())
        else:
            return
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQL_InterpreterParser#selectStmtFrom.
    def visitSelectStmtFrom(self, ctx:SQL_InterpreterParser.SelectStmtFromContext):
        key_list = []
        if ctx.tableName.getText() in my_db.keys():

            key_list = list(my_db[ctx.tableName.getText()])
        else:
            print("Error! The table <" + ctx.tableName.getText() + "> does not exist!")
            return

        numOfColumns = int(((ctx.getChildCount() - 4) + 1) / 2)
        valueList = []
        numOfElements = 0

        newKeyListOfStatement = []
        for x in range(numOfColumns):
            if ctx.name(x).getText() in key_list:
                # push the key into a list
                newKeyListOfStatement.append(ctx.name(x).getText())
                print(ctx.name(x).getText(), end=" ")
                valueList = list(my_db[ctx.tableName.getText()][ctx.name(0).getText()])
                numOfElements = len(valueList)
            else:
                print("Error! The column <" + ctx.name(x).getText() + "> does not exist! ")
        print()
        for m in range(numOfElements):
            for n in range(numOfColumns):
                print(my_db[ctx.tableName.getText()][ctx.name(n).getText()][m], end=" ")
            print()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQL_InterpreterParser#selectStmtStar.
    def visitSelectStmtStar(self, ctx:SQL_InterpreterParser.SelectStmtStarContext):
        if ctx.tableName.getText() in my_db.keys():
            print("Show data for all columns of the table <" + ctx.tableName.getText() + ">")
        else:
            print("Error! The table <" + ctx.tableName.getText() + "> does not exist!")
            return

        for each_row in zip(*([i] + (j)
                              for i, j in my_db[ctx.tableName.getText()].items())):
            print(*each_row, " ")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQL_InterpreterParser#selectStmtWhere.
    def visitSelectStmtWhere(self, ctx:SQL_InterpreterParser.SelectStmtWhereContext):
        key_list = []
        numOfColumns = 0
        numOfColumnNames = 0

        if ctx.tableName.getText() in my_db.keys():
            print("Show rows of the table <" + ctx.tableName.getText() + ">" + " that matches the given filter:")
            # This list holds the key for the given table
            key_list = list(my_db[ctx.tableName.getText()])
        else:
            print("Error! The table does not exist!")
            return

        requestedValue = ctx.columnValue().getText()
        numOfColumnNames = len(ctx.name()) - 2
        # print(numOfColumnNames)

        for x in range(numOfColumnNames):
            if ctx.name(x).getText() not in key_list:
                print("Error! The column <" + str(ctx.name(x).getText()) + "> is not in the table!")
                return
        columnName = ctx.name(len(ctx.name()) - 1).getText()
        value_list = list(my_db[ctx.tableName.getText()][columnName])
        if requestedValue in value_list:  # get the index of the value in the value_list
            for x in range(len(value_list)):
                if value_list[x] == requestedValue:
                    print(" ")
                    for key in key_list:
                        print(my_db[ctx.tableName.getText()][key][x], end=" ")
            print(" ")
        else:
            print("Error! Cannot find the value in the table!")
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQL_InterpreterParser#element.
    def visitElement(self, ctx:SQL_InterpreterParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQL_InterpreterParser#definition.
    def visitDefinition(self, ctx:SQL_InterpreterParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQL_InterpreterParser#integerType.
    def visitIntegerType(self, ctx:SQL_InterpreterParser.IntegerTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQL_InterpreterParser#stringType.
    def visitStringType(self, ctx:SQL_InterpreterParser.StringTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQL_InterpreterParser#name.
    def visitName(self, ctx:SQL_InterpreterParser.NameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by SQL_InterpreterParser#columnValue.
    def visitColumnValue(self, ctx:SQL_InterpreterParser.ColumnValueContext):
        return self.visitChildren(ctx)



del SQL_InterpreterParser