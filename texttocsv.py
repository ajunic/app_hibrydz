import csv
import re

filename = "prueba.txt"
user_id = "15"
fecha="26/05/2021"
version = "1.5"

lines = []

with open(filename) as f:
    lines = f.readlines()

output = "file_"+user_id+fecha+"_"+version+".csv"
print(output)

dic = {
    "title": lines[0],
    "headers": lines[1].split('"')
}

o = open("output.txt","w")

contador = {}

for i in range(3,len(lines)-1):
    rows  = lines[i].split('\t')
    for j in range(len(rows)):
        if len(rows[j]) >0:

            rows[j] = re.sub('"',"",rows[j])
            rows[j] = re.sub('\t',"",rows[j])
            if j == 0:
                if not contador.get(rows[j]):
                    contador[rows[j]] = 0                
                contador[rows[j]] += 1
                o.write(rows[j])

            
            
    
    for j in range(len(rows)):
        x = str(rows[j] + ":"  + str(len(rows[j])))
        print(type(x))
        
        o.write(x)
            
o.close()
            #print(rows[j]+",",end="")


print("/////////////")

for x,y in contador.items():
    print(x,":",y)   
   



"""  with open(output,"W",newline="") as csvfile:

 """
