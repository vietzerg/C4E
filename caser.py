import itertools as ite

def caser(length):
    digits = range(10)
    results = []
    for i in range(1, length-1):
        chain = i*"o" + (length-i)*"x"
        permu = ite.permutations(chain)
        #permu_str = []
        for p in list(set(permu)):
            p_str = "".join(list(p))
            if p_str.find('xx') != -1:
                results.append(p_str)

    count = 0
    counts = []
    counter_digits_combo_test = []
    for result in results:
        number_of_o = result.count('o')
        for digit in digits:
            first_lvl_replace = result.replace('x', str(digit))
            
            counter_digits = list(digits)
            counter_digits.remove(digit)
            counter_digits_combo = list(ite.product(counter_digits, repeat = number_of_o))
            counter_digits_combo_test.append(counter_digits_combo)
            for a_combo in counter_digits_combo:
                prepare_for_replace = first_lvl_replace
                for counter_digit in list(a_combo):
                    prepare_for_replace = prepare_for_replace.replace('o',str(counter_digit),1)
                counts.append(prepare_for_replace)
##            for counter_digit in counter_digits:
##                second_lvl_replace = first_lvl_replace.replace('o', str(counter_digit))
##                counts.append(second_lvl_replace)
        

    return len(counts)

#print((caser(5)))
##print((caser(5)[1]))
##print((caser(5)[2]))
print (caser(4))

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
