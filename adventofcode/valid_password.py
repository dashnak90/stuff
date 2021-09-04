with open('text', 'r') as s:
    count=0
    for i in s:

        line=i.split()
        b,e=line[0].split('-')

        if int(b) <= line[2].count(line[1][0]) <= int(e):
            count+=1 

    print(count)


with open('text', 'r') as s:
    count=0
    for i in s:


        line=i.split()
        b,e=line[0].split('-')
        if (line[2][int(b)-1]==line[1][0] or line[2][int(e)-1]==line[1][0]) and not (line[2][int(b)-1]==line[1][0] and line[2][int(e)-1]==line[1][0]):
            count+=1


    print(count)