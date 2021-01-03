import csv_management

def create_bingo(bingo_code, bingo_len, bingo_size):
    val = {
        'endpoint': 'init',
        'code': bingo_code,
        'bingo_len': bingo_len,
        'bingo_size': bingo_size
    }
    return val