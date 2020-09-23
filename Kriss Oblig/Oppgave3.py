#Oppgave 3

# -- A --
my_list = ["H", "I", "O", "F"]
my_string1 = "H:I:O:F"
my_string2 = "HIOF"

def listToString(s):  
    str1 = ""  
    for ele in my_list:  
        str1 += ele   
    return str1   

print(listToString(my_list))  

# -- B --
def Convert(my_string1): 
    li = list(my_string1.split(":")) 
    return li 
print(Convert(my_string1)) 

# -- C --
res = []
res[:] = my_string2
print(str(res))