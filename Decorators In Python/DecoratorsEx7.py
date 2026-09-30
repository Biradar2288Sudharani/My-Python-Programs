# DecoratorsEx7.py
def convertupper(lw):
    def converttoupper():
        line,words=lw()
        lst=[]
        for word in words:
            lst.append(word.upper())
        return lst,words,line
    return converttoupper
def getwords(gl):
    def words():
        line=gl()
        ws=line.split()
        return ws
    return words
@convertupper
@getwords
def getline():
    return input("Enter a line of Text:")
# Main Program
lstwords=getline()
print("*"*50)
print("Given Line={}".format(lstwords[0]))
print("Given Words={}".format(lstwords[1]))
print("Given Words in Capital={}".format(lstwords[2]))
print("*"*50)



