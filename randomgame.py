import random
random_num = random.randint(1,100)
tries = 0
#print(random_num)
while True:
    num = int(input("enter a number : "))
    if num == random_num:
        if tries == 0:
            print(f"congeratlions you did it in first try num is {random_num}")
        else:
            print(f"congeratlions you did it in {tries} tries num is {random_num}")
        break
    elif abs(random_num - num) <= 10:
        tries += 1
        print("close")
    elif abs(random_num - num) > 10:
        tries += 1
        print("far")
    else:
        pass
