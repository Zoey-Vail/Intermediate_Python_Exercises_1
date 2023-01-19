# Team members
# Ronnie Hampton
# Zoey Vail
# Michael
# Eli Huffman
# Quinn Harris

# Resources used: https://www.w3schools.com/python/python_try_except.asp

numList = []
i = 0
while i < 5:
    num = (input('Enter int #' + str(i + 1) + ": "))
    try:
        int(num)
        numList.append(int(num))
        i += 1
    except:
        print("Invalid input")
        
sum = 0
for i in numList:
    sum += i
print("sum: ", sum)
