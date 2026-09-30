# GeneratorEx4.py
def kvr(begin=0,end=0,step=1):
    while(begin<=end):
        yield begin
        begin=begin+step

# Main Program
k=kvr(10,15,2)    # Function which build generator object here k is an object of type <class,"generator">
while(True):
    try:
        print(next(k))
    except StopIteration:
        print("*"*50)
        break
print("------ OR ------")
r=kvr(1000,1020,6)
for val in r:
    print(val)
print("*"*50)
print("----------- OR -----------")
for val in kvr(50,56):
    print(val)
print("*"*50)
print("----------- OR -----------")
for val in kvr(end=6):
    print(val)
print("*"*50)
print("----------- OR -----------")
for val in kvr(begin=10,end=100,step=10):
    print(val)
print("*"*50)



