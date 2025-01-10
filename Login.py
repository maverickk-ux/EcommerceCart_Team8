import mainpage
import customtkinter as ctk
import tkinter
from tkinter import messagebox
import customtkinter
from PIL import ImageTk, Image
import json
import os

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x440")
        self.root.title("Login")

        # Set appearance and theme
        customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
        customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green

        # Background image
        self.img1 = ImageTk.PhotoImage(Image.open("pattern.png"))
        self.l1 = customtkinter.CTkLabel(master=root, image=self.img1)
        self.l1.pack()

        # Create custom frame
        self.frame = customtkinter.CTkFrame(master=self.l1, width=350, height=320, corner_radius=15)
        self.frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        # Add widgets
        self.add_widgets()

    def add_widgets(self):
        # Welcome Label
        l2 = customtkinter.CTkLabel(
            master=self.frame, text="Welcome to Ecommerce Cart!!", font=("Century Gothic", 18)
        )
        l2.place(x=35, y=45)

        # Username Entry
        self.entry1 = customtkinter.CTkEntry(master=self.frame, width=220, placeholder_text="Username")
        self.entry1.place(x=60, y=110)

        # Password Entry
        self.entry2 = customtkinter.CTkEntry(master=self.frame, width=220, placeholder_text="Password", show="*")
        self.entry2.place(x=60, y=155)

        # Login Button
        button1 = customtkinter.CTkButton(
            master=self.frame, width=220, text="Login", command=self.login_function, corner_radius=6
        )
        button1.place(x=60, y=220)

        # Signup Button
        button2 = customtkinter.CTkButton(
            master=self.frame,height=10, width=100, text="Signup", command=self.signup_function, corner_radius=6, bg_color="#2B2B2B"
        )
        button2.place(x=180, y=260)

    def login_function(self):
        username = self.entry1.get()
        password = self.entry2.get()

        try:
            # Load users from users.json to check login credentials
            if os.path.exists("users.json") and os.path.getsize("users.json") > 0:
                with open("users.json", "r") as file:
                    users = json.load(file)
            else:
                users = {}

            if username not in users:
                messagebox.showinfo("Account invalid", "Please signup!")
            elif users[username] != password:  # Check if the password matches
                messagebox.showerror("Login Failed", "Incorrect password!")
            else:
                messagebox.showinfo("Success", "Login successful!")
                self.root.destroy()
                self.open_main_page(username)
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Data corrupted. Please contact support.")
    
    def signup_function(self):
        username = self.entry1.get()
        password = self.entry2.get()
        
        if not username or not password:
            messagebox.showerror("Error", "Username and Password cannot be empty!")
            return

        if os.path.exists("users.json") and os.path.getsize("users.json") > 0:
            try:
                with open("users.json", "r") as f:
                    users = json.load(f)
            except json.JSONDecodeError:
                messagebox.showerror("Error", "Data corrupted. Initializing a new file.")
                users = {}
        else:
            users = {}

        if username in users:
            messagebox.showerror("Error", "User already exists!")
        else:
            users[username] = password  # Store username and password
            with open("users.json", "w") as f:
                json.dump(users, f)
            messagebox.showinfo("Success", "Signup successful!")
        
    def open_main_page(self,username):
        root = ctk.CTk()
        mainpage.MainPage(root,username)
        root.mainloop()



if __name__ == "__main__":
    root = customtkinter.CTk()
    app = LoginPage(root)
    root.mainloop()