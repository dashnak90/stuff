with open('text', 'r') as s:
    s=s.read().split()
    s=[int(i) for i in s]

    s.sort()
    for i in range(len(s)-2):
        j=i+1
        h=len(s)-1
        while j<h:
            if s[i]+s[j]+s[h]==2020:
                
                print(s[i]*s[j]*[h])
                break
            elif s[i]+s[j]+s[h]<2020:
                j+=1
            elif s[i]+s[j]+s[h]>2020:
                h-=1


            
