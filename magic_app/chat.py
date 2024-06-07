import nltk
from nltk.chat.util import Chat, reflections
from tkinter import *
from datetime import datetime


class SimpleChatbot:
    def __init__(self):
        self.window = Tk()
        self.window.title("Imessage")

        self.input_entry = Entry(self.window)
        self.input_entry.pack(side="bottom", fill="x")

        self.chat_history = Text(
            self.window, wrap="word", state="disabled", height=15, width=40
        )
        self.chat_history.pack(side="left", fill="both", padx=10, pady=10)

        scrollbar = Scrollbar(self.window, command=self.chat_history.yview)
        scrollbar.pack(side="left", fill="y")

        self.chat_history.config(yscrollcommand=scrollbar.set)

        send_button = Button(self.window, text="Send", command=self.send_message)
        send_button.pack(side="bottom")

        self.pairs = [
            ["hi|hello|hey", ["Hello!", "Hi there!", "How can I help you today?"]],
            ["bye|goodbye", ["Goodbye!", "Bye!", "Have a great day!"]],
            ["your name", ["Tamim Bot :)"]],
            [
                "how are you",
                [
                    "I'm just a virtual assistant bot made by Tamim, if he's good I am good. Anyway, thanks for asking!"
                ],
            ],
            ["Who made you?", ["I was made by Tamim"]],
            ["Where does Tamim Study?", ["He is a freshman at Luther College."]],
            [
                "Ronaldo or Messi",
                ["Messi does not speak English, therefore let's go by Ronaldo."],
            ],
            [
                "What other languages do you speak?",
                ["I only know English, but will work on my other skills"],
            ],
            [
                "What is your gender? ",
                ["Have a shame man, of course I am a man!"],
            ],
            ["Help me", ["Dang, ask my boss for permission."]],
            ["I did", ["Ok, what do you want?"]],
            ["Who is your boss?", ["Tamim"]],
            ["Who are you?", ["I am a virtual assistant made by Tamim."]],
            [
                "What is the time?",
                [
                    f"It's something around {datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')}"
                ],
            ],
        ]

        self.chat = Chat(self.pairs, reflections)

        self.window.mainloop()

    def send_message(self):
        user_input = self.input_entry.get()
        self.update_chat_history(f"You: {user_input}")

        # Add a 2-second delay before getting Tamim's response
        self.window.after(2000, self.get_tamim_response, user_input)

        self.input_entry.delete(0, "end")

    def get_tamim_response(self, user_input):
        response = self.chat.respond(user_input)
        self.update_chat_history(f"Tamim: {response}")

    def update_chat_history(self, message):
        self.chat_history.config(state="normal")
        self.chat_history.insert("end", message + "\n")
        self.chat_history.config(state="disabled")
        self.chat_history.yview("end")


if __name__ == "__main__":
    nltk.download("punkt")
    SimpleChatbot()
