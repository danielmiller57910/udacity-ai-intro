
CHARACTER_LIST= "ABCDEFGHI"
NUMBER_LIST = "123456789"

def naked_queens():
    top_list, bottom_list = get_top_and_bottom_list([], [])
    return top_list, bottom_list


def get_top_and_bottom_list(top_list, bottom_list):
    for i in range(len(CHARACTER_LIST)):
        top_list.append(CHARACTER_LIST[i] + NUMBER_LIST[i])

    reversed_numbers = NUMBER_LIST[::-1]
    for i in range(len(CHARACTER_LIST)):
        bottom_list.append(CHARACTER_LIST[i] + reversed_numbers[i])
    return top_list, bottom_list
