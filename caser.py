import itertools as ite

def caser(length):
    digits = range(10)
    result = []
    for i in range(1, length-1):
        str_o, str_x = i*"o", (length-i)*"x"
        #print (str_o)
        #print (str_x)
        #chain = ite.chain(str_o, str_x)
        chain = str_o + str_x
        permu = ite.permutations(chain)
        permu_str = []
        for p in list(set(permu)):
            p_str = "".join(list(p))
            if p_str.find('xx') != -1:
                permu_str.append(p_str)
##        permu_str = [ "".join(list(p)) for p in list(set(permu)) ]
##        for stri in permu_str:
##            if stri.find("xx") == -1:
##                permu_str.remove(stri)
        result.append(permu_str)
    return result
print((caser(5)[0]))
print((caser(5)[1]))
