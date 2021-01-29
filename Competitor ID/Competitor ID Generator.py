import random
import string


aList = ['0','1','2','3','4','5','6','7', '8', '9']
aList.extend(list(string.ascii_uppercase))
print(aList)
print ("choosing 5 random items from a list using random.sample() function")
sampled_list = random.sample(aList, 5)
print(''.join(sampled_list))
