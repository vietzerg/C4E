import itertools as ite

##astr = 'aabbaa'
##z = set('aaaa')
##print (astr[0:int((len(astr)/2))])
##print (check_symmetry(astr))

# CHECK IF THE STRING IS SYMMETRIC (RIGHT-LEFT FLIP-ABLE)
def check_symmetry(string):
    if len(string) % 2 == 0:
        if len(set(string[0:int((len(string)/2))])) == 1 and len(set(string[int((len(string)/2)):])) == 1:
            return True
        else:
            return False
    else:
        return False

#print (check_symmetry(astr))

def caser(length):
    digits = range(10)
    results = []
    for i in range(1, length-1):
        chain = i*"o" + (length-i)*"x"
        permu = ite.permutations(chain)
        for p in list(set(permu)):
            p_str = "".join(list(p))
            if p_str.find('xx') != -1:
                results.append(p_str)

    count = 0
    counts = []
    repeat_cases = []
    for result in results:
        number_of_o = result.count('o')
        for digit in digits:
            all_x_replace = result.replace('x', str(digit))
            
            counter_digits = list(digits)
            counter_digits.remove(digit)
            counter_digits_combo = list(ite.product(counter_digits, repeat = number_of_o))
            for a_combo in counter_digits_combo:
                prepare_for_replace = all_x_replace
                for counter_digit in list(a_combo):
                    prepare_for_replace = prepare_for_replace.replace('o',str(counter_digit),1)
                if check_symmetry(prepare_for_replace):
                    repeat_cases.append(prepare_for_replace)
                counts.append(prepare_for_replace)
                

    return len(set(counts)), (repeat_cases)

#print((caser(5)))
##print((caser(5)[1]))
##print((caser(5)[2]))
print (caser(5))

##dig = list(range(10))
##asd = 5
##dig.remove(asd)
##print (dig)

stringer = 'xxxoox'
digg = range(9)
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
