import tkinter as tk
from tkinter import messagebox
from app import TypingTestApp

class LoginPage():

    def __init__(self,root):
        self.root = root

        # Configure window
        self.root.title("Login Page")
        self.root.geometry("600x400")

        #Label where you are putting your Username to play
        self.name_label = tk.Label(root, text="Enter your name:")
        self.name_label.pack(pady=10)
        #This creates a label widget with the text "Enter your name:" to prompt the user to input their name
        self.name_entry = tk.Entry(root,font=("Helvetica", 14), width=30)
        self.name_entry.pack(pady=10)

        #Label where you are puting your email to play
        self.email_label = tk.Label(root, text="Enter your Email:")
        self.email_label.pack(pady=10)

        #This creates a label widget with the text "Enter your Email:" to prompt the user to input their name
        self.email_entry = tk.Entry(root,font=("Helvetica", 14), width=30)
        self.email_entry.pack(pady=10)

        #Create button for Playing the game
        self.login_button = tk.Button(root, text="Login", command=self.login)
        self.login_button.pack(pady=10)


        #Add functionality to the 'Enter'.Every time you hit enter you start the game
        self.root.bind('<Return>', self.on_enter)


    def open_game_window(self):
        # Create a new window for the typing game
        game_window = tk.Toplevel(self.root)  # Toplevel creates a new window
        game_window.title("Typing Speed Test")
        game_window.geometry("600x400")

        # Create an instance of the TypingTestApp
        typing_game = TypingTestApp(game_window)       

    def login(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        messagebox.showinfo("Welcome", f"Hello, {name}! Let's start the game.")
        print(email)
        self.root.withdraw()

        self.open_game_window()

    def on_enter(self,event):
        self.login()

root = tk.Tk()
login = LoginPage(root)
root.mainloop()