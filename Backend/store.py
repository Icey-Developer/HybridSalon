test_string = "XS knotless braids(R650)"

def getint():
    
    # using List comprehension + isdigit() +split()
    # getting numbers from string 
    s = ''.join(x for x in test_string if x.isdigit())
    
    # print result
    print(int(s)+50)

getint()

