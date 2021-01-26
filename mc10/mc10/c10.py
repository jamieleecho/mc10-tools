BASIC_KEYWORDS = [
    # 0x00 - 0x0f
    b'',  # EOL
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',

    # 0x10 - 0x1f
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',

    # 0x20 - 0x2f
    b' ',
    b'!',
    b'"',
    b'#',
    b'$',
    b'%',
    b'&',
    b'\'',
    b'(',
    b')',
    b'*',
    b'+',
    b',',
    b'-',
    b'.',
    b'/',

    # 0x30 - 0x3f
    b'0',
    b'1',
    b'2',
    b'3',
    b'4',
    b'5',
    b'6',
    b'7',
    b'8',
    b'9',
    b':',
    b';',
    b'<',
    b'=',
    b'>',
    b'?',

    # 0x40 - 0x4f
    b'@',
    b'A',
    b'B',
    b'C',
    b'D',
    b'E',
    b'F',
    b'G',
    b'H',
    b'I',
    b'J',
    b'K',
    b'L',
    b'M',
    b'N',
    b'O',

    # 0x50 - 0x5f
    b'P',
    b'Q',
    b'R',
    b'S',
    b'T',
    b'U',
    b'V',
    b'W',
    b'X',
    b'Y',
    b'Z',
    b'[',
    b'\\',
    b']',
    b'^',
    b'_',

    # 0x60 - 0x6f
    b'`',
    b'a',
    b'b',
    b'c',
    b'd',
    b'e',
    b'f',
    b'g',
    b'h',
    b'i',
    b'j',
    b'k',
    b'l',
    b'm',
    b'n',
    b'o',

    # 0x70 - 0x7f
    b'p',
    b'q',
    b'r',
    b's',
    b't',
    b'u',
    b'v',
    b'w',
    b'x',
    b'y',
    b'z',
    b'{',
    b'|',
    b'}',
    b'~',
    b'\x7f',

    # 0x80 - 0x8f
    b'FOR',
    b'GOTO',
    b'GOSUB',
    b'REM',
    b'IF',
    b'DATA',
    b'PRINT',
    b'ON',
    b'INPUT',
    b'END',
    b'NEXT',
    b'DIM',
    b'READ',
    b'LET',
    b'RUN',
    b'RESTORE',

    # 0x90 - 0x9f
    b'RETURN',
    b'STOP',
    b'POKE',
    b'CONT',
    b'LIST',
    b'CLEAR',
    b'NEW',
    b'CLOAD',
    b'CSAVE',
    b'LLIST',
    b'LPRINT',
    b'SET',
    b'RESET',
    b'CLS',
    b'SOUND',
    b'!',

    # 0xa0 - 0xaf
    b'SKIPF',
    b'TAB(',
    b'TO',
    b'THEN',
    b'!',
    b'STEP',
    b'!',
    b'!',
    b'=',
    b'*',
    b'!',
    b'^',
    b'!',
    b'!',
    b'!',
    b'=',

    # 0xb0 - 0xbf
    b'!',
    b'SGN',
    b'INT',
    b'ABS',
    b'!',
    b'RND',
    b'SQR',
    b'LOG',
    b'EXP',
    b'SIN',
    b'COS',
    b'TAN',
    b'PEEK',
    b'LEN',
    b'STR',
    b'VAL',

    # 0xc0 - 0xcf
    b'ASC',
    b'CHR$',
    b'LEFT$',
    b'RIGHT$',
    b'MID$',
    b'POINT',
    b'!',
    b'INKEY$',
    b'MEM',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',

    # 0xd0 - 0xdf
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',

    # 0xe0 - 0xef
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',

    # 0xf0 - 0xff
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!',
    b'!'
]


class C10Data:
    def __init__(self, filename, start_addr, load_addr, data, filetype,
                 binary_mode, continuous_gap_flag):
        self._filename = filename
        self._start_addr = start_addr
        self._load_addr = load_addr
        self._data = data
        self._filetype = filetype
        self._binary_mode = binary_mode
        self._continuous_gap_flag = continuous_gap_flag

    @property
    def filename(self):
        return self._filename

    @property
    def start_addr(self):
        return self._start_addr

    @property
    def load_addr(self):
        return self._load_addr

    @property
    def data(self):
        return self._data

    @property
    def filetype(self):
        return self._filetype

    @property
    def binary_mode(self):
        return self._binary_mode

    @property
    def continuous_gap_flag(self):
        return self._continuous_gap_flag


def c10_path_to_data(path):
    """Given a C10 file path, returns a C10Data object"""
    with open(path, 'rb') as f:
        return c10_data_to_data(f.read())


def c10_data_to_data(data):
    """Given C10 data as a binary strong, returns a C10Data object"""
    # strip initial leader
    ii = 0
    (ii, block_data, block_type) = skip_leader(data, ii)

    # read the initial block
    (ii, block_data, block_type) = read_block(data, ii)
    if (block_type != 0x0):
        raise Exception(
            f'Unexpected block type {block_type} (expected 0) found at '
            f'{ii - len(block_data) + 1}')
    (filename, filetype, binary_mode, continuous_gap_flag, start_addr,
     load_addr) = parse_initial_block_data(block_data)

    # Skip the padding
    (ii, block_data, block_type) = skip_leader(data, ii)

    # build up the data to return
    (ii, block_data, block_type) = read_block(data, ii)
    file_data = block_data
    while block_type != 0xff:
        if block_type != 1:
            raise Exception(
                f'Unexpected block type {block_type} (expected 1) found at '
                f'{ii - len(block_data) + 1}')
        (ii, block_data, block_type) = skip_leader(data, ii)
        (ii, block_data, block_type) = read_block(data, ii)
        file_data += block_data

    # return the data
    return C10Data(filename, start_addr, load_addr, file_data, filetype,
                   binary_mode, continuous_gap_flag)


def skip_leader(data, ii):
    """Skips data starting at ii until a non 0x55 char is found. Returns
       (new_ii, datai, 0x55)"""
    start_ii = ii
    while((ii < len(data)) and data[ii] == 0x55):
        ii = ii + 1
    if (ii >= len(data)):
        raise EOFError(
            f'Found EOF at index {ii} in the file')
    return (ii, data[start_ii:ii], 0x55)


def read_block(data, ii):
    """Reads the block of data starting at ii, returns
       (new_ii, data_in_block, block_type)"""
    # find the initial file header
    if (ii + 3 >= len(data)):
        raise EOFError(
            'Found EOF while scanning through the initial file header')
    if (data[ii] != 0x3c):
        raise Exception(f'Did not find a file header at {ii}')
    block_type = data[ii + 1]
    size = data[ii + 2]
    ii = ii + 3

    # get the raw data
    if (ii + size >= len(data)):
        raise EOFError(f'Found EOF while loading {size} bytes of data at '
                       f'{ii}')
    data_in_block = data[ii:ii + size]
    ii = ii + size

    # make sure the data passes the checksum
    verify_checksum(data, ii - size - 2, ii)

    return (ii + 1, data_in_block, block_type)


def verify_checksum(data, start_idx, end_idx):
    if (end_idx >= len(data)):
        raise EOFError(
            f'Found EOF at char {len(data) - 1} while scanning for checksum')
    checksum = sum(data[ii] for ii in range(start_idx, end_idx)) & 0xff
    if (checksum != data[end_idx]):
        raise Exception(
            f'Char at {end_idx} is {data[end_idx]}, but expecting {checksum}')


def parse_initial_block_data(block_data):
    """returns (filename, filetype, binary_mode, continuous_gap_flag,
                start_addr, load_addr)"""
    # find the initial file header
    if (len(block_data) != 0xf):
        raise Exception('Initial header has the wrong size')

    # get the filename
    filename = block_data[0:8]
    while(len(filename) > 0 and filename[-1] == 0x00):
        filename = filename[:-1]
    if len(filename) == 0:
        raise Exception('No filename specified')

    # get the different file attributes
    filetype = block_data[8]
    binary_mode = block_data[9]
    continuous_gap_flag = block_data[10]

    # get the start and end addresses
    start_addr = (block_data[11] << 8) | block_data[12]
    load_addr = (block_data[13] << 8) | block_data[14]

    return (filename, filetype, binary_mode, continuous_gap_flag, start_addr,
            load_addr)


def c10data_to_bas(c10data):
    """Given a C10Data Object, returns a bstring containing the equivalent
    BASIC program"""
    if c10data.filetype != 0:
        raise Exception(f'{c10data.filename} has a filetype of'
                        f'{c10data.filetype}, expected 0')
    if c10data.binary_mode != 0:
        raise Exception(f'{c10data.filename} has a binary_mode of'
                        f'{c10data.binary_mode}, expected 0')
    if c10data.binary_mode != 0:
        raise Exception(f'{c10data.filename} has a continuous_gap_mode of'
                        f'{c10data.continuous_gap_mode}, expected 0')

    program = {}  # map a line number to the line
    ii = 0
    while ii < len(c10data.data):
        # Ignore the next line pointer unless it is 0x00
        if ii + 2 > len(c10data.data):
            raise EOFError(f'Found EOF while scanning for line number at {ii}')
        if c10data.data[ii] == 0x00 and c10data.data[ii + 1] == 0x00:
            break
        ii = ii + 2

        # Get the line number
        if ii + 2 > len(c10data.data):
            raise EOFError(f'Found EOF while scanning for line number at {ii}')
        line_number = (c10data.data[ii] << 8) + c10data.data[ii + 1]
        line = bytes(str(line_number), 'iso-8859-1')
        line += b' '
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
            raise EOFError(f'Found EOF while scanning for EOL at {ii}')
        ii = ii + 1

        # Update the program
        program[line_number] = line

    # make sure the output is ordered
    ordered_program = (
      program[line_number] for line_number in sorted(program.keys()))

    return b'\n'.join(ordered_program)


def token_to_keyword(token):
    return BASIC_KEYWORDS[token]


def parse_string_literal(data, index):
    """parses the string literal whose first douvle quote starts at index,
    returning (strilit, new_index) where strlit is the string literal
    including the starting and trailing double quote if there is one.
    new_index points to the char after the end of the string literal"""
    if index >= len(data):
        raise EOFError(
          f'Found EOF while scanning for string literal at {index}')
    if data[index] != 0x22:
        raise EOFError(f'Found {data[index]} at {index}, expected 0x22')
    index = index + 1

    # Extract all of the tokens from the line
    strlit = b'"'
    while index < len(data) and data[index] != 0x00 and data[index] != 0x22:
        strlit += bytes((data[index],))
        index = index + 1

    if index >= len(data):
        raise EOFError(
          f'Found EOF while scanning for end of string literal at {index}')
    if data[index] == 0x00:
        return strlit, index
    strlit += b'"'
    return strlit, index + 1
