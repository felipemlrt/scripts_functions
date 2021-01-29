#quick way to check each element from a series against part of it
test = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in range(0, len (test)):
    if all(test[i] > x for x in (test[i-5:i-1])):
     print(test[i])
