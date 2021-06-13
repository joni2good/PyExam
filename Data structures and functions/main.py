# Lists
intList = [1, 2, 3, 4, 5]  # mutable & ordered & 0 indexed
print(intList)
print("Length: " + str(len(intList)))

charList = ['a', 'b', 'c', 'd', 'e']
print(charList)

combinedList = intList + charList
print(combinedList)

booleanList = list((True, False, True, True))
print(booleanList)

print(intList[0])
print(charList[0])
print(combinedList[0])

print(intList[2:4])  # 2 index included, 4 not included
print(charList[:2])
print(booleanList[0:-1])

print('a' in intList)
print('a' in charList)
print(True not in combinedList)

for i in intList:
    print(i, end=" ")

print()

[print(i, end=" ") for i in intList]

print()

vowelList1 = []
vowelList2 = []

for i in charList:
    if i in 'aeiou':
        vowelList1.append(i)

print(vowelList1)

vowelList2 = [i for i in charList if i in 'aeiou']
# vowelList2 = [i if i in 'aeiou' else 0 for i in charList]

print(vowelList2)

# Tuples
intTuple = (1, 2, 3, 4, 5)  # immutable & ordered & 0 indexed
print(intTuple)
print(len(intTuple))

charTuple = ('a', 'b', 'c', 'd', 'e')
print(charTuple)

combinedTuple = intTuple + charTuple
print(combinedTuple)

tuple1 = ("apple",)
print(type(tuple1))

tuple2 = ("apple")
# tuple2 = tuple(("apple"))
print(type(tuple2))

(vowel1, *consonant, vowel2) = charTuple  # unpack
print(vowel1)
print(consonant)
print(vowel2)

for i in intTuple:
    print(i, end=" ")

print()

# Dicts
intDict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}  # mutable & ordered
print(intDict)
print(len(intDict))

charDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(charDict)

combinedDict = {**intDict, **charDict}
# combinedDict = {}
# combinedDict |= intDict
# combinedDict |= charDict
print(combinedDict)

print(intDict[2])
print(charDict.get('c'))

keys = charDict.keys()
# values = charDict.values()
# itemsAsTupleList = charDict.items()
print(keys)
charDict.update({'f': 6})
print(keys)

print('g' in charDict)

charDict['g'] = 7
# charDict.update({'g': 7})
print(charDict)

charDict.pop('g')
# del charDict['g']
# del charDict  # deletes entire dict
# charDict.clear()
print(charDict)

# for x in charDict.values():
# for x in charDict.keys():  # same output as below
for x in charDict:
    print(x, end=" ")

print()

for x, y in charDict.items():
    print("Key: " + str(x) + " Value: " + str(y), end=" ")

print()

{print("Key: " + str(x) + " Value: " + str(y), end=" ") for x, y in charDict.items()}
# dict_comp = {x: y for x, y in charDict.items()}
# print(dict_comp.items())

print()

# Sets
intSet = {1, 2, 3, 4, 5}  # immutable(can add or remove) & unordered
print(intSet)
print(len(intSet))
print(type(intSet))

charSet = set(('a', 'b', 'c', 'd', 'e'))
print(charSet)
print(type(charSet))

for i in charSet:
    print(i, end=" ")

print()

{print(i, end=" ") for i in intSet}

print()

print('a' in charSet)
print(6 in intSet)

intSet.add(6)
print(intSet)

combinedSet = set.union(intSet, charSet)
# combinedSet = set(())
# combinedSet.update(intSet)
# combinedSet.update(charList)  # Can receive any iterable
print(combinedSet)

print(intSet)
intSet.remove(6)  # Will raise error if doesn't exists
# intSet.discard(6)  # Will not raise error if doesn't exists
print(intSet)

# intSet.clear()
# del intSet

intSet2 = {4, 5, 6, 7, 8}

intSet3 = intSet.intersection(intSet2)  # Will only contain duplicates
print(intSet3)
# intSet.intersection_update(intSet2)
# print(intSet)

intSet4 = intSet.symmetric_difference(intSet2)  # Will only contain non duplicates
print(intSet4)
# intSet.symmetric_difference_update(intSet2)
# print(intSet)
