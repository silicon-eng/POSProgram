# POSProgram
POS system
Authors: Davica Chambers and Paul Brown
Date Created: March 28,2025
Course: ITT103
GitHub Public URL to Code:  
https://github.com/silicon-eng/POSProgram.git

Purpose:
This is a basic POS system that is built to handle inventory, 
process transactions, and generate receipts. It lets users:

.Add items to a cart.
.Remove items from a cart and update inventory accordingly.
.View the cart's contents.
.Get alerts for low stock items when inventory drops below a set limit.
 There is also an option for checking for low stock items.
.Process payments with tax and discounts applied.
.Generate a receipt after a successful transaction.

How to Run:
Requirements:
python 3

Features:
1. Inventory Management:
Products are stored in a dictionary with details like name, price, 
and stock quantity.
The stock is updated automatically when items are added or removed 
from the cart.
A low stock warning appears when an item has fewer than 5 units left.

2. Cart Operations:
Users can add products to the cart if they are in stock.
If there isn't enough stock, the system notifies the user.
Users can remove products from the cart, with the option to 
remove all if needed.

3. Checkout Process:
The subtotal is calculated based on items in the cart.
Orders over $5000 get a 5% discount.
A 10% sales tax is added after applying the discount.
Users enter the amount paid, and the system calculates the change.
If the payment is too low, users must enter a valid amount or cancel 
the transaction.
The cart clears once the payment is completed.

4. Receipt Generation:
A receipt is displayed after checkout with all transaction details.
It includes the cart list, total cost, amount paid, and change given.

Required Modifications:
1. Updating Products: Edit the inventory dictionary in main() 
to change or add additional available products.

2. Adjusting Taxes and Discounts: Modify the values in 
process_checkout() if needed.

3. Changing the Low-Stock Alert: Edit the threshold value in is_low_stock().

Limitations:
1. The system does not support a transaction history.
2. The system only supports cash payments.
3. New products can only be added in the inventory through editing the code.
