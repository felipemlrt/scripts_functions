#quick way to check each element from a series against part of it
test = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
if all(10 <= x for x in test):
 print("test 1")
if all(x == 0 for x in test[0:5]):
 print("test 2")

#to check all in a list against all from anopther list
testb = [0,10,25,50,80]
for i in range(0, len(testb)):
 if all(testb[i] >= x for x in test):
  print("test 3")
