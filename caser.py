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
    for result in results:
        for digit in digits:
            first_lvl_replace = result.replace('x', str(digit))
            
            counter_digits = list(digits)
            counter_digits.remove(digit)
            for counter_digit in counter_digits:
                second_lvl_replace = first_lvl_replace.replace('o', str(counter_digit))
                counts.append(second_lvl_replace)
        
    #return results
    return len(counts), results

#print((caser(5)))
##print((caser(5)[1]))
##print((caser(5)[2]))
print (caser(4))

##dig = list(range(10))
##asd = 5
##dig.remove(asd)
##print (dig)

##stringer = 'xxxoox'
##digg = range(5)
##for i in digg:
##    new = stringer.replace('x',str(i))
##    print (new)
