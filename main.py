import sys
from antlr4 import *
from SQL_InterpreterLexer import SQL_InterpreterLexer
from SQL_InterpreterListener import SQL_InterpreterListener
from SQL_InterpreterParser import SQL_InterpreterParser
from SQL_InterpreterVisitor import SQL_InterpreterVisitor


def main():
    print("Start your query, enter 'exit' to quit!")
    while 1:
        myInput = input('Enter your query: ')
        test = InputStream(myInput)
        if myInput == "exit":
            print("Exit the test!")
            return

        try:

            lexer = SQL_InterpreterLexer(test)
            stream = CommonTokenStream(lexer)
            parser = SQL_InterpreterParser(stream)
            tree = parser.statements()
            res = SQL_InterpreterVisitor().visitStatements(tree)

        except BaseException:
            print("Syntax error or illegal usage of the table! ")


if __name__ == '__main__':
    main()