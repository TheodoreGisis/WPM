import tkinter as tk
import time
from tkinter import messagebox

# List of sentences for different difficulty levels
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "I want to build a typing speed test.",
    "Python programming is fun and versatile.",
    "Typing games can improve accuracy and speed.",
    "Challenge yourself with harder sentences.",
    "Mastering typing skills requires practice.",
    "The wizard quickly jinxed the gnomes.",
    "Advanced users often type without errors.",
    "Each level brings a new typing challenge.",
    "Perfection in typing comes with persistence."
]

class TypingTestApp:
    def __init__(self, root):
        self.root = root
        self.level = 0
        self.start_time = None
        self.current_sentence = sentences[self.level]

        # Configure window
        self.root.title("Typing Speed Test")
        self.root.geometry("600x400")

        # Level label
        self.level_label = tk.Label(root, text=f"Level {self.level + 1}", font=("Helvetica", 16))
        self.level_label.pack(pady=10)

        # Sentence display
        self.sentence_label = tk.Label(root, text=self.current_sentence, font=("Helvetica", 14), wraplength=500, justify="center")
        self.sentence_label.pack(pady=20)

        # Entry box for typing
        self.entry = tk.Entry(root, font=("Helvetica", 14), width=50)
        self.entry.pack(pady=10)
        self.entry.bind("<KeyRelease>", self.check_input)

        # Feedback message
        self.feedback_label = tk.Label(root, text="", font=("Helvetica", 12))
        self.feedback_label.pack(pady=10)

        # Start button
        self.start_button = tk.Button(root, text="Start Level", command=self.start_level)
        self.start_button.pack(pady=20)

    def start_level(self):
        """Initialize the level and start the timer."""
        self.entry.delete(0, tk.END)  # Clear the entry box
        self.start_time = time.time()  # Set the start time here
        self.feedback_label.config(text="")

    def check_input(self, event):
        """Check the user's input in real-time."""
        if self.start_time is None:  # Ensure the level has been started
            return
        
        user_input = self.entry.get()
        
        # Provide real-time feedback
        if user_input == self.current_sentence[:len(user_input)]:
            # Correct input so far
            self.feedback_label.config(text="Typing accurately!", fg="green")
            if user_input == self.current_sentence:
                self.complete_level()
        else:
            # Incorrect input
            self.feedback_label.config(text="Typing mistake detected!", fg="red")

    def complete_level(self):
        """Handle level completion."""
        if self.start_time is None:
            return  # Avoid calculation if start_time is not set
        
        time_taken = time.time() - self.start_time  # Calculate time taken
        messagebox.showinfo("Level Complete", f"Level {self.level + 1} complete!\nTime taken: {time_taken:.2f} seconds")
        
        # Reset start time for next level
        self.start_time = None
        
        # Move to the next level or end game
        self.level += 1
        if self.level < len(sentences):
            self.current_sentence = sentences[self.level]
            self.level_label.config(text=f"Level {self.level + 1}")
            self.sentence_label.config(text=self.current_sentence)
            self.entry.delete(0, tk.END)  # Clear the entry box for the next level
        else:
            self.feedback_label.config(text="Congratulations! You've completed all levels!", fg="blue")
            self.entry.config(state="disabled")  # Disable further input

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTestApp(root)
    root.mainloop()