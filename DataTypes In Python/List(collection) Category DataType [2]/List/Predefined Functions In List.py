# Predefined function in list
# 1. APPEND()
'''
a=[10,"sudha",3.14]
print(a,type(a),id(a))
a.append("rani")
print(a,type(a),id(a))

a=[]
print(a,type(a),id(a))
a.append(100)
a.append("sudha")
a.append(3.14)
a.append("True")
print(a,type(a),id(a))

#a.apppend("python","html","CSS")
#print(a,type(a),id(a))..........AttributeError: 'list' object has no attribute 'apppend'. Did you mean: 'append'?
a.append(["python","html","CSS"])
print(a,type(a),id(a))

# 2. INSERT()
a=[10,"sudha",3.14]#<..........+VE Index Example
print(a,type(a),id(a))
a.insert(2,"python")
print(a,type(a),id(a))
a.insert(1,"shankar")
print(a,type(a),id(a))

a=[10,"sudha",3.14]#<..........-VE Index Example
print(a,type(a),id(a))
a.insert(-1,"python")
print(a,type(a),id(a))
a.insert(-3,"shankar")
print(a,type(a),id(a))

a=[10,"sudha",3.14]
print(a,type(a),id(a))
a.insert(200,"python")
print(a,type(a),id(a))
a.insert(2000,"shankar")
print(a,type(a),id(a))

a=[10,"sudha",3.14]
print(a,type(a),id(a))
a.insert(-200,"python")
print(a,type(a),id(a))

# 3. REMOVE()
a=[10,"sudha",3.14]
print(a,type(a),id(a))
a.remove("sudha")
print(a,type(a),id(a))
a.remove(10)
print(a,type(a),id(a))
a.remove(3.14)
print(a,type(a),id(a))
#a.remove("python")...........ValueError: list.remove(x): x not in list
print(a,type(a),id(a))

a=[10,20,30,10,20,40,50]
print(a,type(a),id(a))
a.remove(10)
print(a,type(a),id(a))
a.remove(10)
print(a,type(a),id(a))
a.remove(20)
print(a,type(a),id(a))
a.remove(20)
print(a,type(a),id(a))
#a.remove(100)...........ValueError: list.remove(x): x not in list
print(a,type(a),id(a))

#print([].remove(10)).............ValueError: list.remove(x): x not in list
#print(list().remove(100)).............ValueError: list.remove(x): x not in list
#print(lilst().remove(100))..............NameError: name 'lilst' is not defined. Did you mean: 'list'?

# 4. POP INDEX()
a=[10,20,30,10,20,40,50]
print(a,type(a),id(a))
a.pop(3)
print(a,type(a),id(a))
a.pop(-4)
print(a,type(a),id(a))
a.pop(120)
#print(a,type(a),id(a))..........IndexError: pop index out of range
#print([].pop(0))................IndexError: pop index out of range
#print(list().pop(-1))............IndexError: pop index out of range
'''
# 5. POP()
a=[10,"sudha",3.14,True]
print(a,type(a),id(a))
a.pop()
print(a,type(a),id(a))
a.pop()
print(a,type(a),id(a))
a.pop()
print(a,type(a),id(a))
a.pop()
print(a,type(a),id(a))
print(a)
#print([].pop()).........IndexError: pop from empty list
#a().pop()
#print(a,type(a),id(a))...........TypeError: 'list' object is not callable

print([10,20,30,40].pop(1))
a("python").pop(5)
print(a("python").pop(-2))
print(a("python").pop(-len("python")))
print(a("python").pop(len("python")))













