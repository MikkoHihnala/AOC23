from pprint import pprint
testInput = open('./input2', 'r')
data = testInput.readlines()
sum = 0

stringDigits = {
        "one"   : "o1e", 
        "two"   : "t2o",
        "three" : "t3e",
        "four"  : "f4r",
        "five"  : "f5e",
        "six"   : "s6x",
        "seven" : "s7n",
        "eight" : "e8t",
        "nine"  : "n9e" 
        }

#by line
for line in data:
    for key, value in stringDigits.items():
        line = line.replace(key, value)
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


