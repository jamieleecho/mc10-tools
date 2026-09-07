import os

import pytest


@pytest.fixture
def filename_block() -> bytes:
    return bytes(
        [
            0x3C,
            0x00,
            0x0F,
            0x42,
            0x4C,
            0x4F,
            0x52,
            0x4B,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x43,
            0x46,
            0x43,
            0x46,
            0x9B,
        ]
    )


@pytest.fixture
def filename_block_bad_checksum() -> bytes:
    return bytes(
        [
            0x3C,
            0x00,
            0x0F,
            0x42,
            0x4C,
            0x4F,
            0x52,
            0x4B,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x43,
            0x46,
            0x43,
            0x46,
            0x9C,
        ]
    )


@pytest.fixture
def filename_block_no_checksum() -> bytes:
    return bytes(
        [
            0x3C,
            0x00,
            0x0F,
            0x42,
            0x4C,
            0x4F,
            0x52,
            0x4B,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x43,
            0x46,
            0x43,
            0x46,
        ]
    )


@pytest.fixture
def filename_block_bad_block_header() -> bytes:
    return bytes(
        [
            0xC3,
            0x00,
            0x0F,
            0x42,
            0x4C,
            0x4F,
            0x52,
            0x4B,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x43,
            0x46,
            0x43,
            0x46,
            0x9C,
        ]
    )


@pytest.fixture
def filename_block_data() -> bytes:
    return bytes(
        [
            0x42,
            0x4C,
            0x4F,
            0x52,
            0x4B,
            0x00,
            0x00,
            0x00,
            0x01,
            0x02,
            0x03,
            0x01,
            0x23,
            0x45,
            0x67,
        ]
    )


@pytest.fixture
def filename_block_data_no_filename() -> bytes:
    return bytes(
        [
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x00,
            0x01,
            0x02,
            0x03,
            0x01,
            0x23,
            0x45,
            0x67,
        ]
    )


def resource_path() -> str:
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources")


def basic_c10_path() -> str:
    return os.path.join(resource_path(), "blork.c10")


def basic_c10_data_path() -> str:
    return os.path.join(resource_path(), "blork_data.bin")


@pytest.fixture
def basic_c10_file() -> bytes:
    with open(basic_c10_path(), "rb") as f:
        return f.read()


@pytest.fixture
def all_keywords_file() -> bytes:
    with open(os.path.join(resource_path(), "all-keywords.c10"), "rb") as f:
        return f.read()


@pytest.fixture
def basic_c10_file_bad_initial_block() -> bytes:
    with open(os.path.join(resource_path(), "blork_bad_initial_block.c10"), "rb") as f:
        return f.read()


@pytest.fixture
def basic_c10_file_bad_block() -> bytes:
    with open(os.path.join(resource_path(), "blork_bad_block.c10"), "rb") as f:
        return f.read()


@pytest.fixture
def basic_c10_data() -> bytes:
    with open(basic_c10_data_path(), "rb") as f:
        return f.read()


def simple_bas_path() -> str:
    return os.path.join(resource_path(), "simple.bas")


@pytest.fixture
def simple_bas_program() -> bytes:
    with open(simple_bas_path(), "rb") as f:
        return f.read()


@pytest.fixture
def basic_usr_c10() -> bytes:
    with open(os.path.join(resource_path(), "basic_usr.c10"), "rb") as f:
        return f.read()
