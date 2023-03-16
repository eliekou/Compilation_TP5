import re
import time as time

#re_ion = re.compile("^ion")
re_ion = re.compile(r'[a-zA-Z]*tions$')

re_2 = re.compile(r'[a-zA-Z]*at[^irt]*$')

file1 = open("dictionary.txt",'r')

txt_file = file1

##global a

#a=0
matching_words = []
matching_words2 = []


def research(line):
    
    result = re_2.match(line)
    #result = re_2.match(line)

    
    if result:
        matching_words.append(line.strip())
        #print(a)
        #print(result)
        #print(result.group(0))
    
def research_2():
    
    with open("dictionary.txt","r") as dic_fr:
        for line in dic_fr:
            if re_ion.match(line):
                matching_words2.append(line.strip())   
        
    



####LECTURE DE FICHIERS EN PYTHON


"""
with open("dictionnary.text","r") as dic_fr:
    for line in dic_fr:
        if regex.match(line):
            matching_words.append(line.strip())"""




####
t=time.time()
while True:
    line = txt_file.readline()
    if not line:
        break

    research(line)
tdurée = time.time() - t

t1= time.time()
research_2()
tdurée2 = time.time()-t1

print(matching_words2)
print(matching_words)
print("LA durée du research 1 est ",tdurée)


print("LA durée du research 2 est ",tdurée2)
print(len(matching_words))
print(len(matching_words))

#close(file1)
#print(i)
#print(a)
