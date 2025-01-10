import mainpage
import customtkinter as ctk
from cart import Cart


class GroceriesPage(Cart):
    def __init__(self, root,username):
        self.root = root
        self.username=username
        self.root.title(f"E-Commerce Product List - Hello {username}")
        self.root.geometry("800x750")
        ctk.set_appearance_mode("dark")


        super().__init__(username) #instead of creating instance now calling
                                   #class constructor and now the the methods
                                   #add_item, remove_item, view_cart, save_cart
                                   #can be directly used

        # Initialize cart
        #self.cart = Cart(username=self.username)

        # Item data
        self.items = {
            "Apples": {"price": 1.00, "expiry": "10 days"},
            "Bananas": {"price": 0.50, "expiry": "5 days"},
            "Milk": {"price": 5.00, "expiry": "7 days"},
            "Bread": {"price": 2.50, "expiry": "3 days"},
            "Chicken": {"price": 6.00, "expiry": "2 days"},
            "Rice": {"price": 3.50, "expiry": "30 days"},
            "Butter": {"price": 1.75, "expiry": "20 days"},
            "Canned Soup": {"price": 1.25, "expiry": "1 year"},
            "Pasta Sauce": {"price": 2.25, "expiry": "6 months"},
            "Eggs": {"price": 1.20, "expiry": "10 days"},
        }

        self.cart_labels = {}

        # Build the UI
        self.create_title()
        self.create_item_list()
        self.create_view_cart_button()
        self.create_return_button()
        self.create_total_price_label()

        # Update the UI with initial cart data
        self.update_cart_ui()

    def create_title(self):
        """Create the title label."""
        title_label = ctk.CTkLabel(self.root, text="Groceries", font=("Diamonds", 24, "bold"))
        title_label.pack(pady=10)

    def create_item_list(self):
        """Create a scrollable frame with items."""
        scrollable_frame = ctk.CTkScrollableFrame(self.root, width=650, height=500)
        scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)

        for i, (item, details) in enumerate(self.items.items()):
            item_frame = ctk.CTkFrame(scrollable_frame, corner_radius=10)
            item_frame.grid(row=i, column=0, pady=10, padx=10, sticky="ew")

            item_frame.columnconfigure(0, weight=1)  # Left side for labels
            item_frame.columnconfigure(1, weight=0)  # Buttons and quantity

            # Item title
            item_label = ctk.CTkLabel(item_frame, text=item, font=("Arial", 18, "bold"))
            item_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

            # Item price
            price_label = ctk.CTkLabel(item_frame, text=f"Price: ${details['price']:.2f}", font=("Arial", 14))
            price_label.grid(row=1, column=0, padx=10, sticky="w")

            # Expiry description
            expiry_label = ctk.CTkLabel(item_frame, text=f"Warranty: {details['expiry']}", font=("Arial", 12, "italic"))
            expiry_label.grid(row=2, column=0, padx=10, pady=0, sticky="w")
            
            # Remove button
            remove_button = ctk.CTkButton(
                item_frame, text="-", width=30, fg_color="#fd5c63", hover_color="red",
                command=lambda i=item: self.remove_from_cart(i)
            )
            remove_button.grid(row=0, column=2, padx=10, sticky="e")

            # Add button
            add_button = ctk.CTkButton(
                item_frame, text="+", width=30,fg_color="#03C03C",hover_color="green", command=lambda i=item: self.add_to_cart(i)
            )
            add_button.grid(row=0, column=3, padx=10, sticky="e")

            # Quantity label
            cart_label = ctk.CTkLabel(item_frame, text="Quantity: 0", font=("Arial", 14))
            cart_label.grid(row=0, column=4, padx=10, sticky="e")

            self.cart_labels[item] = cart_label

    def create_view_cart_button(self):
        """Create the View Cart button."""
        view_cart_button = ctk.CTkButton(
            self.root, text="View Cart", fg_color="#007FFF", hover_color="blue", command=self.view_cart
        )
        view_cart_button.pack(pady=10)

    def create_return_button(self):
        """Create the Return to Main Page button."""
        return_button = ctk.CTkButton(
            self.root, text="Return to Main Page", fg_color="#FF8C00", hover_color="orange", command=self.return_to_main
        )
        return_button.pack(pady=0, padx=20)

    def create_total_price_label(self):
        """Create a dynamic total price label."""
        self.total_price_label = ctk.CTkLabel(self.root, text="Total Price: $0.00", font=("Arial", 14, "bold"))
        self.total_price_label.pack(pady=5, side="bottom", anchor="se")

    def add_to_cart(self, item):
        """Add an item to the cart."""
        self.add_item(item, self.items[item]["price"])
        self.update_cart_ui()

    def remove_from_cart(self, item):
        """Remove an item from the cart."""
        self.remove_item(item)
        self.update_cart_ui()

    def update_cart_ui(self):
        """Update the UI to reflect the cart state."""
        cart = self.get_cart()
        for item, label in self.cart_labels.items():
            quantity = cart.get(item, {}).get("quantity", 0)
            label.configure(text=f"Quantity: {quantity}")
        self.update_total_price()

    def update_total_price(self):
        """Update the total price label."""
        total_price = self.calculate_total_price()
        self.total_price_label.configure(text=f"Total Price: ${total_price:.2f}",font=("Ariel",20))

    def view_cartt(self):
        self.view_cart()

    def return_to_main(self):
        self.root.destroy()
        root = ctk.CTk()
        mainpage.MainPage(root,username=self.username)
        root.mainloop()


if __name__ == "__main__":
    root = ctk.CTk()
    app = GroceriesPage(root,"TestUser")
    root.mainloop()
