"""
@date: 9/25/2023
@author: Peter Murphy
@PID: 906503650
@assignment: HW6 - Recursion
@note: Do NOT alter the function headers that are well documented
"""
def sum_digits(number: int) -> int:
    """ Sums each digit of a number together using recursion
    @param number: an integer whose digits will be summed
    @return: the sum of all digits in the number
    """
    number = abs(number)
    if number / 10 < 1:
        return number
    return number % 10 + sum_digits(int(number / 10))


def is_diff_two(values: list, diff: int) -> bool:
    """ Checks if there are two elements within a list that have a specific
    difference between them using recursion
    @param values: The list of integer values to be searched
    @param diff: The difference value between two elements to find
    @return: True if there are two elements in values with a difference of diff,
    otherwise False
    """
    return check_list(values, diff, 0, 1)

def check_list(values: list, diff: int, i: int, j: int):
    ''' loops through the list using recursive calls and checks the values at 
    index i and index j to see if there is a way to make it so that the difference 
    of the two is the given difference
    @param values: The list of integer values to be searched
    @param diff: The difference value between two elements to find
    @param i: The index for the first value in the list being used
    @param j: The index for the second value in the list being used
    @return: True if the difference of the two values accessed is the given difference
    False if index i is greater than or equal to the length of the list (looped through the whole list)
    Recursive call with values of i and j changed to be the next combination in the list
    '''
    
    if i >= len(values):
        return False
    elif j >= len(values):
        return check_list(values, diff, i + 1, i + 2)
    else: 
        if values[i] - diff == values[j] or values[i] + diff == values[j]:
            return True
        return check_list(values, diff, i, j + 1)
