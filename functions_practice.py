
# Function hello()
def hello():
    print("Hello, user!")

# Function pack()
def pack(arg1, arg2, arg3):
    return[arg1,arg2,arg3]

# Function eat_lunch()
def eat_lunch(lunch_items):
    if len(lunch_items) == 0:
        print("My lunchbox is empty!")
    else:
        for i in range(len(lunch_items)):
            if i == 0:
                print(f"First I eat {lunch_items[i]}")
            else:
                print(f"Next I eat{lunch_items[i]}")

# Calling the Functions
hello()
packed_list= pack("apple","banana","cookie")
print(packed_list)

# Testing eat_lunch()
eat_lunch(["sandwich","chips","apple"])