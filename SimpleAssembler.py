import sys
reg={"R0" : "000" ,"R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110"}

opcode = {
"A" : {"add" : "10000" , "sub" : "10001" , "mul" : "10110" , "xor" : "11010" , "and" : "11100", "or":"11011"}, 
"B" : {"mov" : "10010" , "ls" : "11001","rs":"11000"}, 
"C" : {"mov" : "10011"  ,"div" : "10111" , "not" : "11101" , "cmp" : "11110"},
"D" : {"ld" : "10100" , "st" : "10101"},
"E" : {"jmp" : "11111" , "jlt" : "01100" , "jgt" : "01101" , "je" : "01111"},
"F" : {"hlt" : "01010"} 
}                  

error = 0 
variable = {}
label = {}
machineCodes = []
programCounter = 0




inst0=[i.split() for i in sys.stdin.readlines()]

instructions=inst0.copy()
inst=[]
for i in instructions:
    if i:
        inst.append(i)


if len(inst)>256:                 
    print("Memory Overflow")
    error=1

for i in variable:
    if(not check(i)):
        print("Line",i+1,"Invalid variable definition")
        error=1
    
for i in label:
    if(not check(i)):
        print("Line",i+1,"Invalid label definition")
        error=1

inst = variables(inst)
if error == 0 :
    inst = labels(inst)


for i in variable:
    if(not check(i)):
        print("Line",int(variable[i])-len(inst)+1,"Invalid variable definition")
        error=1
    
for i in label:
    if(not check(i)) and error==0:
        print("Line",int(label[i])+1+len(variable),"Invalid label definition")
        error=1
