import ply.lex as lex

# Microcolor Basic tokens
tokens = (
    "KEYWORD",
    "IDENTIFIER",
    "NUMBER",
    "STRING",
    "PUNCTUATION",
    "SPECIAL",
    "WHITESPACE",
)


t_KEYWORD = (
    r"TAB\s*\(|FOR|GOTO|GOSUB|REM.*$|IF|DATA[^:]*|PRINT|ON|INPUT|"
    r"END|NEXT|DIM|READ|LET|RUN|RESTORE|RETURN|STOP|POKE|CONT|LIST|"
    r"CLEAR|NEW|CLOAD|CSAVE|LLIST|LPRINT|SET|RESET|CLS|SOUND|EXEC|"
    r"SKIPF|TO|THEN|NOT|STEP|OFF|AND|OR|SGN|INT|ABS|USR|RND|SQR|LOG|"
    r"EXP|SIN|COS|TAN|PEEK|LEN|STR$|VAL|ASC|CHR\$|LEFT\$|RIGHT\$|"
    r"MID\$|POINT|VARPTR|INKEY\$|MEM"
)
t_IDENTIFIER = r"(?!" + t_KEYWORD + r")[A-Za-z][A-Z0-9a-z]*\$?"
t_NUMBER = r"[+-]?(\d+(\.\d*)?|\.\d+)([E][+-]?\d+)?"
t_STRING = r"\"[^\"]*(\"|$)"
t_PUNCTUATION = r"[\~\`\!\@\#\$\%\&\(\)\_\[\]\{\}\;\'\:\,\.\|\\]"
t_SPECIAL = r"[\^\*\+\-\=\<\>\?\/]"
t_WHITESPACE = r"\s"


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    return "!"


# Build the lexer
lexer = lex.lex()
