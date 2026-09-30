# STRING EXAMPLES
a='python'
print(a,type(a))
a="python"
print(a,type(a))
a='''python'''
print(a,type(a))

# single line string data examples
a="""python"""
print(a,type(a))
a='python program'
print(a,type(a))
a="python program"
print(a,type(a))
a='12345'
print(a,type(a))
a="123456"
print(a,type(a))
a='''123456'''
print(a,type(a))
a="""123456"""
print(a,type(a))
a='!@#$%^&*()'
print(a,type(a))
a="python3.12"
print(a,type(a))
a="python"
print(len(a))
a="python programming"
print(len(a))

# multiline string data examples
a=''' python is very
popular language in
current marcket'''
print(a,type(a))
a="""python is very
popular language in
current marcket"""
print(a,type(a))


'''
a="python is very           
popular language in
current marcket"
print(a,type(a)...............# unterminated string literal
'''

# memory management of str data examples
a="sudharani"
print(a,len(a))
a="biradar sudharani"
print(a,len(a))

'''
# OPERATIONS ON STR DATA (their is two types of operations)
'''
# 1) INDEXING OPERATION EXAMPLES
a="python"
print(a,type(a))
print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])
print(a[5])
print(a[-1])
print(a[-2])
print(a[-3])
print(a[-4])
print(a[-5])
print(a[-6])
'''
print(a[10]) #............. IndexError: String Index Out Of Range
print(a[-7]) #............. IndexError: String Index Out Of Range
'''

# MOST IMPORTANT QUESTIONS FOE INTERVIEW POINT OF VIEW
a="python"
print(a,type(a))
print(len(a))
print(a[len(a)-1])
print(a[-len(a)])
print(a[len(a)-len(a)])
'''
print(a[-len(a)-1])  #............. IndexError: String Index Out Of Range
print(a[len(a)])     #............. IndexError: String Index Out Of Range
'''



# SLICING OPERATION EXAMPLES (In slicing opertoin their is 5 syntaxes)
# SYNTAX - 1: strobg[BEGIN : END]
# EXAMPLE - 1:-
s="python"
print(s,type(s))
print(s[0:0])
print(s[0:1])
print(s[0:2])
print(s[0:3])
print(s[0:4])
print(s[0:5])
print(s[0:6])
print(s[0:7])
print(s[0:100])
print(s[1:0])
print(s[2:1])
print(s[3:2])
print(s[4:3])
print(s[5:4])
print(s[6:5])

# EXAMPLE - 2:-
s="python"
print(s,type(s))
print(s[-6:-1])
print(s[-6:-2])
print(s[-6:-3])
print(s[-6:-4])
print(s[-6:-5])
print(s[-6:-6])
print(s[-2:-1])
print(s[-3:-2])
print(s[-4:-3])
print(s[-5:-4])
print(s[-6:-5])
print(s[-7:-6])
print(s[-125:-2])
print(s[-1000:-5])
print(s[-50:-3])
print(s[-200:-4])
print(s[-4:-45])


#EXAMPLE - 3:-
s="python"
print(s,type(s))
print(s[1:-2])
print(s[2:-1])
print(s[3:-1])
print(s[-5:4])
print(s[-6:6])
print(s[0:-1])
print(s[-6:123])
print(s[-123:234])
print(s[-1000:2000])
print(s[4:-5])
print(s[2:-5])
print(s[0:-6])
print(s[0:-5])


#EXAMPLE - 4:-
s="python"
print(s,type(s))
print(s[-6:len(s)])
print(s[-len(s):6])
print(s[-len(s):6666])
print(s[6666:len(s)])
print(s[0:0])
print(s[-1:-1])
print(s[2:-2])


# SYNTAX - 2: strobg[BEGIN : ]
#EXAMPLE - 1:-
s="python"
print(s,type(s))
print(s[2:])
print(s[3:])
print(s[1:])
print(s[4:])
print(s[5:])
print(s[55:])

#EXAMPLE - 2:-
s="python"
print(s,type(s))
print(s[-1:])
print(s[-2:])
print(s[-3:])
print(s[-4:])
print(s[-5:])
print(s[-6:])
print(s[-123:])
print(s[-123:-123])

# SYNTAX - 3: strobg[ : END]
# EXAMPLE - 1:-
s="python"
print(s,type(s))
print(s[:0])
print(s[:2])
print(s[:1])
print(s[:3])
print(s[:4])
print(s[:5])
print(s[:6])
print(s[:146])


# EXAMPLE - 2:-
s="python"
print(s,type(s))
print(s[:0])             # MOST IMPORTANT
print(s[:-2])
print(s[:-1])
print(s[:-3])
print(s[:-4])
print(s[:-5])
print(s[:-6])
print(s[:-146])


# SYNTAX - 4: strobg[ : ]
# EXAMPLES
s="python"
print(s[:])
s="LIRIL"
print(s[:])
s="RACECAR"
print(s[:])
s="WOW"
print(s[:])
print(s[:123])
print(s[-123:])


# SYNTAX - 5: strobg[BEGIN : END : STEP]
# RULE - 2:-
# EXAMPLE - 1 :-
s="python"
print(s,type(s))
print(s[0:6:1])
print(s[0:6:2])
print(s[0:6:3])
print(s[2:6:2])
print(s[3:100:2])
print(s[::1])
print(s[::2])
print(s[1::])
print(s[3::2])
print(s[:200:])
print(s[:200:4])
print(s[:200:15])
print(s[4:300:])

# EXAMPLE - 2 :-
s="python"
print(s,type(s))
print(s[5:3:1])
print(s[3:2:2])
print(s[4:1:2])
print(s[0:6:1])


# RULE - 3:-
# EXAMPLE - 1 :-
s="python"
print(s,type(s))
print(s[::])
print(s[::-1])
print(s[::1])
print(s[0:6:-1])
print(s[2:6:-1])
print(s[5:1:-1])
print(s[5:2:-2])
print(s[::-2])
print(s[4::-2])
print(s[:5:2])
print(s[:5:2] [: : -1])


# EXAMPLE - 2 :-
s="python"
print(s,type(s))
print(s[-6::])
print(s[-6::-1])
print(s[-6::1])
print(s[-1::])
print(s[-1::-1])
print(s[-1::-2])
print(s[-2:-5:-2])
print(s[-2:-6:-3])
print(s[122:-1000:-1])
print(s[0:1000:-2])
print(s[0:1000:])
print(s[100:-7:-1])


# RULE - 4:-
# EXAMPLE - 1 :-
s="python"
print(s,type(s))
print(s[::])
print(s[2:0:1])
print(s[2:0])


# RULE - 4:-
# EXAMPLE - 1 :-
s="python"
print(s,type(s))
print(s[-6:-1:-1])
print(s[:-1:-1])
print(s[-123:-1:-2])


# OTHER MORE EXAMPLES OF STR
s="LIRIL"
print(s)
print(s[ : : ])
print(s[ : :-1])
print(s[ : : ]==s[: :-1])
s="python"
print(s[ : : ]==s[: :-1])
s="MADAM"
print(s[ : : ]==s[: :-1])
s="MALAYALAM"
print(s[ : : ]==s[: :-1])
s="SUDHARANI"
print(s[ : : ]==s[: :-1])
s="RACcar"
print(s[ : : ]==s[: :-1])
print("WOW"=="WOW"[: : -1])





































































