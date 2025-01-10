import customtkinter as ctk
from tkinter import messagebox
import time
import threading
import random
import cart

class PaymentPage(ctk.CTkToplevel):
    def __init__(self, parent, receipt_details, go_to_home_callback,username):
        super().__init__(parent)
        self.title("Payment Page")
        self.geometry("500x500")

        self.c = cart.Cart(username=username)
        self.receipt_details = receipt_details
        self.go_to_home_callback = go_to_home_callback
        self.payment_status = ctk.StringVar(value="Pending")
        self.transaction_id = None
        self.username=username

        # Ensure window is on top
        self.lift()
        self.focus_force()

        #Display Username
        ctk.CTkLabel(self,text=f"User: {self.username}",font=("Ariel",16,"bold")).pack(pady=10)

         # Receipt Display
        ctk.CTkLabel(self, text="Receipt Details:", font=("Arial", 14, "bold")).pack(pady=10)
        self.receipt_text = ctk.CTkTextbox(self, width=450, height=100)

        # Insert the receipt details into the Textbox
        self.receipt_text.configure(state="normal")  # Enable editing the textbox
        self.receipt_text.insert("1.0", self.receipt_details)  # Insert the receipt details at the start
        self.receipt_text.configure(state="disabled")  # Disable editing again
        self.receipt_text.pack(pady=10)
            
        # Payment Method Selection
        ctk.CTkLabel(self, text="Select Payment Method:", font=("Arial", 12)).pack(pady=5)
        self.payment_method = ctk.StringVar(value="Credit Card")
        ctk.CTkOptionMenu(self, variable=self.payment_method,
                          values=["Credit Card", "Cash on Delivery", "UPI", "Wallet"]).pack(pady=10)

        # Progress Bar
        self.progress_label = ctk.CTkLabel(self, text="Payment Status: Pending", font=("Arial", 12))
        self.progress_label.pack(pady=5)
        self.progress_bar = ctk.CTkProgressBar(self, width=400)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=10)

        # Buttons
        self.confirm_button = ctk.CTkButton(self, text="Confirm Payment", command=self.start_payment)
        self.confirm_button.pack(pady=10)

        self.cancel_button = ctk.CTkButton(self, text="Cancel Payment", command=self.cancel_payment, state="disabled")
        self.cancel_button.pack(pady=5)

    def start_payment(self):
        self.transaction_id = f"TXN{random.randint(100000, 999999)}"  # Generate transaction ID
        self.confirm_button.configure(state="disabled")
        self.cancel_button.configure(state="normal")
        threading.Thread(target=self.process_payment).start()

    def process_payment(self):
        try:
            for i in range(1, 11):  
                time.sleep(0.5)
                self.progress_bar.set(i / 10)
                self.progress_label.configure(text=f"Payment Status: {'Processing' if i < 10 else 'Completed'}")
                if self.payment_status.get() == "Failed":
                    break
            if self.payment_status.get() == "Failed":
                self.display_status("Failed", "red")
            else:
                self.payment_status.set("Completed") 
                self.display_status("Completed", "green")
                messagebox.showinfo("Thanking You","Thank YOU for shopping with us")
                
        finally:
            self.confirm_button.configure(state="normal")
            self.cancel_button.configure(state="disabled")

    def cancel_payment(self):
        self.payment_status.set("Failed")
        self.progress_label.configure(text="Payment Status: Failed")
        self.progress_bar.set(0)

    def display_status(self, status, color):
        ctk.CTkLabel(self, text=f"Payment {status}!", font=("Arial", 12, "bold"),
                text_color=color).pack(pady=10)        

# # Test Script
# if __name__ == "__main__":
#     ctk.set_appearance_mode("System")  # Use system light/dark mode
#     ctk.set_default_color_theme("blue")  # Default color theme

#     def go_to_home():
#         print("Returning to Home Page...")

#     # Simulated Receipt
#     receipt_details = """
# Item 1: ₹500
# Item 2: ₹300
# Discount: ₹50
# -------------------
# Total: ₹750
# """

#     root = ctk.CTk()
#     root.title("Main Application")
#     root.geometry("500x500")

#     def open_payment_page():
#         PaymentPage(root, receipt_details, go_to_home,username="TestUser")

#     # Button to Open Payment Page
#     open_button = ctk.CTkButton(root, text="Open Payment Page", command=open_payment_page)
#     open_button.pack(pady=20)

#     root.mainloop()
