class Product:
    def __init__(self, name, price, stock):              #defining a product with attributes name, price and stock
        self.name = name
        self.price = price
        self.stock = stock
    
    def update_stock(self, quantity):                   
        if self.stock >= quantity:                       #checks if stock for a product is greater than input
            self.stock -= quantity                       #deducts from stock
            return True                                  #returns true if quantity is deducted from stock
        return False                                     #returns false if quantity can not be deducted from stock
    
    def restock(self, quantity):                         #adds back to the stock of a product
        self.stock += quantity
    
    def is_low_stock(self):                              
        return self.stock < 5                            #returns true if stock is below 5 and false if stock is 5 or greater



def add_items(cart, product_name, quantity, inventory):
    
    product = inventory[product_name]                #sets that specific product name to a variable for manipulation of data
    if product.update_stock(quantity):               #checks if there is enough stock and adjusts accordingly
        cart_product = (product.name, product.price)
        for x in range(quantity):
            cart.append(cart_product)     #adds to cart if there is enough stock
        print("-" * 25)
        print("Item successfully added.")   #displays sucess message
        print("-" * 25)
        if product.is_low_stock():
            print("-" * 25)
            print(f"Stock for {product_name} is low.")     #outputs a low stock message if stock is low for a product
            print("-" * 25)
    else:
        print("-" * 25)
        print(f"Not enough {product_name} in stock.")     #lets user know that not enough product is in stock
        print("-" * 25)
    


def remove_items(cart, product_name, quantity, inventory):
    product = inventory.get(product_name)                      #gets product from inventory
    cart_product = (product.name, product.price)       
    count = cart.count(cart_product)                           #count occurrences of product in the cart

    if quantity < 0:
        print("-" * 50)
        print("Can't remove a negative number of item/s.")    #displays message if quntity input is negative
        print("-" * 50)
        return
    
    elif quantity == 0:
        print("-" * 25)
        print("Can't remove zero items.")    #displays message if quntity input is zero
        print("-" * 25)
        return
        
    else:
        while quantity > count:                                       #if trying to remove more than number of products in cart
            print("-" * 50)
            print(f"Not enough {product_name} in the cart. There is only {count}.")
            print("-" * 50)
            decision = int(input(f"\nDo you want to remove all {count} instead? 1)yes  2)no: ")) #gives user a potential alternate instead of just exiting

            if decision == 1:
                quantity = count                                   #adjusts quantity to be equal to count of product in cart
            elif decision == 2:
                print("-" * 25)
                print("No items were removed.")
                print("-" * 25)
                return
            else:
                print("-" * 25)
                print("Invalid option. Try again.")
                print("-" * 25)
                print(int(input("\nEnter quantity: ")))         #allows user another attempt
                continue

        #loop for removing product one at a time 
        for x in range(quantity):
            cart.remove(cart_product)
            product.restock(1)

        if quantity == 1:
            print("-" * 50)
            print(f"{quantity} item of {product_name} were removed.")    #displays sucess message for quantity being 1
            print("-" * 50)
        else:
            print("-" * 50)
            print(f"{quantity} items of {product_name} were removed.")    #displays sucess message for quantity more than 1
            print("-" * 50)


def view_cart(cart):
    if not cart:                             #checks if cart is empty 
        print("\n🛒 --- Cart ---")
        print("The cart is empty.")
        return None
    
    #formatting for viewing cart

    print("\n🛒 --- Cart ---")
    print("-" * 50)
    print("Product" + " "*7 + "Qty" + " "*6 + "Unit Price" + " "*5 + "Total Price")
    print("-" * 50)

    cost = 0
    counted_items = []                       #keeps track of products already processed

    for item in cart:                        #separates each product in the cart
        product = item[0]                    #separates the product name and the product price
        price = item[1]

        if product in counted_items:         #if already tracked then skip iteration
            continue

        amount_of_item = 0

        for cart_item in cart:               #loop through and count specific product
            if cart_item[0] == product:      #checks if the current product appears again in the cart
                amount_of_item += 1

        total = amount_of_item * price       #calculates total amount for a single product
        print(f"{product:<15}{amount_of_item:<10}{price:<15.2f}{total:<15.2f}")

        cost += total                        #calculates all the totals to get the final cost
        counted_items.append(product)        #add product to tracked list

    print("-" * 50)
    print(f"Total:                                 ${cost:.2f}")


def check_low_stock(inventory):
    """
    Displays alerts for products with stock below 5.
    """
    print("\n--- Low Stock Alert ---")
    for product in inventory.values():               #directly access product object data
        if product.is_low_stock():
            name = product.name
            stock = product.stock
            print(f"{product.name} has {product.stock} remaining")
    print("-----------------------")

def process_checkout(cart):
    """
    Calculates the total, applies tax, and handles payment.
    Allows for processing multiple transactions.
    """
    if not cart:                                         #checks if cart is empty
        print("\n🛒 --- Cart ---")
        print("Cart is empty.")
        return None

    # Calculate subtotal 
    subtotal = 0
    for item in cart:
        subtotal += item[1]                             #item[1] is the price

    # If subtotal is greater than $5000 apply 5% discount
    discount = 0
    if subtotal > 5000:
        discount = subtotal * 0.05
        print(f"\nA discount of 5% (${discount:.2f}) has been applied.")

    discounted_subtotal = subtotal - discount
    tax = discounted_subtotal * 0.10                    #applies 10% sales tax
    total_cost = discounted_subtotal + tax

    # Display checkout details
    print("\n💵--- Checkout ---")
    print(f"Subtotal: ${subtotal:.2f}")
    if discount > 0:
        print(f"Discount (5%): ${discount:.2f}")
    print(f"Tax (10%): ${tax:.2f}")
    print(f"Total Sales: ${total_cost:.2f}")

    # Payment process
    while True:
        try:
            amount_received = float(input("Enter amount received from customer: "))
            if amount_received >= total_cost:
                change = amount_received - total_cost
                print(f"Cash: ${amount_received:.2f}")
                print(f"Change: ${change:.2f}")
                generate_receipt(cart, subtotal, discount, tax, total_cost, amount_received, change) #calls to generate receipt if payment was a success
                cart.clear()                                                                         #clear cart for next transaction
                break
            else:
                print("-" * 50)
                print("Insufficient payment.")
                print("-" * 50)
                decision = int(input("\ndo you wish to cancel transaction? 1)yes   2)no :"))    #gives user a choice to cancel the transaction and return to the menu
                if decision == 1:
                    break
                elif decision == 2:
                    continue
                else:                                                                            #if another number is entered, continue to the next iteration
                    print("-" * 50)
                    print("Not a valid option. Continuing...")
                    print("-" * 50)
                    continue
        except ValueError:
            print("-" * 50)
            print("Invalid input. Please enter a numeric value.")
            print("-" * 50)

def generate_receipt(cart, subtotal, discount, tax, total_cost, amount_received, change):
    #formatting the receipt
    print("\n" + "-" * 50)
    print("             BEST BUY RETAIL STORE")
    print("             Receipt of Purchase")
    print("-" * 50)

    #count items and calculate total price per product
    print("Product" + " "*7 + "Qty" + " "*6 + "Unit Price" + " "*5 + "Total Price")
    print("-" * 50)
    counted_items = []
    for item in cart:
        product_name = item[0]  #retrive product name
        price = item[1]         #retrive price

        if product_name in counted_items:  #skip if already counted
            continue

        quantity = 0
        #count occurrences of the specific product in cart
        for cart_item in cart:
            if cart_item[0] == product_name:
                quantity += 1          

        total_price = quantity * price  #calculate total price per product
        print(f"{product_name:<15}{quantity:<10}{price:<15.2f}{total_price:<15.2f}")

        counted_items.append(product_name)  #adds to the list of counted items

    print("-" * 50)
    print(f"Subtotal: ${subtotal:.2f}")
    if discount > 0:                                          #displays discount only if it is greater than 0
        print(f"Discount (5%) off orders over $5000: ${discount:.2f}")
    print(f"Sales Tax (10%): ${tax:.2f}")
    print(f"Total Due: ${total_cost:.2f}")
    print(f"Amount Paid: ${amount_received:.2f}")
    print(f"Change Returned: ${change:.2f}")
    print("-" * 50)
    print("       Thank you for shopping with us!")
    print("-" * 50)


def get_product_name(product_choice):
    #product name gets assigned to the variable depending on user input
    if product_choice == 1:
        return "mackerel"
    elif product_choice == 2:
        return "sardine"
    elif product_choice == 3:
        return "bake beans"
    elif product_choice == 4:
        return "rice"
    elif product_choice == 5:
        return "flour"
    elif product_choice == 6:
        return "bread"
    elif product_choice == 7:
        return "ketchup"
    elif product_choice == 8:
        return "soda"
    elif product_choice == 9:
        return "water"
    elif product_choice == 10:
        return "corned beef"
    elif product_choice == 11:
        return "milk"
    elif product_choice == 12:
        return "eggs"
    elif product_choice == 13:
        return "butter"
    elif product_choice == 14:
        return "cheese"
    elif product_choice == 15:
        return "chicken"
    elif product_choice == 16:
        return "beef"
    elif product_choice == 17:
        return "detergent"
    else:
        return ""                       #handles invalid number inputs
    
def get_index(product_name):
    #gives each product a index number for identification
    if product_name == "mackerel":
        return 1
    if product_name == "sardine":
        return 2
    if product_name == "bake beans":
        return 3
    if product_name == "rice":
        return 4
    if product_name == "flour":
        return 5
    if product_name == "bread":
        return 6
    if product_name == "ketchup":
        return 7
    if product_name == "soda":
        return 8
    if product_name == "water":
        return 9
    if product_name == "corned beef":
        return 10
    if product_name == "milk":
        return 11
    if product_name == "eggs":
        return 12
    if product_name == "butter":
        return 13
    if product_name == "cheese":
        return 14
    if product_name == "chicken":
        return 15
    if product_name == "beef":
        return 16
    if product_name == "detergent":
        return 17

def main():

    inventory = {
        "mackerel": Product("mackerel", 245.5, 140),
        "sardine": Product("sardine", 350, 190),
        "bake beans": Product("bake beans", 325.5, 160),
        "rice": Product("rice", 235, 850),
        "flour": Product("flour", 198.99, 250),
        "bread": Product("bread", 459.99, 100),
        "ketchup": Product("ketchup", 245.99, 60),
        "soda": Product("soda", 99.99, 470),
        "water": Product("water", 120, 680),
        "corned beef": Product("corned beef", 1200, 150),
        "milk": Product("milk", 520, 200),
        "eggs": Product("eggs", 360, 300),
        "butter": Product("butter", 450, 120),
        "cheese": Product("cheese", 750, 80),
        "chicken": Product("chicken", 950, 100),
        "beef": Product("beef", 1200, 90),
        "detergent": Product("detergent", 650, 75)
    }
     
    cart = []
    
    while True:
        print("\n--- Best Buy Retail Store ---")
        print("1. Add item to cart")
        print("2. Remove item from cart")
        print("3. View cart 🛒")
        print("4. Check Low Stock")
        print("5. Checkout 💵")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        #adding items
        if choice == "1":
        
            try:
                #creating a menu with products in the inventory
                items = inventory.keys()          #stores all the keys inside a list
                for item in items:                #for each item in the list of keys
                    product = inventory[item]     #gets the value assigned to the item in the inventory so that we can have access to its attributes
                    index_of_item = get_index(product.name)
                    print(str(index_of_item)+ ") " + product.name + ":  $" + str(product.price) + " stock: " + str(product.stock))
                print("18) Cancel")                 #adds an option to cancel adding products

                #asks for user input for product
                product_choice = int(input("\nSelect product choice: "))

                if product_choice < 0:
                    print("-" * 50)
                    print("Can't use negative numbers")
                    print("-" * 50)
                    continue

                #if user decides to cancel process skip to the next iteration
                if product_choice == 18:
                    continue
            
                #gets the product name that is assigned to the index which is the user input
                product_name = get_product_name(product_choice)
        
                #if the product is not in the inventory displays message to user then skips to the next iteration
                product = inventory.get(product_name)                      #gets product from inventory

                if not product:                                            #if product does not exist in inventory
                    print("-" * 50)
                    print(f"{product_name} was not found in inventory.")
                    print("-" * 50)
                    continue
                
                #asks for user input for quantity
                quantity = int(input("Enter quantity: "))

                #checks if quantity entered is valid 
                if quantity < 0:
                    print("-" * 50)
                    print("Can't add a negative number of item/s.")    #displays message if quantity input is negative
                    print("-" * 50)
                    continue
                if quantity == 0:
                    print("-" * 25)
                    print("Can't add zero items.")    #displays message if quntity input is zero
                    print("-" * 25)
                    continue
                
                #passes information to the add items function
                add_items(cart, product_name, quantity, inventory)     #passing variables to the function
                product_name = ""                                      #clears product name
            #in the case that the user input is not int
            except ValueError:
                print("-" * 25)
                print("Invalid input.")
                print("-" * 25)
                
        #removing items
        elif choice == "2":
            try:
                #checks if cart if empty, if yes skips to next iteration
                if cart == []:
                    print("-" * 50)
                    print("Cart is empty. Please add some items")    #continues to the next iteration because cart is empty
                    print("-" * 50)
                    continue

                counted_items = []                            #stores already displayed product to prevent a repeat

                #displays only items currently in the cart
                print("\nItems currently in cart:")
                for items in cart:
                    product_name = items[0]                          #retrives the name of the products in the cart

                    if product_name in counted_items:           #checks if item has already been displayed to the screen to prevent repeating products
                        continue

                    index_of_item = get_index(product_name)

                    amount_of_item = 0                  #counter for repeated products in cart
                    product = inventory[product_name]
                    product_name = ""

                    for cart_item in cart:               #loop through and counts for a specific product
                        if cart_item[0] == product.name:      #checks if the current product appears again in the cart
                            amount_of_item += 1

                    print(str(index_of_item) + ") " + product.name + ":  $" + str(product.price) + " * " + str(amount_of_item))  #displaying what is in the cart
                    counted_items.append(product.name)   #adds the product name to a counting list of items

                print("18) Cancel")                        #option to cancel removing items process

                #prompts user for product input
                product_choice = int(input("\nSelect product to be removed: "))

                if product_choice < 0:
                    print("-" * 50)
                    print("Can't use negative numbers")
                    print("-" * 50)
                    continue

                #gives user the option to cancel process
                if product_choice == 18:
                    continue
                
                #gets product name based on user input
                product_name = get_product_name(product_choice)
            
            
                #checks if the product is in the inventory for input validation
                if product_name not in inventory:                 
                    print("-" * 50)
                    print("Not a valid product selection.")
                    print("-" * 50)
                    continue

                product = inventory[product_name]                      #gets the data needed for the specific product from the inventory
                cart_product = (product.name, product.price)            #adds product name and price to a variable to see if it is in the cart
                
                #checks if the product is in the cart and continues to the next iteration if it is not
                if cart_product not in cart:                             #if product does not exist in the cart
                    print("-" * 50)
                    print(f"{product_name} is not in cart.")
                    print("-" * 50)
                    continue
                
                #gets user input and then passes the information to the remove items function
                quantity = int(input("Enter quantity to remove: "))
                remove_items(cart, product_name, quantity, inventory)
                product_name = ""                                     #clears product name

            #handles user input not being an int
            except ValueError:
                print("-" * 25)
                print("Invalid input.")
                print("-" * 25)

        #view cart       
        elif choice == "3":
            view_cart(cart)
        
        #check low stock
        elif choice == "4":
            check_low_stock(inventory)

        #checkout process
        elif choice == "5":
            process_checkout(cart)

        #exit program
        elif choice == "6":
            print("-" * 50)
            print("Exiting POS System.")
            print("-" * 50)
            break
        #handles invalid input
        else:
            print("-" * 50)
            print("Invalid choice. Please try again.")
            print("-" * 50)


if __name__ == "__main__":
    main()