import tkinter as tk
from tkinter import ttk
import csv


class Forget:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x400")
        self.root.title("Forget Password Window")

        self._incorrect_attempts = 0
        self._label_root = None
        self.main()
        self.root.mainloop()

    def main(self):
        self.entry1 = tk.Entry(self.root, font=("Arial", 15))
        self.entry1.insert(tk.END, "Name")
        self.entry1.bind("<FocusIn>", self.remover)
        self.entry1.bind("<FocusOut>", self.restore)
        self.entry1.pack(padx=5, pady=5)

        self.entry2 = tk.Entry(self.root, font=("Arial", 15))
        self.entry2.insert(tk.END, "Last Name")
        self.entry2.bind("<FocusIn>", self.remover)
        self.entry2.bind("<FocusOut>", self.restore)
        self.entry2.pack(padx=5, pady=5)

        self.entry3 = tk.Entry(self.root, font=("Arial", 15))
        self.entry3.insert(tk.END, "Email")
        self.entry3.bind("<FocusIn>", self.remover)
        self.entry3.bind("<FocusOut>", self.restore)
        self.entry3.pack(padx=5, pady=5)

        self.button_submit = tk.Button(
            self.root, text="Submit", fg="black", command=self.submit
        )
        self.button_submit.pack(padx=5, pady=5)

    def remover(self, event):
        if event.widget.get() in ["Name", "Last Name", "Email"]:
            event.widget.delete(0, tk.END)

    def restore(self, event):
        if not event.widget.get():
            if event.widget == self.entry1:
                event.widget.insert(tk.END, "Name")
            elif event.widget == self.entry2:
                event.widget.insert(tk.END, "Last Name")
            elif event.widget == self.entry3:
                event.widget.insert(tk.END, "Email")

    def submit(self):
        found_correct_info = False
        with open("info.csv", "r", encoding="UTF-8") as file_reader:
            csv_reader = csv.DictReader(file_reader)
            for row in csv_reader:
                if (
                    self.entry1.get() == row["name"].lower()
                    and self.entry2.get() == row["last name"].lower()
                    and self.entry3.get() == row["email"].lower()
                ):
                    found_correct_info = True
                    self.create_new_password_window()
                    break  # Exit the loop if correct information is found

            if not found_correct_info:
                self._incorrect_attempts += 1
                if self._incorrect_attempts == 1:
                    self._label_root = tk.Label(self.root, text="Incorrect Information")
                    self._label_root.pack()
                else:
                    self._label_root.config(
                        text=f"Incorrect Information Times {self._incorrect_attempts}"
                    )

    def create_new_password_window(self):
        self.top = tk.Toplevel()
        self.top.geometry("600x400")
        self.top.title("Create a New Password")
        self.new_box = tk.Entry(self.top, font=("Arial", 10))
        self.new_box.insert(tk.END, "New Password")
        self.new_box.bind("<FocusIn>", self.clear_text)
        self.new_box.bind("<FocusOut>", self.restore_default_text)
        self.new_box.pack(padx=5, pady=5)
        self.new_box2 = tk.Entry(self.top, font=("Arial", 10))
        self.new_box2.insert(tk.END, "Verify Password")
        self.new_box2.bind("<FocusIn>", self.clear_text)
        self.new_box2.bind("<FocusOut>", self.restore_default_text)
        self.new_box2.pack(padx=5, pady=5)
        self.button = tk.Button(
            self.top, text="Submit", font=("Arial", 20), command=self.password_forget
        )
        self.button.pack()
        self.top.mainloop()

    def clear_text(self, event):
        if event.widget.get() == "New Password":
            event.widget.delete(0, tk.END)
        if event.widget.get() == "Verify Password":
            event.widget.delete(0, tk.END)

    def restore_default_text(self, event):
        if not event.widget.get():
            event.widget.insert(tk.END, "New Password")
        if not event.widget.get():
            event.widget.insert(tk.END, "Verify Password")

    def password_forget(self):
        if (
            self.new_box.get() == self.new_box2.get()
            and self.new_box2.get() == self.new_box.get()
        ):
            with open("info.csv", "r", newline="") as reader:
                csv_reader = csv.DictReader(reader)
                data = list(csv_reader)

            for row in data:
                row["password"] = self.new_box.get()

            with open("info.csv", "w", newline="") as writer:
                fieldnames = data[0].keys()
                csv_writer = csv.DictWriter(writer, fieldnames=fieldnames)
                csv_writer.writeheader()
                csv_writer.writerows(data)

            # Now update the content in the GUI
            self.new_box.delete(0, tk.END)
            self.new_box.insert(tk.END, self.new_box.get())
            self.label1 = tk.Label(text="Successfully Password Updated")
            self.label1.pack()
        else:
            self.label = tk.Label(text="Password Does not match")


if __name__ == "__main__":
    Forget()
