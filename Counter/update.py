from collections import Counter
coun=Counter()
print(coun)
print("After Updating")
coun.update([1,2,3,4,5,6])
print(coun)
coun.update([1,4,2,2])
print(coun)