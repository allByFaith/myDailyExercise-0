# Using a while loop, one very iteration generate a 
# randomnumber. If it'sa multiple of 5, break from the loop.
# If it's a multiple of 3, end the current iteration with 
# continue and print a message to show you are skipping.
# If it's neither, print the number and continue the loop.

import random

num = random.randint(1,100)
print("The first generated num : ", num)
      
count = 1
while((num % 5)!=0):
    print("Num is not multiple by 5 : ", num)
    if ((num % 3)==0):
        print(f"New generate num : {num} is multiple of 3 :---> Skipping")
        num = random.randint(1,100)
        print("New generated num : ", num)
        count += 1
        break
    else:
        while((num % 3)!=0):
            print("Num is not multiple by 3 : ", num)
            num = random.randint(1,100)
            print("New generated num : ", num)
            count += 1

print("########### Total time of num generated : ", count)
    



        