############################### question 1

def my_func(x1,x2,x3):
    mylist =[x1,x2,x3]
    for i in mylist:
        if type(i) == float:
            continue
        elif type(i) not in (float,int): 
            raise TypeError('None')
        else:
            raise TypeError('Error: parameters should be float')
            
    a = (x1+x2+x3)
    b = (x2+x3)
    
    if (x1+x2+x3) == 0:
         raise TypeError('Not a number – denominator equals zero')
    else:
        result = a*b*x3 / a 
        return result
   

##print(my_func(2.0,0.0,1.0))

################################# question 2


from itertools import islice

def revword(word):
    return word[::-1].lower()


def countword():
    with open('text.txt') as fhand:
        counter = dict()
        word = fhand.readline().rstrip()
        counter[word] = 1
        for line in islice(fhand,0,None):
            lineWords = line.rstrip().split()
            for i in lineWords:
                reverse = revword(i)
                if reverse == word:
                    counter[word] = counter[word] + 1
                else:
                    counter[word] = counter[word]
        result = counter.get(word)
        print("The number of appearance of the first word on the file is:",result)
    
countword()
  

