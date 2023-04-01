import sys
from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, \
    QApplication
from backend import Chatbot
import threading


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # instanciate Chatbot class here outside the method so you only need to
        # do it once instead of every time over again when you press the button
        self.chatbot = Chatbot()

        self.setMinimumSize(700, 500)

        # add chat area widget and define location
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 480, 320)
        self.chat_area.setReadOnly(True)

        # add the input field
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10, 340, 480, 40)
        #send message by pressing enter
        self.input_field.returnPressed.connect(self.send_message)

        # add the button
        self.button = QPushButton("Send", self)
        self.button.setGeometry(500, 340, 100, 40)
        self.button.clicked.connect(self.send_message)

        self.show()

    # this method activates when u press the send button
    def send_message(self):
        # get the input from text field
        user_input = self.input_field.text().strip()
        # disply that input in the chat window
        self.chat_area.append(f"<p style='color:#333333'>Me: {user_input}</p>")
        # clear input field
        self.input_field.clear()
        # we send the query to the chatbox and get response through treading to
        # avoid lag as its now loading it in the background
        thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))
        thread.start()

    def get_bot_response(self, user_input):
        # get response from chatbox, we instanciated this chatbox in the __init__ method
        response = self.chatbot.get_repsonse(user_input=user_input)
        # disply response in chat window
        self.chat_area.append(
            f"<p style='color:#333333; background-color:#E9E9E9'>Bot: {response}</p>")


app = QApplication(sys.argv)
main_window = ChatbotWindow()
sys.exit(app.exec())
