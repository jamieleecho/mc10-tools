class C10Data:
    def __init__(
        self,
        filename,
        start_addr,
        load_addr,
        data,
        filetype,
        binary_mode,
        continuous_gap_flag,
    ):
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
    with open(path, "rb") as f:
        return c10_file_to_data(f.read())


def c10_file_to_data(data):
    """Given C10 data as a binary string, returns a C10Data object"""
    # strip initial leader
    ii = 0
    (ii, block_data, block_type) = skip_leader(data, ii)

    # read the initial block
    (ii, block_data, block_type) = read_block(data, ii)
    if block_type != 0x0:
        raise Exception(
            f"Unexpected block type {block_type} (expected 0) found at "
            f"{ii - len(block_data) + 1}"
        )
    (filename, filetype, binary_mode, continuous_gap_flag, start_addr, load_addr) = (
        parse_initial_block_data(block_data)
    )

    # Skip the padding
    (ii, block_data, block_type) = skip_leader(data, ii)

    # build up the data to return
    (ii, block_data, block_type) = read_block(data, ii)
    file_data = block_data
    while block_type != 0xFF:
        if block_type != 1:
            raise Exception(
                f"Unexpected block type {block_type} (expected 1) found at "
                f"{ii - len(block_data) + 1}"
            )
        (ii, block_data, block_type) = skip_leader(data, ii)
        (ii, block_data, block_type) = read_block(data, ii)
        file_data += block_data

    # return the data
    return C10Data(
        filename,
        start_addr,
        load_addr,
        file_data,
        filetype,
        binary_mode,
        continuous_gap_flag,
    )


def skip_leader(data, ii):
    """Skips data starting at ii until a non 0x55 char is found. Returns
    (new_ii, datai, 0x55)"""
    start_ii = ii
    while (ii < len(data)) and data[ii] == 0x55:
        ii = ii + 1
    if ii >= len(data):
        raise EOFError(f"Found EOF at index {ii} in the file")
    return (ii, data[start_ii:ii], 0x55)


def read_block(data, ii):
    """Reads the block of data starting at ii, returns
    (new_ii, data_in_block, block_type)"""
    # find the initial file header
    if ii + 3 >= len(data):
        raise EOFError("Found EOF while scanning through the initial file header")
    if data[ii] != 0x3C:
        raise Exception(f"Did not find a file header at {ii}")
    block_type = data[ii + 1]
    size = data[ii + 2]
    ii = ii + 3

    # get the raw data
    if ii + size >= len(data):
        raise EOFError(f"Found EOF while loading {size} bytes of data at " f"{ii}")
    data_in_block = data[ii : ii + size]
    ii = ii + size

    # make sure the data passes the checksum
    verify_checksum(data, ii - size - 2, ii)

    return (ii + 1, data_in_block, block_type)


def verify_checksum(data, start_idx, end_idx):
    if end_idx >= len(data):
        raise EOFError(f"Found EOF at char {len(data) - 1} while scanning for checksum")
    checksum = sum(data[ii] for ii in range(start_idx, end_idx)) & 0xFF
    if checksum != data[end_idx]:
        raise Exception(
            f"Char at {end_idx} is {data[end_idx]}, but expecting {checksum}"
        )


def parse_initial_block_data(block_data):
    """returns (filename, filetype, binary_mode, continuous_gap_flag,
    start_addr, load_addr)"""
    # find the initial file header
    if len(block_data) != 0xF:
        raise Exception("Initial header has the wrong size")

    # get the filename
    filename = block_data[0:8]
    while len(filename) > 0 and filename[-1] == 0x00:
        filename = filename[:-1]
    if len(filename) == 0:
        raise Exception("No filename specified")

    # get the different file attributes
    filetype = block_data[8]
    binary_mode = block_data[9]
    continuous_gap_flag = block_data[10]

    # get the start and end addresses
    start_addr = (block_data[11] << 8) | block_data[12]
    load_addr = (block_data[13] << 8) | block_data[14]

    return (filename, filetype, binary_mode, continuous_gap_flag, start_addr, load_addr)


def c10data_to_c10file(c10data):
    """Creates the corresponding c10 file based on the c10data block"""
    output = bytearray()

    # Generate all of the initial header stuff
    output += generate_initial_leader()
    output += generate_initial_block_data(c10data)
    output += generate_secondary_leader()

    # Generate normal block
    ii = 0
    while ii < len(c10data.data):
        (block_data, ii) = generate_block_data(c10data.data, ii, 1)
        output += block_data
        if ii < len(c10data.data):
            output += generate_interblock_leader()

    # Generate the final block
    output += generate_final_block_leader()
    output += generate_block_data(bytearray(), 0, 0xFF)[0]
    output += b"\xff"
    padding = (((len(output) + 4095) // 4096) * 4096) - len(output)
    output += b"\0" * padding

    return output


def generate_initial_leader():
    """Generates the initial leader that starts all c10 files"""
    return b"\x55" * 0x80


def generate_initial_block_data(c10data):
    """Generates the first block leader that starts all c10 files"""

    # put in the filename, make sure it is exactly 8 bytes
    initial_block = bytearray()
    initial_block += c10data.filename
    if len(initial_block) > 8:
        initial_block = initial_block[0:8]
    elif len(initial_block) < 8:
        initial_block += b"\0" * (8 - len(initial_block))
    # Note that filename = c10data.data[0:8]

    # put in different file flags
    initial_block.append(c10data.filetype)
    initial_block.append(c10data.binary_mode)
    initial_block.append(c10data.continuous_gap_flag)

    # put in the start and load addresses
    initial_block.append((c10data.start_addr >> 8) & 0xFF)
    initial_block.append(c10data.start_addr & 0xFF)
    initial_block.append((c10data.load_addr >> 8) & 0xFF)
    initial_block.append(c10data.load_addr & 0xFF)

    return generate_block_data(initial_block, 0, 0)[0]


def generate_secondary_leader():
    """Generates the secondary leader after the initial c10 block"""
    return b"\x55" * 0x81


def generate_block_data(data, index, blocktype):
    """Generates the largest block possible starting at index in data.
    returns (output, new_index) where output is the generated block and
    new_index points to where the next block in data would be extracted"""
    output = bytearray()
    output += b"\x3c"
    output.append(blocktype)
    sz = len(data) - index
    if sz > 0xFF:
        sz = 0xFF
    output.append(sz)
    output += data[index : index + sz]
    checksum = sum(output[1:]) & 0xFF
    output.append(checksum)
    return (output, index + sz)


def generate_interblock_leader():
    """Generates the leader between normal blocks"""
    return b"\x55" * 0x2


def generate_final_block_leader():
    """Generates the leader between the last normal block and the end block"""
    return b"\x55" * 0x3
