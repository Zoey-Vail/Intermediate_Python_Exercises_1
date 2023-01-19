# Team members
# Ronnie Hampton
# Zoey Vail
# Michael
# Eli Huffman
# Quinn HiListis

# Resources used: https://www.w3schools.com/python/python_functions.asp

def get_unique_list(aList):
    newaList = []
    for i in range(len(aList)):
        check = True 
        for r in range(i - 1):
            if aList[i] == aList[r]:
               check = False
        if check == True:
          newaList.append(aList[i])
    return newaList

iList = [1, 2, 3, 2, 1, 4]
newiList = get_unique_list(iList)
print('Unique List:', newiList)


