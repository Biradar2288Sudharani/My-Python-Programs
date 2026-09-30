from collections import deque
name=["k","v","r"]
dq=deque(name)
print(dq,type(dq))
dq.rotate(1)
print(dq,type(dq))
dq.rotate(2)
print(dq,type(dq))
dq.rotate(-1)
print(dq,type(dq))
dq.rotate(-2)
print(dq,type(dq))

