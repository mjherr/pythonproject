#function named hello()
def hello():
    print("Hey, Person")

#function name pack()
def pack(water, food, phone):
    return [water, food, phone]

#function eat_lunch():
def eat_lunch(my_lunch):
    if len(my_lunch) == 0:
        print("My lunch is empty!")
    else:
        for i in range(len(my_lunch)):
            if i == 0:
                print(f"First I eat {my_lunch[0]}")
            else:
                print(f"Next I eat {my_lunch[i]}")

hello()
print(pack("water", "food", "phone"))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["chips", "banana", "sandwich", "cookie"])
