def stooge(a):
    n = len(a)
    if n == 2 and a[0] > a[1]:
#        print "swapping %d and %d" % (a[0],a[1])
        temp = a[0]
        a[0] = a[1]
        a[1] = temp
    elif n > 2:
        k = 2*n/3
        #print a[0:k-1]
        #print a[n-k:n-1]
        stooge(a[0:k-1])
        stooge(a[n-k:n-1])
        stooge(a[0:k])
    return a

a = [2,7,6,4,5]
print a
a = stooge(a)
print a
