import os

import pytest


@pytest.fixture
def filename_block():
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
def filename_block_bad_checksum():
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
def filename_block_no_checksum():
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
def filename_block_bad_block_header():
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
def filename_block_data():
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
def filename_block_data_no_filename():
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


def resource_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "resources")
