# Team members
# Ronnie Hampton
# Zoey Vail
# Michael
# Eli Huffman
# Quinn Harris

word = input("Enter a word: ").lower()
print(word)
myDict = dict()
for i in range(len(word)):
    count = 0
    r = i + 1
    for r in range(len(word)):
        if word[i] == word[r]:
            count += 1
    myDict[word[i]] = count
print(myDict)