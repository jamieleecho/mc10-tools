import conftest
import pytest

from mc10 import c10


def test_c10data():
    filename = b"HELLO"
    start = 0x1234
    load = 0x4321
    data = bytes([0x11, 0x12, 0x13])
    filetype = 0x25
    binary_mode = 0x23
    continuous_gap_flag = 0x24
    c10data = c10.C10Data(
        filename, start, load, data, filetype, binary_mode, continuous_gap_flag
    )
    assert c10data.filename == filename
    assert c10data.start_addr == start
    assert c10data.load_addr == load
    assert c10data.data == data
    assert c10data.filetype == filetype
    assert c10data.binary_mode == binary_mode
    assert c10data.continuous_gap_flag == continuous_gap_flag


def test_skip_leader():
    data = bytes([0x55, 0x55, 0x55, 0x20, 0x70, 0x55, 0x55])
    assert c10.skip_leader(data, 0) == (3, data[:3], 0x55)
    assert c10.skip_leader(data[3:], 0) == (0, b"", 0x55)
    with pytest.raises(EOFError) as err:
        c10.skip_leader(data[5:], 0)
    assert str(err.value) == "Found EOF at index 2 in the file"


def test_read_block(filename_block):
    (ii, block_data, block_type) = c10.read_block(filename_block, 0)
    assert ii == len(filename_block)
    assert block_data == filename_block[3:18]
    assert block_type == 0


def test_read_block_with_bad_checksum(filename_block_bad_checksum):
    with pytest.raises(Exception) as err:
        c10.read_block(filename_block_bad_checksum, 0)
    assert str(err.value) == "Char at 18 is 156, but expecting 155"


def test_read_block_with_no_checksum(filename_block_no_checksum):
    with pytest.raises(EOFError) as err:
        c10.read_block(filename_block_no_checksum, 0)
    assert str(err.value) == "Found EOF while loading 15 bytes of data at 3"


def test_read_block_bad_block_header(filename_block_bad_block_header):
    with pytest.raises(Exception) as err:
        c10.read_block(filename_block_bad_block_header, 0)
    assert str(err.value) == "Did not find a file header at 0"


def test_verify_checksum(filename_block):
    c10.verify_checksum(filename_block, 2, len(filename_block) - 1)
    c10.verify_checksum(filename_block + b"IGNOREME", 2, len(filename_block) - 1)


def test_verify_checksum_with_bad_checksum_1(filename_block_bad_checksum):
    with pytest.raises(Exception) as err:
        c10.verify_checksum(
            filename_block_bad_checksum, 2, len(filename_block_bad_checksum) - 1
        )
    assert str(err.value) == "Char at 18 is 156, but expecting 155"


def test_verify_checksum_with_bad_checksum_2(filename_block_no_checksum):
    with pytest.raises(EOFError) as err:
        c10.verify_checksum(
            filename_block_no_checksum, 2, len(filename_block_no_checksum)
        )
    assert str(err.value) == "Found EOF at char 17 while scanning for checksum"


def test_parse_initial_block_data_1(filename_block_data):
    (filename, filetype, binary_mode, continuous_gap_flag, start_addr, load_addr) = (
        c10.parse_initial_block_data(filename_block_data)
    )
    assert filename == b"BLORK"
    assert filetype == 1
    assert binary_mode == 2
    assert continuous_gap_flag == 3
    assert start_addr == 0x0123
    assert load_addr == 0x4567


def test_parse_initial_block_data_2(filename_block_data):
    with pytest.raises(Exception) as err:
        c10.parse_initial_block_data(filename_block_data + b" ")
    assert str(err.value) == "Initial header has the wrong size"


def test_parse_initial_block_data_no_filename(filename_block_data_no_filename):
    with pytest.raises(Exception) as err:
        c10.parse_initial_block_data(filename_block_data_no_filename)
    assert str(err.value) == "No filename specified"


def test_c10_file_to_data(basic_c10_file, basic_c10_data):
    data = c10.c10_file_to_data(basic_c10_file)
    assert data.filename == b"BLORK"
    assert data.start_addr == 0x4346
    assert data.load_addr == 0x4346
    assert data.filetype == 0x0
    assert data.binary_mode == 0x0
    assert data.continuous_gap_flag == 0x0
    assert data.data == basic_c10_data


def test_c10_path_to_data(basic_c10_data):
    data = c10.c10_path_to_data(conftest.basic_c10_path())
    assert data.filename == b"BLORK"
    assert data.start_addr == 0x4346
    assert data.load_addr == 0x4346
    assert data.filetype == 0x0
    assert data.binary_mode == 0x0
    assert data.continuous_gap_flag == 0x0
    assert data.data == basic_c10_data


def test_c10_file_to_data_bad_initial_block(basic_c10_file_bad_initial_block):
    with pytest.raises(Exception) as err:
        c10.c10_file_to_data(basic_c10_file_bad_initial_block)
    assert str(err.value) == "Unexpected block type 5 (expected 0) found at 133"


def test_c10_file_to_data_bad_block(basic_c10_file_bad_block):
    with pytest.raises(Exception) as err:
        c10.c10_file_to_data(basic_c10_file_bad_block)
    assert str(err.value) == "Unexpected block type 7 (expected 1) found at 803"
