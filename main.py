import tkinter as tk
from function import Forget
import csv
from chat import SimpleChatbot


class Text:
    def __init__(self, name: str, password: str):
        # Credentials
        self.name = name
        self.password = password
        self._incorrect_attempts = 0
        # Tkinter window
        self.root = tk.Tk()
        self.root.title("Credentials")
        self.root.geometry("600x400")
        self.label1 = tk.Label(
            self.root,
            text="Provide your credentials",
            font=("Arial", 20),
            background="gray",
            foreground="white",
        )
        self.label1.pack(pady=30)
        self.box_name = tk.Entry(self.root, fg="white", font=("Arial", 15))
        self.box_name.insert(tk.END, "Name")
        self.box_name.bind("<FocusIn>", self.clear_text)
        self.box_name.bind("<FocusOut>", self.restore_default_text)
        self.box_name.pack(padx=2, pady=5)
        self.box_name1 = tk.Entry(self.root, fg="white", font=("Arial", 15))
        self.box_name1.insert(tk.END, "Password")
        self.box_name1.bind("<FocusIn>", self.clear_text)
        self.box_name1.bind("<FocusOut>", self.restore_default_text)
        self.box_name1.pack(padx=5, pady=5)
        self.button1 = tk.Button(
            self.root, text="Submit", fg="black", command=self.submit
        )
        self.button1.pack(padx=5, pady=5)
        self.signbutton = tk.Button(
            self.root, text="Sign In", font=("Arial", 10), command=self.sign
        )
        self.signbutton.pack(padx=5, pady=5)
        self.forgot_text = tk.Button(
            self.root, text="Forget Password", font=("Arial", 10), command=Forget
        )
        self.forgot_text.pack(padx=5, pady=5)
        self.root.mainloop()

    def submit(self):
        credentials_correct = False

        with open("info.csv", "r") as file:
            file = csv.DictReader(file)
            for row in file:
                if (
                    self.box_name.get() == row["name"]
                    and self.box_name1.get() == row["password"]
                ):
                    credentials_correct = True
                    break

        if credentials_correct:
            SimpleChatbot()
        if not credentials_correct:
            self._incorrect_attempts += 1
            if self._incorrect_attempts == 1:
                self._label_root = tk.Label(self.root, text="Credentials Incorrect")
                self._label_root.pack()
            else:
                self._label_root.config(
                    text=f"Incorrect Information Times {self._incorrect_attempts}"
                )

    def sign(self):
        if self.signbutton:
            self.window_sign()
        else:
            pass

    def window_sign(self):
        self.top = tk.Toplevel()
        self.top.geometry("600x400")
        self.top.title("Create a new account")
        self.sign_box = self.create_entry("Name")
        self.sign_box1 = self.create_entry("Last Name")
        self.sign_box2 = self.create_entry("Email")
        self.sign_box3 = self.create_entry("Password")

        self.button = tk.Button(
            self.top, text="Submit", font=("Arial", 20), command=self.submit_sign
        )
        self.button.pack()
        self.top.mainloop()

    def create_entry(self, placeholder):
        entry = tk.Entry(self.top, font=("Arial", 10))
        entry.insert(tk.END, placeholder)
        entry.bind("<FocusIn>", self.clear_text)
        entry.bind("<FocusOut>", self.restore_default_text)
        entry.pack(padx=5, pady=5)
        return entry

    def clear_text(self, event):
        if event.widget.get() in ["Name", "Password", "Last Name", "Email"]:
            event.widget.delete(0, tk.END)

    def restore_default_text(self, event):
        current_text = event.widget.get()

        if not current_text:
            if event.widget == self.box_name:
                event.widget.insert(tk.END, "Name")
            elif event.widget == self.box_name1:
                event.widget.insert(tk.END, "Password")
            elif event.widget == self.sign_box:
                event.widget.insert(tk.END, "Name")
            elif event.widget == self.sign_box1:
                event.widget.insert(tk.END, "Last Name")
            elif event.widget == self.sign_box2:
                event.widget.insert(tk.END, "Email")
            elif event.widget == self.sign_box3:
                event.widget.insert(tk.END, "Password")

    def submit_sign(self):
        name = self.sign_box.get()
        last_name = self.sign_box1.get()
        email = self.sign_box2.get()
        password = self.sign_box3.get()

        if not (name and last_name and email and password):
            self.show_error("All fields are required!")
            return

        with open("info.csv", "a", newline="") as file:
            fieldnames = ["name", "last name", "email", "password"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Check if the file is empty, write header if needed
            if file.tell() == 0:
                writer.writeheader()

            # Write data to CSV
            writer.writerow(
                {
                    "name": name,
                    "last name": last_name,
                    "email": email,
                    "password": password,
                }
            )

        self.top.destroy()
        # Add any additional actions after successful submission

    def show_error(self, message):
        error_label = tk.Label(self.top, text=message, fg="red")
        error_label.pack()


if __name__ == "__main__":
    Text("Tamim", "123")
