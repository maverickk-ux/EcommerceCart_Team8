import Electronics, Clothing, Groceries
import customtkinter as ctk
from PIL import Image, ImageTk
from cart import Cart

class MainPage():
    def __init__(self, root,username):
        self.root = root
        self.username=username
        self.root.title(f"E-Commerce App: Hello {self.username}, Welcome to Main page!!")
        self.root.geometry("1100x600")

        self.cart=Cart(username)

        # Set appearance and theme
        ctk.set_appearance_mode("dark")  # Options: "dark", "light"
        ctk.set_default_color_theme("blue")  # Theme options: "blue", "green", "dark-blue"

        # Load images
        self.electronics_img = self.load_image("electronics_image.png", (300, 250))
        self.clothing_img = self.load_image("clothing_image.png", (300, 250))
        self.groceries_img = self.load_image("groceries_image.png", (300, 250))

        # Build UI components
        self.create_header()
        self.create_buttons()
        self.create_categories()

    def load_image(self, image_path, s):
        """Load and resize images for category icons."""
        img = Image.open(image_path)
        return ctk.CTkImage(img,size=s)

    def create_header(self):
        """Create the header label."""
        header_label = ctk.CTkLabel(
            self.root, text="E-Commerce Cart System",
            font=("Helvetica", 24, "bold"),
            text_color="#F0F8FF"
        )
        header_label.pack(pady=20)

    def create_buttons(self):
        """Create the top-right buttons for viewing the cart and checkout."""
        buttons_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        buttons_frame.pack(pady=10)

        view_cart_button = ctk.CTkButton(
            buttons_frame, text="View Cart", width=150, command=self.view_cart
        )
        view_cart_button.grid(row=0, column=0, padx=20)

    def create_categories(self):
        """Create the category frames with images and buttons."""
        categories_frame = ctk.CTkFrame(self.root)
        categories_frame.pack(pady=20, fill="x", expand=True)
        categories_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Electronics Category
        self.create_category(
            categories_frame, "Electronics", self.electronics_img, self.view_electronics, 0, 0
        )

        # Clothing Category
        self.create_category(
            categories_frame, "Clothing", self.clothing_img, self.view_clothing, 0, 1
        )

        # Groceries Category
        self.create_category(
            categories_frame, "Groceries", self.groceries_img, self.view_groceries, 0, 2
        )

    def create_category(self, parent, title, image, command, row, column):
        """Helper method to create a category frame."""
        category_frame = ctk.CTkFrame(parent, width=250, height=300, corner_radius=10)
        category_frame.grid(row=row, column=column, padx=20, pady=10)

        category_label = ctk.CTkLabel(category_frame, text=title, font=("Arial", 18, "bold"))
        category_label.pack(pady=10)

        category_image_label = ctk.CTkLabel(category_frame, image=image, text="")
        category_image_label.pack()

        category_button = ctk.CTkButton(category_frame, text=f"View {title}", command=command)
        category_button.pack(pady=10)

    # Button Actions
    def view_cart(self):
        self.cart.view_cart()


    def view_electronics(self):
        """Open the Electronics page."""
        self.root.destroy()  # Close the main page
        root = ctk.CTk()
        Electronics.ElectronicsPage(root,username=self.username)  # Call the Electronics page from the module
        root.mainloop()

    def view_clothing(self):
        """Open the Clothing page."""
        self.root.destroy()  # Close the main page
        root = ctk.CTk()
        Clothing.ClothingPage(root,username=self.username)  # Call the Clothing page from the module
        root.mainloop()

    def view_groceries(self):
        """Open the Groceries page."""
        self.root.destroy()  # Close the main page
        root = ctk.CTk()
        Groceries.GroceriesPage(root,username=self.username)  # Call the Groceries page from the module
        root.mainloop()

# class Products:

#     def add_item(self, item_name, item_price):
#         """Add an item to the cart."""
#         if item_name in self.cart:
#             self.cart[item_name]["quantity"] += 1
#         else:
#             self.cart[item_name] = {"quantity": 1, "price": item_price}
#         self.save_cart()

#     def remove_item(self, item_name):
#         """Remove an item from the cart."""
#         if item_name in self.cart:
#             self.cart[item_name]["quantity"] -= 1
#             if self.cart[item_name]["quantity"] <= 0:
#                 del self.cart[item_name]
#             self.save_cart()

#     def clear_cart(self):
#         """Clear all items from the cart."""
#         self.cart = {}
#         self.save_cart()
#         #messagebox.showinfo("Cart Cleared", "Your cart has been cleared!")

if __name__ == "__main__":
    root = ctk.CTk()
    app = MainPage(root,"Testuser")
    root.mainloop()