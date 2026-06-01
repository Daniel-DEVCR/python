set1 = {1, 2, 3}
set2 = {1, 2, 3}
set3 = set1

print(id(set1))
print(id(set2))
print(id(set3))

print(set1 is set2)
print(set1 is set3)


'''
{1, 2, 3} → creates a new object

= → creates a new reference, not a new object (same ID)

'''