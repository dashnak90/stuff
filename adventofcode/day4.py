import re
with open('text','r') as file:
    file=file.read()
    file=[re.sub('\n', ' ', i) for i in file.split('\n\n')]
    file=[i.split() for i in file]
#    print(file)

    dic_list=[]
#part A
    for i in file:
        d={}
        for j in i:
            j=j.split(':')
            d[j[0]]=j[1]
        if len(d)==8 :
            dic_list.append(d)
        if len(d)==7 and not 'cid' in d:
            dic_list.append(d)
#part B
            
#print(dic_list)    
invalid=[]       
for dic in dic_list:

    for key in dic:
        if key=='byr' and not(1920 <= int(dic[key]) <=2002 ):
            invalid.append(dic)
            break
          
        if key=='iyr' and not(2010 <= int(dic[key]) <=2020):
            invalid.append(dic)
            break

        if key=='eyr' and not(2020 <= int(dic[key]) <=2030):
            invalid.append(dic)
            break

        if key=='hgt' and (dic[key].endswith('cm') or dic[key].endswith('in')):
            if dic[key].endswith('cm') and not (150 <= int(dic[key][:-2]) <=193):
                    invalid.append(dic)
                    break
            if dic[key].endswith('in') and not (59 <= int(dic[key][:-2])  <=76):
                    invalid.append(dic)
                    break
        




        h='0123456789abcdef'
        if key=='hcl' and not(dic[key].startswith('#') and len(dic[key])==7 and set(list(dic[key][1:])).issubset(list(h))): 
            invalid.append(dic)
            break
 
        if key=='ecl' and dic[key] not in ["amb", "blu", "brn" ,"gry", "grn" ,"hzl", "oth"]:
            invalid.append(dic)
            break
        if key=='pid' and not(dic[key].isdigit() and len(dic[key])==9 ):
            invalid.append(dic)
            break        

diff=[i for i in dic_list if i not in invalid]
#print(diff)
print(len(dic_list))  
print(len(diff))  
s

