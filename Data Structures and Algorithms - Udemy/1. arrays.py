strings = ['a', 'b', 'c', 'd']
strings.append('e') #takes only O(1)
strings.append('f') #takes only O(1) 
strings.pop() #takes only O(1)
strings.insert(0, '1') #takes O(n) because of the shifting of all other indices
strings.insert(2, '44')
print(strings[2])
print(strings)