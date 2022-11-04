# import the random module
import random

# set the flag for infinitive while loop
keepOn = True
# set the counter for the number of loop counting
count = 0

# Infinitive while loop untile the generated num is the multiple of 5
while (keepOn):
    num = random.randint(1, 100)
    count += 1
    print("Generated num : ", num)
    if ((num % 5)==0):
        keepOn = False  # Option code in here.....^^
        print(f"Exit the while loop because {num} is multipled by 5")
        break
    elif ((num % 3)==0):
        print(f"{num} is multipled by 3, skipping and contiune to loop......")
        continue
    
    print(f"The {num} are not multiple by both 3 and 5")
    continue

print(f"\n---------------------------------------------------")
print(f"It goes through {count} count(s) of looping!")

