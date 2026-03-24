import nltk
from nltk.chat.util import Chat, reflections

reflections = {
  "i am": "you are",
  "i was": "you were",
  "i'll": "you will",
  "i'm": "you are",
  "i'd": "you would",
  "i've": "you have",
  "i'll": "you will",
  "my": "your",
  "you are": "I am",
  "you were": "I was",
  "you've": "I have",
  "you'll": "I will",
  "your": "my",
  "yours": "mine",
  "you": "me",
  "me": "you"
}

pairs = [
  [
      r"my name is {.*}",
      ["Hello %1, How are you today?", "Hi %1! Nice to meet you."]
  ],
  [
      r"hi|hello|hey",
      ["Hello!", "Hey there!", "Hi :)"]
  ],
  [
      r"how are you?",
      ["I'm doing good, thank you!", "I'm great! How about you?"]
  ],
  [
      r"sorry (.*)",
      ["It's okay.", "No worries!", "Don't stress about it."]
  ],
  [
      r"i am (.*)",
      ["Why are you %1?", "How long have you been %1?", "Do you enjoy being %1?"]
  ],
  [
      r"i'm (.*)",
      ["Why are you %1?", "How does being %1 make you feel?"]
  ],
  [
      r"what is your name?",
      ["I am a chatbot created using NLTK.", "You can call me ChatBot!"]
  ],
  [
      r"who created you?",
      ["I was created by a Python developer like you!", "Someone awesome built me :D"]
  ],
  [
      r"where are you from?",
      ["I live in your computer!", "I exist everywhere :D"]
  ],
  [
      r"what can you do?",
      ["I can chat with you!", "I can answer simple questions."]
  ],
  [
      r"quit",
      ["Bye! Take care.", "Goodbye! Have a great day!"]
  ],
  [
      r"(.*) help (.*)",
      ["I can try to help you.", "Sure! Tell me more."]
  ],
  [
      r"(.*) your hobby?",
      ["I love chatting with people!", "Talking to you is my hobby :D"]
  ],
  [
      r"(.*) (location|city)?",
      ["I am everywhere.", "I exist virtually."]
  ],
  [
      r"(.*) weather (.*)",
      ["I can't check weather right now, but I hope it's nice!"]
  ],
  [
      r"(.*)",
      ["Interesting...", "Tell me more.", "I see.", "Can you elaborate?"]
  ],
  [
      r"who is (.*)?",
      ["1% is a great person!"]
  ]
]

def chat():
    print("Hi! I am a chatbot created by Codingal Edu. Pvt. Lim. for your serive")
    chat = Chat(pairs, reflections)
    chat.converse(quit = "quit")

if __name__ == "__main__":
    chat()