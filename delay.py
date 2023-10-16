delay_int = open("delay.txt","r")
delay_int = delay_int.read()
delay_max=0
temp = ""
list_of_instructions=[]
for i in delay_int:
    if i != '\n':
        
        temp += i
        # print(temp)
    else:

        list_of_instructions.append(temp)
        temp=""

x = list(map(str,list_of_instructions[0].split()))

for i in x:
    if (int(i) > delay_max):
        delay_max = int(i)


