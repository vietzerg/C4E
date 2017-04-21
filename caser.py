import itertools as ite
import collections

##astr = 'aabbaa'
##z = set('aaaa')
##print (astr[0:int((len(astr)/2))])
##print (check_symmetry(astr))

# CHECK IF THE STRING IS SYMMETRIC (RIGHT-LEFT FLIP-ABLE)
def check_symmetry(string):
    if len(string) % 2 == 0:
        if len(set(string[0:int((len(string)/2))])) == 1 and len(set(string[int((len(string)/2)):])) == 1 and set(string[0:int((len(string)/2))]) != set(string[int((len(string)/2)):]):
            return True
        else:
            return False
    else:
        return False

#print (check_symmetry(astr))

# RETURN A LIST OF DUPLICATED ITEMS IN A LIST CONTAINING TUPLES WITH KEYS (CAN BE DUPLICATIONS) AND VALUES
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

##zzz = [(1,"a"),(2,"b"),(1,"z"),(1,"d"),(2,"k"),(3,"k")]
##for key, value in get_duplicate(zzz).items():
##    if len(value) > 1:
##        print ((key, value))
#print (get_duplicate(zzz))

# CONVERT A RESULT STRING INTO ITS DOPPELGANGER, FOR EXAMPLE: xxxoox => oooxxo
# I AM MAKING THIS BECAUSE THE PROGRAM IS MAKING DUPLICATES OTHER THAN THE SYMMETRIC ONES
def converter(stringer):
    source = {'x':'o', 'o':'x'}
    list_char = list(stringer)
    new_list = [ source[char] for char in list_char ]
    return "".join(new_list)

print (converter('xxxoox'))

def caser(length):
    digits = range(10)
    results = []
    for i in range(0, length-1):
        chain = i*"o" + (length-i)*"x"
        permu = ite.permutations(chain)
        for p in list(set(permu)):
            p_str = "".join(list(p))
            if p_str.find('xx') != -1:
                results.append(p_str)

    total_case_count = 0
    repeat_cases_count = 0
    counts = []
    repeat_cases = []
    for result in results:
        converter(result)
        number_of_o = result.count('o')
        for digit in digits:
            #all_x_replace = result.replace('x', str(digit))
            
            counter_digits = list(digits)
            counter_digits.remove(digit)
            counter_digits_combo = list(ite.product(counter_digits, repeat = number_of_o))
            for a_combo in counter_digits_combo:
                prepare_for_replace = result.replace('x', str(digit))
                for counter_digit in list(a_combo):
                    prepare_for_replace = prepare_for_replace.replace('o',str(counter_digit),1)
                #yield prepare_for_replace
                if check_symmetry(prepare_for_replace):
                    repeat_cases_count += 1
                    repeat_cases.append(prepare_for_replace)
                counts.append((prepare_for_replace, a_combo))
                #counts.append(prepare_for_replace)
                total_case_count += 1
                

    #return len(set(counts))
    return get_duplicate(counts)
    #return len(set(counts))

#print((caser(5)))
##print((caser(5)[1]))
##print((caser(5)[2]))
#print (caser(4))
#print (caser(7))
##for i in caser(5):
##    print (i)

##import time
##start_time = time.time()
##(caser(5))
##print("--- %s seconds ---" % (time.time() - start_time))

##dig = list(range(10))
##asd = 5
##dig.remove(asd)
##print (dig)

##stringer = 'xxxoox'
##digg = range(9)
##while stringer.find('x') != -1:
##    for i in digg:
##        new = stringer.replace('x',str(i),1)    
##for i in digg:
##    new = stringer.replace('x',str(i))
##    print (new)

##pool = list(ite.product(digg,repeat=2))
##print ((list(pool))[1])
##for a in list((list(pool))[1]):
##    stringer = stringer.replace('o',str(a),1)
##print (stringer)
