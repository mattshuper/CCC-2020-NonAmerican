input = [n for n in input()]
indicator = False
instructionList = []
stringList = []
turnList = []
count = 0

string = ""
state = ""
turn = []
finalTurn = ""

for element in input:
    
    

    if indicator == True:
        Num = False
        
        for x in range(0,10):
            if element == str(x):
                Num = True
                turn.append(element)
        if count + 1 == len(input):
            for x in turn:
                finalTurn += x
            turnList.append(int(finalTurn))
            finalTurn = ""
            turn = []
        if Num == False:
            for x in turn:
                finalTurn += x
            turnList.append(int(finalTurn))
            indicator = False
            finalTurn = ""
            turn = []
        

    if indicator == False:
        
        if element == "+" or element == "-":
            if element == "+":
                state = "tighten"
            if element == "-":
                state = "loosen"
            indicator = True
            stringList.append(string)
            instructionList.append(state)
            string = ""
            state = ""
        else:
            string += element
    count = count + 1
            


for x in range(0,len(stringList)):
    print(f"{stringList[x]} {instructionList[x]} {turnList[x]}")   
    
    


    

