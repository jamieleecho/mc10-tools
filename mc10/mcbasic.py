import re
from mc10 import c10
from .mclex import lexer as mclexer


# Maximum line length
BASIC_MAX_LINE_LEN = 127

# Maximum line number
BASIC_MAX_LINE_NUM = 63999

# Parses the line number and text
BASIC_LINE_REGEX = re.compile(rb"^ *(\d+) *(.*)$")

# Address where BASIC programs are loaded
BASIC_LOAD_ADDR = 0x4346

# Maps a token to a BASIC keyword
BASIC_KEYWORDS = [
    # 0x00 - 0x0f
    b"",  # EOL
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    # 0x10 - 0x1f
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    # 0x20 - 0x2f
    b" ",
    b"!",
    b'"',
    b"#",
    b"$",
    b"%",
    b"&",
    b"'",
    b"(",
    b")",
    b"*",
    b"+",
    b",",
    b"-",
    b".",
    b"/",
    # 0x30 - 0x3f
    b"0",
    b"1",
    b"2",
    b"3",
    b"4",
    b"5",
    b"6",
    b"7",
    b"8",
    b"9",
    b":",
    b";",
    b"<",
    b"=",
    b">",
    b"?",
    # 0x40 - 0x4f
    b"@",
    b"A",
    b"B",
    b"C",
    b"D",
    b"E",
    b"F",
    b"G",
    b"H",
    b"I",
    b"J",
    b"K",
    b"L",
    b"M",
    b"N",
    b"O",
    # 0x50 - 0x5f
    b"P",
    b"Q",
    b"R",
    b"S",
    b"T",
    b"U",
    b"V",
    b"W",
    b"X",
    b"Y",
    b"Z",
    b"[",
    b"\\",
    b"]",
    b"^",
    b"_",
    # 0x60 - 0x6f
    b"`",
    b"a",
    b"b",
    b"c",
    b"d",
    b"e",
    b"f",
    b"g",
    b"h",
    b"i",
    b"j",
    b"k",
    b"l",
    b"m",
    b"n",
    b"o",
    # 0x70 - 0x7f
    b"p",
    b"q",
    b"r",
    b"s",
    b"t",
    b"u",
    b"v",
    b"w",
    b"x",
    b"y",
    b"z",
    b"{",
    b"|",
    b"}",
    b"~",
    b"\x7f",
    # 0x80 - 0x8f
    b"FOR",
    b"GOTO",
    b"GOSUB",
    b"REM",
    b"IF",
    b"DATA",
    b"PRINT",
    b"ON",
    b"INPUT",
    b"END",
    b"NEXT",
    b"DIM",
    b"READ",
    b"LET",
    b"RUN",
    b"RESTORE",
    # 0x90 - 0x9f
    b"RETURN",
    b"STOP",
    b"POKE",
    b"CONT",
    b"LIST",
    b"CLEAR",
    b"NEW",
    b"CLOAD",
    b"CSAVE",
    b"LLIST",
    b"LPRINT",
    b"SET",
    b"RESET",
    b"CLS",
    b"SOUND",
    b"EXEC",
    # 0xa0 - 0xaf
    b"SKIPF",
    b"TAB(",
    b"TO",
    b"THEN",
    b"NOT",
    b"STEP",
    b"OFF",
    b"+",
    b"-",
    b"*",
    b"/",
    b"^",
    b"AND",
    b"OR",
    b">",
    b"=",
    # 0xb0 - 0xbf
    b"<",
    b"SGN",
    b"INT",
    b"ABS",
    b"!",
    b"RND",
    b"SQR",
    b"LOG",
    b"EXP",
    b"SIN",
    b"COS",
    b"TAN",
    b"PEEK",
    b"LEN",
    b"STR$",
    b"VAL",
    # 0xc0 - 0xcf
    b"ASC",
    b"CHR$",
    b"LEFT$",
    b"RIGHT$",
    b"MID$",
    b"POINT",
    b"VARPTR",
    b"INKEY$",
    b"MEM",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    # 0xd0 - 0xdf
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    # 0xe0 - 0xef
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    # 0xf0 - 0xff
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
    b"!",
]


BASIC_KEYWORD_TO_TOKEN = {
    keyword: token for token, keyword in enumerate(BASIC_KEYWORDS)
}
BASIC_KEYWORD_TO_TOKEN["!"] = 0x21


def c10data_to_bas(c10data):
    """Given a C10Data Object, returns a bstring containing the equivalent
    BASIC program"""
    if c10data.filetype != 0:
        raise Exception(
            f"{c10data.filename} has a filetype of" f"{c10data.filetype}, expected 0"
        )
    if c10data.binary_mode != 0:
        raise Exception(
            f"{c10data.filename} has a binary_mode of"
            f"{c10data.binary_mode}, expected 0"
        )
    if c10data.binary_mode != 0:
        raise Exception(
            f"{c10data.filename} has a continuous_gap_mode of"
            f"{c10data.continuous_gap_mode}, expected 0"
        )

    program = {}  # map a line number to the line
    ii = 0
    while ii < len(c10data.data):
        # Ignore the next line pointer unless it is 0x00
        if ii + 2 > len(c10data.data):
            raise EOFError(f"Found EOF while scanning for line number at {ii}")
        if c10data.data[ii] == 0x00 and c10data.data[ii + 1] == 0x00:
            break
        ii = ii + 2

        # Get the line number
        if ii + 2 > len(c10data.data):
            raise EOFError(f"Found EOF while scanning for line number at {ii}")
        line_number = (c10data.data[ii] << 8) + c10data.data[ii + 1]
        line = bytes(str(line_number), "iso-8859-1")
        line += b" "
        ii = ii + 2

        # Extract all of the tokens from the line
        while ii < len(c10data.data) and c10data.data[ii] != 0x00:
            char = c10data.data[ii]
            if char == 0x22:
                (strlit, ii) = parse_string_literal(c10data.data, ii)
                line += strlit
            else:
                line += token_to_keyword(c10data.data[ii])
                ii = ii + 1

        # Did we find the EOL character?
        if ii >= len(c10data.data):
            raise EOFError(f"Found EOF while scanning for EOL at {ii}")
        ii = ii + 1

        # Update the program
        program[line_number] = line

    # make sure the output is ordered
    ordered_program = (program[line_number] for line_number in sorted(program.keys()))

    return b"\n".join(ordered_program)


def token_to_keyword(token):
    return BASIC_KEYWORDS[token]


def parse_string_literal(data, index):
    """parses the string literal whose first double quote starts at index,
    returning (strilit, new_index) where strlit is the string literal
    including the starting and trailing double quote if there is one.
    new_index points to the char after the end of the string literal"""
    if index >= len(data):
        raise EOFError(f"Found EOF while scanning for string literal at {index}")
    if data[index] != 0x22:
        raise EOFError(f"Found {data[index]} at {index}, expected 0x22")
    index = index + 1

    # Extract all of the tokens from the line
    strlit = b'"'
    while index < len(data) and data[index] != 0x00 and data[index] != 0x22:
        strlit += bytes((data[index],))
        index = index + 1

    if index >= len(data):
        raise EOFError(f"Found EOF while scanning for end of string literal at {index}")
    if data[index] == 0x00:
        return strlit, index
    strlit += b'"'
    return strlit, index + 1


def bas_to_c10(program, filename):
    """given a BASIC program as a byte string, returns the corresponding C10
    file as a byte string"""
    tokenized_program = tokenize_bas(program, BASIC_LOAD_ADDR)
    c10data = c10.C10Data(
        filename, BASIC_LOAD_ADDR, BASIC_LOAD_ADDR, tokenized_program, 0x0, 0x0, 0x0
    )
    return c10.c10data_to_c10file(c10data)


def tokenize_bas(program, address):
    """tokenizes program which is an iso-8859-1 byte encoding of an mc-10
    BASIC program so that the program can be stored at address. Returns
    the tokenized program stored as a byte string"""
    program = program.replace(b"\r\n", b"\n")
    program = program.replace(b"\r", b"\n")
    program_lines = program.split(b"\n")
    tokens = b""
    for line, program_line in enumerate(program_lines):
        (line_tokens, address) = tokenize_bas_line(program_line, address, line + 1)
        tokens += line_tokens

    tokens += b"\0\0"
    return tokens


def tokenize_bas_line(bas_line, address, line_num):
    """tokenizes bas_line which is an iso-8859-1 byte encoding of an mc-10
    BASIC program line without the trailing newline character. line_num is
    the line number of bas_line in the file (not the BASIC line number).
    Returns the tokenized line as a byte string with the terminating null
    character and address + len(tokenized_line)"""
    (bas_line, bas_line_num) = normalize_bas_line(bas_line, line_num)
    if bas_line_num is None:
        return (b"", address)

    # tokenize the line
    bas_line_str = bas_line.decode("iso-8859-1")
    mclexer.input(bas_line_str)
    tokens = bytearray()
    tokens.append((bas_line_num >> 8) & 0xFF)
    tokens.append(bas_line_num & 0xFF)
    use_alt_punctuation = False
    while True:
        token = mclexer.token()
        if not token:
            break
        val = bytes(token.value, "iso-8859-1")
        if token.type == "KEYWORD":
            use_alt_punctuation = True
            if val.startswith(b"TAB"):
                keyword = b"TAB("
                rhs = b""
            elif val.startswith(b"REM"):
                keyword = b"REM"
                rhs = val[3:]
            elif val.startswith(b"DATA"):
                keyword = b"DATA"
                rhs = val[4:]
            else:
                keyword = val
                rhs = b""

            if keyword not in BASIC_KEYWORD_TO_TOKEN:
                raise Exception(f"{line_num}: {val} is an unknown keyword")
            tokenid = BASIC_KEYWORD_TO_TOKEN[keyword]
            tokens.append(tokenid)
            tokens += rhs
        elif token.type == "IDENTIFIER":
            use_alt_punctuation = True
            tokens += val
        elif token.type == "NUMBER":
            val = val.replace(b"-", bytes((BASIC_KEYWORD_TO_TOKEN[b"-"],)))
            val = val.replace(b"+", bytes((BASIC_KEYWORD_TO_TOKEN[b"+"],)))
            tokens += val
        elif token.type == "STRING":
            tokens += val
            if len(val) <= 1 or val[-1] != b'"'[0]:
                tokens += b'"'
        elif token.type == "PUNCTUATION":
            tokens += val
        elif token.type == "SPECIAL":
            tokenid = BASIC_KEYWORD_TO_TOKEN[val] if use_alt_punctuation else val[0]
            if tokenid is None:
                raise Exception(f"{line_num}: {val} is an unknown keyword")
            tokens.append(tokenid)
        elif token.type == "WHITESPACE":
            tokens += b" "
        else:
            raise Exception(f"{line_num}: {token.type} is an unknown token")

    # prepend the next address bytes
    next_address = address + len(tokens) + 3
    tokens[0:0] = ((next_address >> 8) & 0xFF, next_address & 0xFF)
    tokens.append(0)

    return (tokens, next_address)


def normalize_bas_line(bas_line, line_num):
    """canonicalizes bas_line to how the mc-10 would represent the line.
    bas_line is an iso-8859-1 byte encoding without a trailing newline
    character. Returns a pair with a version of bas_line without its
    line number and the line number as an integer. The returned bas_line
    will be left stripped and removes any space between TAB and (. Raises when
    the line is too long or the line number is invalid on a non blank line"""

    # Left strip the line - if it is blank, there is no more work to do
    bas_line = bas_line.lstrip()
    if bas_line == b"":
        return (bas_line, None)

    # Extract and check the line number
    match = BASIC_LINE_REGEX.match(bas_line)
    if not match:
        raise Exception(f"{line_num}: line does not start with a number.")
    bas_line_num = int(match[1])
    if bas_line_num > BASIC_MAX_LINE_NUM:
        raise Exception(f"{line_num}: {bas_line_num} > {BASIC_MAX_LINE_LEN}")

    # Canonicalize the line and check to make sure the line is not too long.
    # Note that this is not completely correct because of the way that TAB
    # ( should canonicalize # to TAB(. We will live with the slight wrongness
    # here though
    bas_line = match[2]
    if len(bas_line) > BASIC_MAX_LINE_LEN:
        raise Exception(
            f"{line_num}: the canonicalized line has too many characters "
            f"{len(bas_line)} > {BASIC_MAX_LINE_LEN}"
        )

    return (bas_line, bas_line_num)
