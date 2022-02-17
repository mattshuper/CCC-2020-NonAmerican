# There will be one line of input which is a sequence of tuning instructions. Each tuning
# instruction will be a sequence of uppercase letters, followed by a plus sign (+) or minus
# sign (-), followed by a positive integer. There will be at least one instruction and at least
# one letter per instruction. Also, each uppercase letter will appear at most once.


input = input()
count = 0
looping = True
instructionList = []

while looping == True:
    instruction = ""
    number = False
    while number == False:
        for x in range(count,len(input)):
            instruction += input[x]
            count += 1
            print(instruction)
            for i in range(0,10):
                if input[x] == str(i):
                    number = True
                    break
            if number == True:
                break
            
    instructionList.append(instruction)
    if count >= len(input):
        looping = False



print(instructionList)



