from mc10 import c10, mcbasic


def test_c10data_to_program(all_keywords_file):
    data = c10.c10_file_to_data(all_keywords_file)
    program = mcbasic.c10data_to_bas(data)
    print(program)


def test_tokenize_bas():
    tokens = mcbasic.tokenize_bas(b"10 FORAA=20TO1000STEP3\n" b"20 AA=.232E+3", 0x4000)
    print(tokens)
