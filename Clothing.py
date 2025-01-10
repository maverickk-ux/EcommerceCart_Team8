import mainpage
import customtkinter as ctk
from cart import Cart


class ClothingPage(Cart):
    def __init__(self, root, username):
        self.root = root
        self.username = username
        self.root.title(f"E-Commerce Product List - Hello {username}")
        self.root.geometry("800x750")
        ctk.set_appearance_mode("dark")

        super().__init__(username) 


        # Initialize cart
        #self.cart = Cart(username=self.username)

        # Item data
        self.items = {
            "Jeans": 100.00,
            "T-Shirt": 150.00,
            "Tank top": 500.00,
            "Belt": 300.00,
            "Heels": 50.00,
            "Off shoulder top": 200.00,
            "Skirt": 400.00,
            "Blazer": 20.00,
        }

        self.cart_labels = {}
        self.size_vars = {}  # Dictionary to store size StringVars
        self.color_vars = {}  # Dictionary to store color StringVars

        # Build the UI
        # self.create_title()
        self.create_item_list()
        self.create_view_cart_button()
        self.create_return_button()
        self.create_total_price_label()

        # Update the UI with initial cart data
        self.update_cart_ui()

    def create_item_list(self):
        """Create a scrollable frame with items."""
        scrollable_frame = ctk.CTkScrollableFrame(self.root, width=650, height=500)
        scrollable_frame.pack(pady=20, padx=20, fill="both", expand=True)

        for i, (item, price) in enumerate(self.items.items()):
            item_frame = ctk.CTkFrame(scrollable_frame, corner_radius=10)
            item_frame.grid(row=i, column=0, pady=10, padx=10, sticky="ew")
            
            # Configure grid columns to align items properly
            item_frame.columnconfigure(0, weight=1)  # Left side for labels
            item_frame.columnconfigure(1, weight=0)  # Dropdowns
            item_frame.columnconfigure(2, weight=0)  # Buttons and quantity

            # Item title
            item_label = ctk.CTkLabel(item_frame, text=item, font=("Arial", 18, "bold"))
            item_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

            # Item price
            price_label = ctk.CTkLabel(item_frame, text=f"Price: ${price:.2f}", font=("Arial", 14))
            price_label.grid(row=1, column=0, padx=10, sticky="w")

            # Size dropdown
            size_var = ctk.StringVar(value="Small")  # Default size
            size_dropdown = ctk.CTkOptionMenu(item_frame, variable=size_var, width=15, values=["Small", "Medium", "Large"])
            size_dropdown.grid(row=0, column=1, padx=10, sticky="w")
            self.size_vars[item] = size_var  # Store the variable for this item

            # Color dropdown
            color_var = ctk.StringVar(value="Red")  # Default color
            color_dropdown = ctk.CTkOptionMenu(item_frame, variable=color_var, width=15, values=["Red", "Green", "Brown"])
            color_dropdown.grid(row=1, column=1, padx=10, sticky="w")
            self.color_vars[item] = color_var  # Store the variable for this item

            # Remove button
            remove_button = ctk.CTkButton(
                item_frame,
                text="-",
                width=30,
                fg_color="#fd5c63",
                hover_color="red",
                command=lambda i=item: self.remove_from_cart(i, self.size_vars[i].get(), self.color_vars[i].get())
            )
            remove_button.grid(row=0, column=2, padx=5, sticky="e")

            # Add button
            add_button = ctk.CTkButton(
                item_frame,
                text="+",
                width=30,
                fg_color="#03C03C",
                hover_color="green",
                command=lambda i=item: self.add_to_cart(i, self.size_vars[i].get(), self.color_vars[i].get())
            )
            add_button.grid(row=0, column=3, padx=5, sticky="e")

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

    def add_to_cart(self, item, size, color):
        """Add an item to the cart."""
        key = f"{item} ({size}) - {color}"  # Create a unique key
        self.add_item(key, self.items[item])
        self.update_cart_ui()

    def remove_from_cart(self, item, size, color):
        """Remove an item from the cart."""
        key = f"{item} ({size}) - {color}"  # Create a unique key
        self.remove_item(key)
        self.update_cart_ui()

    def update_cart_ui(self):
        """Update the UI to reflect the cart state."""
        cart = self.get_cart()
        for item, label in self.cart_labels.items():
            total_quantity = sum(
                cart[key]["quantity"] for key in cart if key.startswith(item)
            )
            label.configure(text=f"Quantity: {total_quantity}")
        self.update_total_price()

    def update_total_price(self):
        """Update the total price label."""
        total_price = self.calculate_total_price()
        self.total_price_label.configure(text=f"Total Price: ${total_price:.2f}",font=("Ariel",20))

    def view_cartT(self):
        self.view_cart()

    def return_to_main(self):
        self.root.destroy()
        root = ctk.CTk()
        mainpage.MainPage(root, self.username)
        root.mainloop()


if __name__ == "__main__":
    root = ctk.CTk()
    app = ClothingPage(root, "TestUser")
    root.mainloop()
