#testInput = open('./testinput', 'r')
testInput = open('./input', 'r')
data = testInput.readlines()
sum = 0

#by line
for line in data:
    numberInString = ""
    #find first digit
    for char in line:
        if char.isdigit():
            numberInString += char
            break
    #find last digit
    for char in reversed(line):
        if char.isdigit():
            numberInString += char
            break
    print(numberInString)
    sum += int(numberInString)

print(sum)


