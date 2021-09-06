with open('text', 'r') as s:
    s=s.read()
    s=[i for i in s.split('\n')]
#    print(s)
#    print(len(s[0]), len(s))
    i,j=0,0
    tree=0
#    print(len(s)-2)

    while i!=len(s)-2:  #322
        i+=1
        j+=3
#        print('coord',i,j%len(s[0]))
#        print(s[i][j%len(s[0])])   
        if s[i][j%len(s[0])]=='#':
            tree+=1
    print(tree)
