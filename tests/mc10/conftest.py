import os
import pytest


@pytest.fixture
def filename_block():
    return bytes([0x3c, 0x00, 0x0f, 0x42, 0x4c, 0x4f, 0x52, 0x4b, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x43, 0x46, 0x43, 0x46,
                  0x9b])


@pytest.fixture
def filename_block_bad_checksum():
    return bytes([0x3c, 0x00, 0x0f, 0x42, 0x4c, 0x4f, 0x52, 0x4b, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x43, 0x46, 0x43, 0x46,
                  0x9c])


@pytest.fixture
def filename_block_no_checksum():
    return bytes([0x3c, 0x00, 0x0f, 0x42, 0x4c, 0x4f, 0x52, 0x4b, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x43, 0x46, 0x43, 0x46])


@pytest.fixture
def filename_block_bad_block_header():
    return bytes([0xc3, 0x00, 0x0f, 0x42, 0x4c, 0x4f, 0x52, 0x4b, 0x00,
                  0x00, 0x00, 0x00, 0x00, 0x00, 0x43, 0x46, 0x43, 0x46,
                  0x9c])


@pytest.fixture
def filename_block_data():
    return bytes([0x42, 0x4c, 0x4f, 0x52, 0x4b, 0x00, 0x00, 0x00, 0x01,
                  0x02, 0x03, 0x01, 0x23, 0x45, 0x67])


@pytest.fixture
def filename_block_data_no_filename():
    return bytes([0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x01,
                  0x02, 0x03, 0x01, 0x23, 0x45, 0x67])


def resource_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        'resources')


def basic_c10_path():
    return os.path.join(resource_path(), 'blork.c10')


def basic_c10_data_path():
    return os.path.join(resource_path(), 'blork_data.bin')


@pytest.fixture
def basic_c10_file():
    with open(basic_c10_path(), 'rb') as f:
        return f.read()


@pytest.fixture
def all_keywords_file():
    with open(os.path.join(resource_path(), 'all-keywords.c10'),
              'rb') as f:
        return f.read()


@pytest.fixture
def basic_c10_file_bad_initial_block():
    with open(os.path.join(resource_path(), 'blork_bad_initial_block.c10'),
              'rb') as f:
        return f.read()


@pytest.fixture
def basic_c10_file_bad_block():
    with open(os.path.join(resource_path(), 'blork_bad_block.c10'),
              'rb') as f:
        return f.read()


@pytest.fixture
def basic_c10_data():
    with open(basic_c10_data_path(), 'rb') as f:
        return f.read()


def simple_bas_path():
    return os.path.join(resource_path(), 'simple.bas')


@pytest.fixture
def simple_bas_program():
    with open(simple_bas_path(), 'rb') as f:
        return f.read()
