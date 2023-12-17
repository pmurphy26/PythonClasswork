'''
@date: 12/5/2023
@author: Peter Murphy
@PID: pmurphy26, HW 13 Final Project Group 26
@assignment: Option B final Project
'''

import hashlib, binascii
import time
import matplotlib.pyplot as plt
import itertools

def get_and_break_user_passwords(valid_passwords):
    '''
    Takes a user input for the password
    Users can enter sha256 of sha512 to set that to the hashing algorithm they wish to use or q to quit

    The program takes the user input and feeds it to the get_num_of_words_in_password function, which will 
    return the number of words in the inputted password or -1 if it's an invalid password. The inputted password and 
    the number of words are given as parameters to the dict_attack function, which returns the results for the
    time it took to crack and how many attempts it took to crack and stores them into the respective list that
    will then be accessed to get and display the appropriate data in the graph. The code at the end of the
    function creates and displays a graph and legend showing all the required data  
    '''
    recieving_input = True
    passwords = []
    time_to_crack_passwords = []
    attempts_to_crack_passwords = []
    hash_type_used = []
    hash_type = "sha256"
    print("The current hashing type is sha256, if you wish to change to sha512  enter sha512 for the password and viceversa.")
    while (recieving_input):
        inputted_password = input("Password: ")

        if inputted_password == "q":
            recieving_input = False
        elif inputted_password == "sha256":
            hash_type = "sha256"
            print("you are now using sha256 hashing")
        elif inputted_password == "sha512": 
            hash_type = "sha512"
            print("you are now using sha512 hashing")
        else: #if actual password is entered
            num_of_words = get_num_of_words_in_password(valid_passwords, inputted_password, 1)
            if num_of_words != -1:
                hashed_password = hash_password(inputted_password, hash_type)
                crack_stats = dict_attack(valid_passwords, hashed_password, num_of_words)
                if crack_stats[0] != -1: # if dict_attack was able to crack password
                    time_to_crack = crack_stats[0]
                    attempts_to_crack = crack_stats[1]
                    hash_type_used.append(crack_stats[2])
                    passwords.append(inputted_password)
                    time_to_crack_passwords.append(time_to_crack)
                    attempts_to_crack_passwords.append(attempts_to_crack)
                    print("the time it took to crack the password was " + str(time_to_crack) + " seconds.")
            else: 
                print("please enter a valid password")



    #Graph
    fig, ax = plt.subplots()
    ax.axis([0, len(passwords), 0, max(time_to_crack_passwords)])
    ax.set_ylabel('Time to Crack (Seconds)')
    ax.set_xlabel('Password Difficulty')
    ax.set_title("Dictionary Size: " + str(len(valid_passwords)))


    legend_strs = [] 
    for i, password in enumerate(passwords):
        plt.plot(i, time_to_crack_passwords[i], "C" + str(i) + "o")
        password_point = "(" + password + ", "  + str(time_to_crack_passwords[i]) + ", " + str(attempts_to_crack_passwords[i]) + ", " + str(hash_type_used[i]) + ")"
        legend_strs.append(password_point)
        #plt.text(i, time_to_crack_passwords[i], password)

    # Make legend
    pos = ax.get_position()
    ax.set_position([pos.x0, pos.y0, pos.width * 0.8, pos.height])
    ax.legend(legend_strs, loc='center right', bbox_to_anchor=(1.25, 0.5))

    plt.show()
    return 0

def read_valid_passwords(file_name):
    '''
    Reads all the lines from the dictionary and stores each line as a string in the list of passwords
    returns the list of valid passwords 
    '''
    content = open(file_name,"r")
    passwords = content.read().splitlines()
    return passwords

def hash_password(unhashed_password, hashing_type):
    '''
    Takes the unhashed password and hashing type and hashes the password using the given hashing type
    '''
    hashed_password = hashlib.pbkdf2_hmac(hashing_type, 
                                          unhashed_password.encode("utf-8"), "salt".encode("utf-8"), 200)
    return binascii.hexlify(hashed_password)

def get_num_of_words_in_password(valid_passwords, input, iteration):
    '''
    Recursive method that gets the number of words in an inputted password
    returns -1 if the inputted password is not valid
    '''
    for p in valid_passwords:
        if input.find(p) != -1:
            shortened_str = input.replace(p,"",1)
            if len(shortened_str) != 0: #still more words in the password
                ret_value = get_num_of_words_in_password(valid_passwords, shortened_str, iteration + 1)
                if ret_value != -1: 
                    '''
                    make sure that it ends well and doesn't accidentially remove wrong part
                    ex is how if the password it turtleturtle it will initially take out let 
                    and then turtle and will be left with tur on the first removal attempt through
                    '''
                    return ret_value 
            else: 
                return iteration

    return -1

def dict_attack(valid_passwords, hashed_password, num_of_words):
    '''
    Performs a dictionary attack based on the given list of valid passwords and the number of words used in the password

    checks the length of the hashed password to determine which type of hashing is being used. Then uses the number of words
    to create a list of all possible passwords before looping through it and checking each possible password.
    '''
    times_attempted = 0
    start_time = time.perf_counter()

    if len(str(hashed_password)) == 67:
        hash_type = "sha256"
    elif len(str(hashed_password)) == 131:
        hash_type = "sha512"
    else:
        return [-1, -1, "None"] 


    #create list of possible passwords using num_of_words
    possible_passwords = itertools.product(valid_passwords, repeat=num_of_words)
    
    #loop through and check all possible passwords
    for pos_pass in possible_passwords:
        possible_password = ""
        for word in list(pos_pass):
            possible_password += word
        times_attempted += 1
        hashed_possible_password = hash_password(possible_password, hash_type)
        if (hashed_possible_password == hashed_password):
            end_time = time.perf_counter()
            print("The password is " + possible_password + ", the number of attempts this took was " + str(times_attempted))
            time_required = end_time - start_time
            return [round(time_required, 4), times_attempted, hash_type]

    print("the password was not found, you probably entered an invalid password")
    return [-1,times_attempted, hash_type]


#code that is run that calls methods and effectively runs program
valid_passwords = read_valid_passwords("dict.txt")
get_and_break_user_passwords(valid_passwords)