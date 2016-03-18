print "n  | Data"
print "---+-----------------"
x = [4, 9, 13, 5]
st = 0
def histogram (x,st):
    for n in x:
        for y in range(n):
            st = ""
            for col in range (n):
                st += "*"
        print "%4.1g   |  %4.2f" %(x,st)
histogram(x,st)
