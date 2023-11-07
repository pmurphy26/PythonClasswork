
"""
@date: 9/14/2023
@author: Peter Murphy
@PID: 906503650
@assignment: HW4 practicing algorithms
@note: Do NOT alter the function headers that are well documented,
Do put your hw answers in the spaces provided within function headers
"""
def log_base_2(number: float) -> str:
    """ Gives the approximate log base 2 calculation of the input number
    @param number: float to calculate on
    @precondition: number is > 0
    @return str: A string description of the approximate result
    parts i-iii from HW
    i. Work out the steps to figure out the 2 concrete examples of 256 and 81
    step by step and briefly explain your work and thinking(5pts)
        Given 256
        divide by 2, 128
        repeat until the number is less than 2
        128/2 = 64
        64/2 = 32
        32 / 2 = 16
        16 / 2 = 8
        8 / 2 = 4
        4 / 2 = 2
        2 / 2 = 1
        since we divided by two eight times, log2 256 = 8

        Given 81
        81 / 2 = 40.5
        40.5 / 2 = 20.25
        20.25 / 2 = 10.125
        10.125 / 2 = 5.0625
        5.0625 / 2 = 2.53125
        2.03125 / 2 = 1.265625
        since we divided by two six times, log2 81 is roughly equal to 6
        
    ii. Find and describe a pattern and attempt to generalize (5pts)
        We set a number equal to the float parameter
        Divide the number by 2, incrementing the counter by one each time
        when the number is less than or equal to two, the counter is the 
        final answer and then the string is generated as so:
        if the number equals 1 --> answer is a whole number, log answer is count
        if the number is not equal to 1 --> answer is not a whole number, log answer
        is between count and count + 1

    iii. Investigate and explain special cases to see if the pattern holds up
    (5pts)
        one of the preconditions is that the parameter is greater than 0. If the parameter 
        is less than or equal to 0, the program returns "the logarithm lies between 0 and 1"
    """
    num = number
    count = 0

    if number < 1: 
        num = 1
        while num > number:
            count -= 1
            num = (2 ** count)

        if num == number: #log is an exact number
            result = str(count) 
        else: #log is between two numbers
            result = "between " + str(count) + " and " + str(count + 1)
    else: 
        while num >= 2.0:
            num = num / 2
            count += 1
        
        if num != 1: #log is between two numbers
            result = "between " + str(count) + " and " + str(count + 1) 
        else: #log is an exact number
            result = str(count)

    return result

def reverse_list(aList: list) -> list:
    """Gives a list with the elements in reversed order
    @param aList: list input that's going to be reversed
    @return list: the reversed version of the input list
    parts i-iii from HW
    i. Work out the steps to figure out a concrete example and briefly explain
    your work and thinking(5pts)
        Given the array [1, 2, 3, 4, 5]
        we want to swap the first and last index [5, 2, 3, 4, 1]
        then swap the 1 and 3 index [5, 4, 3, 2, 1]
        since there is an odd number of indices we don't need to swap 3 because it is in the middle

    ii. Find and describe a pattern and attempt to generalize (5pts)
        Get the 0 and last index and swap them
        Get the next two indices in (1 and second to last index) and swap them
        repeat until you reach the length of the array / 2 index of the array (middle index)

    iii. Investigate and explain special cases to see if the pattern holds up
        One of the special cases is when an empty list is handed to the function
        the pattern holds up because the while loop never runs and the function returns the 
        empty list which is technically the reversed version of itself
    (5pts)
    """
    i = len(aList)

    while i > len(aList) / 2:
        temp = aList[i - 1]
        aList[i - 1] = aList[len(aList) - i]
        aList[len(aList) - i] = temp
        i-=1
    return aList


num = 1/7
print(log_base_2(num))