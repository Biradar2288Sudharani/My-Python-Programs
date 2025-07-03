# DICT CATEGORY DATA TYPE 
a={10:"sudha"}
print(a,type(a),len(a))

b={}
print(b, type(b), len(b))

a={10:20, 30:20,30:90}
print(a,type(a),len(a))

a={100:1.2, 200:3.3, 300:4.2}
print(a,type(a),len(a))
#print(a[0])..............KEY ERROR
print(a[200])
a[100] = 4.7
print(a)

# EMPTY DICT
a={}
print(a,type(a),len(a))

a={}
print(a,type(a),len(a))
a[10]="sudha"
a[20]="amma"
a[30]="anna"
a[40]="appa"
print(a,type(a),len(a))


# NON-EMPTY LIST
a={10:20, 30:20,30:90}
print(a,type(a),len(a))


# pre-defined functions in dict
# 1. CLEAR()
a={10:1.2, 20:3.4,30:4.3,40:5.5}
print(a,type(a),len(a),id(a))
print(a.clear())
print(a,type(a),len(a),id(a))

# 2. POP()
a={10:1.2, 20:3.4,30:4.3,40:5.5}
print(a,type(a),len(a),id(a))
print(a.pop(30))
print(a,type(a),len(a),id(a))
# print(a.pop(100))..............KEY ERROR
# print(dict().pop(10))..............KEY ERROR
# print(dict().pop(10))..............KEY ERROR

# 3. POPITEM()
a={10:1.2, 20:3.4,30:4.3,40:5.5}
print(a,type(a),len(a),id(a))
print(a.popitem())
print(a,type(a),len(a),id(a))
# print(a.popitem())..............KEY ERROR
# print({}.popitem())..............KEY ERROR
# print(dict().popitem())..............KEY ERROR

# 4. COPY()
a={10:1.2, 20:3.4,30:4.3,40:5.5}
print(a,type(a),len(a),id(a))
b=a.copy()
print(b,type(b),len(b),id(b))
a[50]=6.6
a[60]=7.3
b[50]=9.0
b[60]=4.3
print(a,type(a),len(a),id(a))
print(b,type(b),len(b),id(b))

# 5. GET()
a={10:"python",20:"c",30:"c++",40:"django"}
print(a,type(a),len(a),id(a))
b=a.get(30)
print(b)
c=a.get(10)
print(c)
d=a.get(100)
print(d)
print({}.get(100))
print({}.get(0))
print(dict().get(100))
a={10:"python",20:"c",30:"c++",40:"django"}
print(a,type(a),len(a),id(a))
print(a[10])
print(a[20])
print(a[30])
print(a[40])
#print({}.get(20))..............KEY ERROR
print(dict()[20])
print({1:1.1,2:2.2,3:3.3,4:4.4}.get(2))

# 6. KEYS()
a={10:"python",20:"c",30:"c++",40:"django"}
print(a,type(a),len(a),id(a))
b=a.keys()
print(b,type(b),len(b),id(b))
for val in b:
      print(val)
for val in a.keys():
      print(val)

# 7. VALUES()
a={10:"python",20:"c",30:"c++",40:"django"}
print(a,type(a),len(a),id(a))
b=a.values()
print(b,type(b),len(b),id(b))
for val in b:
      print(val)
for val in a.values():
      print(val)

# 8. ITEMS()
a={10:"python",20:"c",30:"c++",40:"django"}
print(a,type(a),len(a),id(a))
b=a.items()
print(b,type(b),len(b),id(b))
for val in b:
      print(val)
for val in a.items():
      print(val)
for k,v in b:
    print(k,"-->",v)

# 9. UPDATE()
a={10:1.1,20:2.2}
b={30:3.3,40:4.4}
print(a,type(a),len(a),id(a))
print(b,type(b),len(b),id(b))
print(a.update(b))
print(a,type(a),id(a))
print(b,type(b),id(b))
# IN SAME KEY
a={10:1.1,20:2.2}
b={20:3.3,40:4.4}
print(a,type(a),len(a),id(a))
print(b,type(b),len(b),id(b))
print(a.update(b))
print(a,type(a),id(a))
print(b,type(b),id(b))
# IN a and b BOTH SAME KEYS
a={10:1.1,20:2.2}
b={10:3.3,20:4.4}
print(a,type(a),len(a),id(a))
print(b,type(b),len(b),id(b))
print(a.update(b))
print(a,type(a),id(a))
print(b,type(b),id(b))
# UPDATE TWO MORE DICT
a={10:1.1,20:2.2}
b={1:"sudha",2:"shankar"}
c={"mango":12,"banana":24}
#print(a.update(b,c))..........TypeError: update expected at most 1 argument, got 2
#print(a.update(b).update(c))...........AttributeError: 'NoneType' object has no attribute 'update'
# SOLUTION FOR ABOVE TWO MORE DICT
print(a.update(b))
print(a.update(c))
print(a)

# SPECIAL POINTS
a={"mango":12,"banana":24,"kiwi":6}
print(a)
for val in a.keys():
    print(val)
for val in a.values():
    print(val)
for val in a.items():
    print(val)
for val in a:
    print(val)
for val in a.keys():
    print(val,"-->",a[val])
for val in a:
    for val in a:
        print(val,"-->",a.get[val])...........TypeError: 'builtin_function_or_method' object is not subscriptable

# Combination of dict with dict,set,list and tuple
# CASE-1: DICT IN DICT----POSSIBLE
a={"number":10,"name":"sudha","marks":{"C":50,"C++":30,"PYTHON":60,"Django":45}}
print(a,type(a),len(a),id(a))
for val in a:
    print(val)
for val in a:
    print(val,"-->",a.get(val))
for k,v in a.items:
    print(k,"-->",v)
for k,v in a.items:
    print(k,type(k),type(a))........TypeError: 'builtin_function_or_method' object is not iterable
for k,v in a["marks"]:
    print(k,"-->",v)........TypeError: 'builtin_function_or_method' object is not iterable
a["marks"]["C"]=55
print(a)
a["marks"]["DBMS"]=50
print(a)
a["marks"].pop("DBMS")
print(a)
a.pop("marks")
print(a)

# CASE-2: DICT IN SET----NOT-POSSIBLE
a={10,"sudha",{10:1.1,20:2.2},"python"}............TypeError: unhashable type: 'dict'

# CASE-3: DICT IN TUPLE-------POSSIBLE
a=(10,"sudha",{10:1.1,20:2.2},"python")
print(a,type(a),len(a),id(a))
for val in a:
    print(val,type(val))
for val in a[2]:
    print(val)........TypeError: 'builtin_function_or_method' object is not iterable
for k,v in a[2].items:
    print(k,"-->",v)........TypeError: 'builtin_function_or_method' object is not iterable
a[2][20]=2.4
print(a,type(a))
a[-2][10]=1.5
print(a,type(a))
a=100,"amma",{"TS":"HYD","KAR":"BANG","MH":"MUMB"},"PYTHON"
print(a,type(a),len(a),id(a))
for k,v in a[-2].items:
    print(k,"-->",v)........TypeError: 'builtin_function_or_method' object is not iterable

# CASE-4: DICT IN LIST-------POSSIBLE
a=[100,"amma",{"TS":"HYD","KAR":"BANG","MH":"MUMB"},"PYTHON"]
print(a,type(a),len(a),id(a))
for val in a:
    print(val,type(val))
for k in a[-2].keys():
    print(k,"-->",a[-2].get(k))
for k in a[-2].keys():
    print(k,"-->",a[2][k])
a[-2]["AP"]="VIJ"
print(a,type(a))
a.insert(10,{"hb1":"read","hb2":"attend","hb3":"practice"})
print(a,type(a))
for k,v in a[2].items:
    print(k,"-->",v)........TypeError: 'builtin_function_or_method' object is not iterable

# CASE-5: SET IN DICT-------POSSIBLE
a={"roll_no":3,"name":"sudha","intmarks":{37.38,39,40},"college_name":"KIT"}
print(a,type(a),len(a),id(a))
for k,v in a.items():
    print(k,"-->",v,"-->",type(v),type(a))
a["intmarks"].add(36)
print(a,type(a))
a["extmarks"]=(40,45,50,35,30)
print(a,type(a))

# CASE-6: TUPLE IN DICT-------POSSIBLE
a={"roll_no":3,"name":"sudha","intmarks":{39.38,35,40},"college_name":"KIT"}
print(a,type(a),len(a),id(a))
for k,v in a.items():
    print(k,"-->",v,"-->",type(v),type(a))
a["intmarks"]=tuple(sorted(a["intmarks"]))
for k,v in a.items():
    print(k,"-->",v,"-->",type(v),type(a))
a["extmarks"]=(40,45,50,35,30)
for k,v in a.items():
    print(k,"-->",v,"-->",type(v),type(a))
print(a["extmarks"][2])
print(len(a["extmarks"]))
print(len(a["extmarks"])-1)
print(a["extmarks"],len(a["extmarks"])-1)

# CASE-7: LIST IN DICT-------POSSIBLE
a={"roll_no":3,"name":"sudha","intmarks":{39.38,35,40},"college_name":"KIT"}
print(a,type(a),len(a),id(a))
for k,v in a.items():
    print(k,"-->",v,"-->",type(v),type(a))
for val in a["intmarks"]:
    print(val)
print(a["intmarks"].insert(44,36))...........AttributeError: 'set' object has no attribute 'insert'
for k,v in a.items():
    print(k,"-->",v,"-->",type(v),type(a))
