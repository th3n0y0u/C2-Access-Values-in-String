'''

Access values in String
- To access substrings, Use the square bracets for slicing along with index or indixies to obtain your substring.

var = "Hello"

# Individual
string: | H | e | l | l | o |
positive: | 0 | 1 | 2 | 3 | 4 |
negative: | -5 | -4 | -3 | -2 | -1 |

# Consective
string: | H | e | l | l | o |
index: 0   1   2   3   4   5

In case of printing consecutive characters, it needs to strat beginning index and colon, then ending index

ex) print "ello" from var
print (var[1: ])

'''

List1 = ["a", "b", "g", "y", "j", "k", "h"]
print(List1[1:4])

string = "student"
print(string[3:])

var1 = "Hello World!"
var2 = "Python Programming"
# 1. print 'h' from var2
print(var2[3])

# 2. print 'hi' from using var1, and var2

print(var1[0] + var2[-3])

print(var1[0] + var2 [15])
print(var2[3] + var2 [15]) 

print(var1[4:7])
print(var2.find(" ")) # returns the index of the first matched character(s)
print(var2[0:var2.find(" ")])

if("Python" in var2):
  print("YAAAAAAAAY!")
else:
  print("NAAAAAYYYYY")

print(ord('A'))
print(chr(75))
print(chr(0))