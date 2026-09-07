from mc10 import c10, mcbasic


def test_c10data_to_program(all_keywords_file: bytes) -> None:
    data = c10.c10_file_to_data(all_keywords_file)
    program = mcbasic.c10data_to_bas(data)
    print(program)


def test_tokenize_bas() -> None:
    tokens = mcbasic.tokenize_bas(b"10 FORAA=20TO1000STEP3\n20 AA=.232E+3", 0x4000)
    print(tokens)


def test_usr_round_trip(basic_usr_c10: bytes) -> None:
    # Test that the USR function is tokenized and de-tokenized correctly.
    # Some BASIC round-trips normalize trailing whitespace/newline formatting,
    # so compare the canonicalized program text rather than the raw byte stream.
    c10_obj = c10.c10_file_to_data(basic_usr_c10)
    basic_prog = mcbasic.c10data_to_bas(c10_obj)
    assert b"USR" in basic_prog
    new_c10_data = mcbasic.bas_to_c10(basic_prog, basic_prog)
    new_basic_prog = mcbasic.c10data_to_bas(c10.c10_file_to_data(new_c10_data))
    assert new_basic_prog.strip() == basic_prog.strip()
