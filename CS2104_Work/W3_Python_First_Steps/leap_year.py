year = int(input('Enter a year: '))

if year % 400 == 0: 
    print('leap year')
elif year % 4 != 0: 
    print('NOT a leap year')
elif year % 100 != 0: 
    print('leap year')
else: 
    print('NOT a leap year')


def horners_method(polynomial, degree, x):
    value = 0
    while (degree >= 0): # process remaining 
        print("degree is: " + str(degree))
        value = polynomial[degree] + value * x
        degree -= 1

        print(value)
    return value


def max_subsequence_sum_3(values):
    size = len(values)
    max_sum = 0
    this_sum = 0
    j = 0
    while (j <= size -1):
        print("j is: " + str(j))
        this_sum = this_sum + values[j]
        print("this sum is: " + str(this_sum))
        if ( this_sum > max_sum ):
            max_sum = this_sum
        elif ( this_sum < 0 ):
            this_sum = 0
        j = j + 1

        print("this is: " + str(max_sum))
    return max_sum

def max_subsequence_sum_1(values):
    size = len(values)
    max_sum = 0
    i = 0
    while i < size:
        print("i is: " + str(i))
        j = i
        while j < size:
            print("j is: " + str(j))
            this_sum = 0
            k = i
            while k <= j:
                print("k is: " + str(k))
                this_sum = this_sum + values[k]
                print("this sum is: " + str(this_sum))
                k = k + 1
                if (this_sum > max_sum ):
                    max_sum = this_sum
                print("max sum is: " + str(max_sum))
            j = j + 1
        i= i + 1
    return(max_sum)

def max_subsequence_sum_2(values):
    size = len(values)
    max_sum = 0
    i = 0
    while i < size:
        print("i is: " + str(i))
        j = i
        this_sum = 0
        while j < size:
            print("j is: " + str(j))
            this_sum = this_sum + values[j]
            print("this sum is: " + str(this_sum))
            if (this_sum > max_sum ):
                max_sum = this_sum
            print("max sum is: " + str(max_sum))
            j = j + 1
        i= i + 1
    return(max_sum)

#horners_method([5, 0, -6, 3, 1], 4, -2)
max_subsequence_sum_3([5, -1, -6, 3, 7, -8])