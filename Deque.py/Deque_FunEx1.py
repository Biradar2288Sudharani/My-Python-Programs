from collections import deque
a=['d', 'u', 'r', 'e', 'k']
b=deque(a)
print(b,type(b))
print("*"*50)

print("-----------APPEND FUNCTION-------------")
b.append("h")
print(b)
print("*"*50)

print("-----------APPENDLEFT FUNCTION-------------")
b.appendleft("s")
print(b)
print("*"*50)

print("-----------clear FUNCTION-------------")
b.clear()
print(b)
print("*"*50)

print("-----------COUNT FUNCTION-------------")
b.count()
print(b)
print("*"*50)

print("-----------EXTEND FUNCTION-------------")
b.extend()
print(b)
print("*"*50)

print("-----------ROTATE FUNCTION-------------")
b.rotate(3)
print(b)
print("*"*50)

print("-----------INDEX FUNCTION-------------")
b.index([3])
print(b)
print("*"*50)

print("-----------INSERT FUNCTION-------------")
b.insert([0],"Sudha")
print(b)
print("*"*50)

print("-----------POP FUNCTION-------------")
b.pop()
print(b)
print("*"*50)

print("-----------POPLEFT FUNCTION-------------")
b.popleft()
print(b,type(b))
print("*"*50)

print("-----------REMOVE FUNCTION-------------")
b.remove("s")
print(b,type(b))
print("*"*50)

print("-----------REVERSE FUNCTION-------------")
b.reverse()
print(b,type(b))
print("*"*50)
