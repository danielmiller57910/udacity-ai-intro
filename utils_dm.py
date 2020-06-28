from string import ascii_letters

def string_to_grid():
    grid_columns = get_grid_columns()
    grid_rows = get_grid_rows() 
    return True

def get_grid_columns():
    return [i for i in range(1, 10)]

def get_grid_rows():
    return [ascii_letters[ascii_letters.index('A') + i] for i in range(0, 9)]