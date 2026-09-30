# IteratorsEx1.py
s="PYTHON"
itrobj=iter(s)
while(True):
    try:
        item=next(s)    # Iterate By Calling Next
        print(item)
    except StopIteration:    # Exception Will Happen When Iteration Will Over
        break









