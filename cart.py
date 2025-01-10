import json
import os
import customtkinter as ctk
from tkinter import messagebox
import payment

class Cart:
    def __init__(self, username, cart_file="cart.json"):
        self.username = username
        self.cart_file = cart_file
        self.cart = self.load_cart()

    def load_cart(self):
        """Load the cart from the JSON file."""
        if os.path.exists(self.cart_file):
            if os.path.getsize(self.cart_file) == 0:  # Check if file is empty
                return {}
            with open(self.cart_file, "r") as file:
                try:
                    users = json.load(file)
                    return users.get(self.username, {})
                except json.JSONDecodeError:
                    print("Error: Cart file is corrupted. Initializing a new cart.")
                    return {}
        return {}

    def save_cart(self):
        """Save the current cart state to the JSON file."""
        if os.path.exists(self.cart_file):
            with open(self.cart_file, "r") as file:
                try:
                    users = json.load(file)
                except json.JSONDecodeError:
                    users = {}
        else:
            users = {}

        users[self.username] = self.cart

        with open(self.cart_file, "w") as file:
            json.dump(users, file, indent=4)

    def view_cart(self):
        """Display the cart in a GUI window with quantity adjustment buttons."""
        cart_window = ctk.CTkToplevel()
        cart_window.title(f"{self.username}'s Cart")
        cart_window.geometry("500x500")

        if not self.cart:
            ctk.CTkLabel(cart_window, text="Your cart is empty!", font=("Times New Roman", 14)).pack(pady=20)
            return

        row = 0

        def update_quantity(product, delta):
            """Update the quantity of a product by a given delta (+1 or -1)."""
            if product in self.cart:
                self.cart[product]["quantity"] += delta
                if self.cart[product]["quantity"] <= 0:  # Remove the item if quantity goes to zero
                    del self.cart[product]
            self.save_cart()
            cart_window.destroy()  # Refresh the cart window
            self.view_cart()

        def generate_final_bill():
            """Close the cart window and open the bill window."""
            cart_window.destroy()
            self.generate_bill()

        for product, details in self.cart.items():
            # Product name and price
            ctk.CTkLabel(
                cart_window, text=f"{product}: Price per item: ${details['price']:.2f}",
                font=("Times New Roman", 12)
            ).grid(row=row, column=0, padx=10, pady=5, sticky="w")

            # Quantity display and buttons
            ctk.CTkButton(
                cart_window, text="-", width=30, fg_color="#FF6347", hover_color="red",
                command=lambda p=product: update_quantity(p, -1)
            ).grid(row=row, column=1, padx=5)

            ctk.CTkLabel(
                cart_window, text=str(details["quantity"]), font=("Times New Roman", 12)
            ).grid(row=row, column=2, padx=5)

            ctk.CTkButton(
                cart_window, text="+", width=30, fg_color="#00FF00", hover_color="green",
                command=lambda p=product: update_quantity(p, 1)
            ).grid(row=row, column=3, padx=5)

            row += 1

        ctk.CTkButton(cart_window, text="Proceed To Checkout", fg_color="#007FFF", hover_color="blue", width=120,
                      command=generate_final_bill).grid(row=row, column=0, pady=20)


    def get_cart(self):
        """Return the current cart."""
        return self.cart
    
    def calculate_total_price(self):
        """Calculate the total price of the cart."""
        total_price = 0
        for product, details in self.cart.items():
            total_price += details["quantity"] * details["price"]
        return total_price

    def generate_bill(self):
        """Generate a detailed bill and display it in a new window."""
        total_price = self.calculate_total_price()

        bill_window = ctk.CTkToplevel()
        bill_window.title("Bill")
        bill_window.geometry("400x400")

        ctk.CTkLabel(bill_window, text="Bill Summary", font=("Times New Roman", 16, "bold")).pack(pady=10)

        receipt_details = ""  # Prepare receipt details to pass to the Payment Page
        for product, details in self.cart.items():
            item_line = f"{product}: {details['quantity']} x ${details['price']:.2f} = ${details['quantity'] * details['price']:.2f}"
            ctk.CTkLabel(bill_window, text=item_line, font=("Times New Roman", 12)).pack(anchor="w", padx=20, pady=5)
            receipt_details += item_line + "\n"

        ctk.CTkLabel(bill_window, text=f"Total: ${total_price:.2f}", font=("Times New Roman", 14, "bold")).pack(pady=20)
        receipt_details += f"-------------------\nTotal: ${total_price:.2f}"

        def go_back_to_cart():
            """Go back to the cart window."""
            bill_window.destroy()
            self.view_cart()

        def open_payment_window():
            """Open the payment window."""
            bill_window.destroy()
            self.open_payment_window(receipt_details)  # Pass the receipt details

        ctk.CTkButton(bill_window, text="Go Back to Cart", fg_color="#007FFF", hover_color="blue",
                    command=go_back_to_cart).pack(pady=10)

        ctk.CTkButton(bill_window, text="Proceed to Payment", fg_color="#000000", hover_color="black",
                    command=open_payment_window).pack(pady=10)

    def open_payment_window(self, receipt_details):
        """Open the payment page with receipt details."""
        def go_to_home():
            """Callback for returning to the main application."""
            print("Returning to Home Page...")

        payment.PaymentPage(parent=None, receipt_details=receipt_details, go_to_home_callback=go_to_home,username=self.username)

    def add_item(self, item_name, item_price):
        """Add an item to the cart."""
        if item_name in self.cart:
            self.cart[item_name]["quantity"] += 1
        else:
            self.cart[item_name] = {"quantity": 1, "price": item_price}
        self.save_cart()

    def remove_item(self, item_name):
        """Remove an item from the cart."""
        if item_name in self.cart:
            self.cart[item_name]["quantity"] -= 1
            if self.cart[item_name]["quantity"] <= 0:
                del self.cart[item_name]
            self.save_cart()

    def clear_cart(self):
        """Clear all items from the cart."""
        self.cart = {}
        self.save_cart()
        messagebox.showinfo("Cart Cleared", "Your cart has been cleared!")


if __name__ == "__main__":
    root = ctk.CTk()
    cart = Cart(username="TestUser")
    cart.add_item("Laptop", 1000)
    cart.add_item("Phone", 500)
    cart.view_cart()
    root.mainloop()
