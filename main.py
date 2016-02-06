numOfDays = 3
numOfWorkers = 8



def comb(lista):
    if len(lista)==1:
        return [lista]
    else:
        #print "curr in: " + str(lista)
        smallercombs=comb(lista[0:-1])
        #print "smallercomb: " + str(smallercombs)
        biggercombs = []
        for smallercomb in smallercombs:
            for i in range(len(smallercomb)+1):
                biggercomb=smallercomb[:i]+[lista[-1]]+smallercomb[i:]
                biggercombs.append(biggercomb)
                #print biggercomb
        return biggercombs

combs = comb([1,2,3,4])
print combs
print len(combs)  
