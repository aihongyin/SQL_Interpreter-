grammar SQL_Interpreter;

statements          : statement EOF
                    ;

statement           : createStmt
                    | dropStmt
                    | showStmt
                    | insertStmt
                    | selectStmtFrom
                    | selectStmtStar
                    | selectStmtWhere
                    ;

createStmt          : CREATE TABLE tableName=name
                        LPAREN element (COMMA element)* RPAREN
                        SEMICOLON
                    ;

dropStmt            : DROP TABLE tableName=name
                        SEMICOLON
                    ;

showStmt            : SHOW TABLES
                        SEMICOLON
                    ;

insertStmt          : INSERT INTO tableName=name VALUES
                        LPAREN columnValue (COMMA columnValue)* RPAREN
                        SEMICOLON
                    ;

selectStmtFrom      : SELECT name (COMMA name)* FROM tableName=name 
                        SEMICOLON
                    ;

selectStmtStar      : SELECT ASTERISK FROM tableName=name
                        SEMICOLON
                    ;

selectStmtWhere     : SELECT name (COMMA name)* FROM tableName=name WHERE name EQUAL columnValue
                        SEMICOLON
                    ;

element             : definition
                    ;

definition          : name type ;

type                : (INTEGER | INT) UNSIGNED?                                                     #integerType
                    | STRING                                                                          #stringType
                    ;

name                : NAME ;

columnValue         : QUOTE NAME QUOTE
                    | NUMBER
                    | REAL 
                    ;
                    
CREATE              : C R E A T E;
TABLE               : T A B L E;

DROP                : D R O P;

SHOW                : S H O W;
TABLES              : T A B L E S;

INSERT              : I N S E R T;
INTO                : I N T O;
VALUES              : V A L U E S;

SELECT              : S E L E C T;
FROM                : F R O M;
WHERE               : W H E R E;

INTEGER             : I N T E G E R;
INT                 : I N T;
SMALLINT            : S M A L L I N T;
TINYINT             : T I N Y I N T;
UNSIGNED            : U N S I G N E D;
NUMERIC             : N U M E R I C;
NULL                : N U L L;
STRING              : S T R I N G;
VARCHAR             : V A R C H A R;
CHARVAR             : C H A R A C T E R ' ' V A R Y I N G;
CHAR                : C H A R;
DATETIME            : D A T E T I M E;
TIMESTAMP           : T I M E S T A M P;
BLOB                : B L O B;
SUBTYPE             : S U B UNDER T Y P E;
DECIMAL             : D E C I M A L;
YEAR                : Y E A R;

QUOTE               : [`']; 
LPAREN              : '(';
RPAREN              : ')';
COMMA               : ',';
SEMICOLON           : ';';
EQUAL               : '=';
DOUBLE_COLON        : '::';
ASTERISK            : '*';

SPACES              : [ \t\r\n] -> skip;
    
NUMBER              : DIGIT+;
REAL                : DIGIT+ '.' DIGIT+;
    
NAME                : [a-z][a-z0-9_]+
                    ;
    
fragment UNDER      : '_';
    
fragment DIGIT      : [0-9];
    
fragment A          : [aA];
fragment B          : [bB];
fragment C          : [cC];
fragment D          : [dD];
fragment E          : [eE];
fragment F          : [fF];
fragment G          : [gG];
fragment H          : [hH];
fragment I          : [iI];
fragment J          : [jJ];
fragment K          : [kK];
fragment L          : [lL];
fragment M          : [mM];
fragment N          : [nN];
fragment O          : [oO];
fragment P          : [pP];
fragment Q          : [qQ];
fragment R          : [rR];
fragment S          : [sS];
fragment T          : [tT];
fragment U          : [uU];
fragment V          : [vV];
fragment W          : [wW];
fragment X          : [xX];
fragment Y          : [yY];
fragment Z          : [zZ];
