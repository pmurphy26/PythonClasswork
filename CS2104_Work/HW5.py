
"""
@date: 9/19/2023
@author: Peter Murphy
@PID: 906503650
@assignment: HW 5 - Algorithm Efficiency 
@note: Do NOT alter the function headers that are well documented
"""
def max_difference(values: list) -> float:
    """ Efficiently finds the largest difference between any two elements in a list
    @param values: a list of numbers
    @return number for the largest difference between elements
    """
    # loops through the list once giving it O(n) complexity 
    smallest_num = values[0]
    largest_num = values[1]

    for num in values:
        if num < smallest_num:
            smallest_num = num
        elif num > largest_num:
            largest_num = num

    return largest_num - smallest_num

def sort_bivalued(values: list) -> list:
    """Efficiently sort a list of binary values
    @param values: a list of binary digits (0 or 1)
    @return: a list of binary numbers in ascending sort order
    """
    # has two pointers, one at beginning of list (i) and one at the end (j) 
    # that move towards the middle until they intersect or pass each other 
    # it loops throught the list a maximum time of once, giving it O(n) complexity
    i = 0
    k = j = len(values) - 1
    
    while i < j:
        while values[i] != 1 and i < j:
            i += 1
        while values[j] == 1 and i < j:
            j -= 1

        if i < j:
            values[i] = 0
            values[j] = 1
            print(values)
            j -= 1
            i += 1

    return values
