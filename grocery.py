import datetime as dt

# Products Available
products = {
    "Milk": 25,
    "Curd": 20,
    "Chips": 45,
    "Momos": 60
}

# Customer Cart
cart = {}

today = dt.datetime.now()

# ----------------------------

def view():
    print("\n====== AVAILABLE PRODUCTS ======\n")

    for i in products:
        print(f"{i} : ₹{products[i]}")

# ----------------------------

def buy():

    while True:

        item = input("\nEnter Product Name (type 'done' to finish): ")

        if item.lower() == "done":
            break

        if item in products:

            qty = int(input("Enter Quantity: "))

            if item in cart:
                cart[item] += qty
            else:
                cart[item] = qty

            print("✅ Product Added Successfully")

        else:
            print("❌ Product Not Available")

# ----------------------------

def add():

    name = input("Enter New Product Name: ")
    price = int(input("Enter Price: "))

    products[name] = price

    print("✅ Product Added Successfully")

# ----------------------------

def bill():

    if len(cart) == 0:
        print("\nCart is Empty!")
        return

    total = 0

    print("\n========== BILL ==========")

    for i in cart:

        amount = products[i] * cart[i]

        print(f"{i} x {cart[i]} = ₹{amount}")

        total += amount

    print("---------------------------")
    print("Total Bill = ₹", total)

# ----------------------------

while True:

    print("\n================================")
    print("      RUDRA GROCERY STORE")
    print("================================")
    print("Date :", today.strftime("%d-%m-%Y"))
    print("Time :", today.strftime("%H:%M:%S"))

    print("""
1. View Products
2. Buy Product
3. Add New Product
4. Generate Bill
5. Exit
""")

    choice = int(input("Enter Your Choice : "))

    if choice == 1:
        view()

    elif choice == 2:
        buy()

    elif choice == 3:
        add()

    elif choice == 4:
        bill()

    elif choice == 5:
        print("\n❤️ Thank You For Visiting Rudra Grocery Store")
        break

    else:
        print("❌ Invalid Choice")