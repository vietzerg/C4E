##2:40PM April 21, 2017:
##
##I gave up trying. I wished to explore the possibility of creating a counter program that executes without storing all the cases in one list, because the execution
##time is so long.. and additionally I supposed that using a counter should reduce that required time.
##
##In the exploration, I managed to define a number of helper functions to aid the process of defining a duplicated case, and they worked all right.
##
##Eventhough I am not completely satisfied with my work so far, I am relieved that I have made this far.
##
##FOR ME IN THE FUTURE, IF YOU SEE THIS AGAIN, REMEMBER YOU HAD A TIME TRYING DAY AND NIGHT TO SOLVE SUCH A PROBLEM. JUST REMEMBER SO.

#_____________________________________________________________________________________________________________________________________________________________________________________

##THE ORIGINAL QUESTION IS: HOW MANY CAR PLATES IDs (IN THIS FORMAT: xxx-YYYY) ARE THERE SUCH THAT xxx ARE 3 CONSECUTIVE REPEATED LETTERS AND IN YYYY THERE ARE AT LEAST 2 CONSECUTIVE
##REPEATED DIGITS?
##
##IN THIS FILE I JUST DEALT WITH THE SECOND "HALF" OF THE PROBLEM: AT LEAST 2 CONSECUTIVE REPEATED DIGITS IN YYYY.

#_____________________________________________________________________________________________________________________________________________________________________________________

import itertools as ite
import collections

# CHECK IF THE STRING IS SYMMETRIC (RIGHT-LEFT FLIP-ABLE)
def check_symmetry(string):
    if len(string) % 2 == 0:
        if len(set(string[0:int((len(string)/2))])) == 1 and len(set(string[int((len(string)/2)):])) == 1 and set(string[0:int((len(string)/2))]) != set(string[int((len(string)/2)):]):
            return True
        else:
            return False
    else:
        return False

# PRINT ELEMENTS IN A LIST OF DUPLICATED ITEMS IN A LIST CONTAINING TUPLES WITH KEYS (CAN BE DUPLICATIONS) AND VALUES
# THIS IS JUST FOR TESTING PROCEDURE, NOT TO INCLUDE IN THE MAIN PROGRAM
# FOR EXAMPLE, [(1,"a"),(2,"b"),(1,"z"),(1,"d"),(2,"k"),(3,"k")]
def get_duplicate(a_list):
    d = collections.defaultdict(list)
    for k, v in a_list:
        d[k].append(v)
    for key, value in d.items():
        if len(value) > 1:
            print((key,value))
    return

# CONVERT A RESULT STRING INTO ITS DOPPELGANGER, FOR EXAMPLE: xxxoox => oooxxo
# I AM MAKING THIS BECAUSE THE PROGRAM IS MAKING DUPLICATES OTHER THAN THE SYMMETRIC ONES. THIS IS WHERE IT GETS INTRIGUING.
def converter(stringer):
    source = {'x':'o', 'o':'x'}
    list_char = list(stringer)
    new_list = [ source[char] for char in list_char ]
    return "".join(new_list)

# NOW INTO THE MAIN PROBLEM.
def caser(length):
    digits = range(10)
    results = []

    # First I try to find all possible forms of the numbers before assembling digits to the positions.
    
    for i in range(0, length-1):
        chain = i*"o" + (length-i)*"x"
        permu = ite.permutations(chain)
        for p in list(set(permu)):
            p_str = "".join(list(p))
            if p_str.find('xx') != -1:
                results.append(p_str)

    counts = []
    for result in results:
        converter(result)
        number_of_o = result.count('o')
        for digit in digits:            
            counter_digits = list(digits)
            counter_digits.remove(digit)
            counter_digits_combo = list(ite.product(counter_digits, repeat = number_of_o))

            # This generates all possible combos from the remaining 9 digits for the "o" positions
            
            for a_combo in counter_digits_combo:

            # Accessing a particular combo to assemble it into the "o" positions
            
                prepare_for_replace = result.replace('x', str(digit))

                # First I need to replace/lock the "x" positions
                
                for counter_digit in list(a_combo):
                    prepare_for_replace = prepare_for_replace.replace('o',str(counter_digit),1)
                counts.append(prepare_for_replace)
    return (set(counts))
                    
##                if check_symmetry(prepare_for_replace):
##                    repeat_cases_count += 1
##                    repeat_cases.append(prepare_for_replace)
                #counts.append((prepare_for_replace, a_combo))

##ACTUALLY THE ABOVE COMMENT LINES ARE NOT NECESSARY ANYMORE, BECAUSE I RETURN THE SET OF THE counts list, WHICH REMOVES ALL THE DUPLICATES ANYWAY. BUT I STILL WANT TO KEEP THEM HERE,
##IN CASE SOMETHING COMES UP.

##TESTING PROGRAM EXECUTION TIME
##import time
##start_time = time.time()
##(caser(5))
##print("--- %s seconds ---" % (time.time() - start_time))
