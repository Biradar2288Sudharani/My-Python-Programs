# GeneratorEx3.py
def kvr(begin,end):
    while(begin,end):
        yield begin
        begin=begin+1

# Main Program
k=kvr(10,15)    # Function which build generator object here k is an object of type <class,"generator">
while(True):
    try:
        print(next(k))
    except StopIteration:
        print("*"*50)
        break






