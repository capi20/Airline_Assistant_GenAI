# ✈️ Airline AI Assistant ✈️

YourFlight AI Assistant is an interactive chatbot powered by OpenAI’s GPT and DALL·E models. It helps users inquire about airline ticket prices to various destinations and generates vibrant pop-art style images representing vacation spots in the requested city.

![Gradio UI](https://img.shields.io/badge/Powered%20by-Gradio-%23FF6B00?style=flat&logo=gradio)
![OpenAI](https://img.shields.io/badge/API-OpenAI-%2300A67E)

---

## 🚀 Features

- 💬 Chat with an AI assistant trained specifically for airline queries.
- 💸 Retrieve return ticket prices for popular destinations.
- 🎨 Receive a unique pop-art style image of the requested city.
- 🧹 Clear chat history easily.
- 🗣️ Short, courteous, and accurate one-sentence responses from the assistant.

---

## 🛠️ Tech Stack

- Python 3.8+
- Gradio (for UI) 🎛️
- OpenAI API (GPT-4o-mini and DALL·E 3 models) 🤖
- PIL (Python Imaging Library) for image handling 🖼️
- dotenv (for environment variable management) 🌿

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/capi20/Airline_Assistant_GenAI.git
cd Airline_Assistant_GenAI
```

### 2. Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Your OpenAI API Key

Create a .env file in the root of the project:

```bash
# .env
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 5. Usage
Run the app with:

```bash
python main.py
```

This will launch a Gradio web interface in your browser automatically.

---

## 📂 Repository Structure

```
Airline_Assistant_GenAI/
│
├── main.py             # Main entrypoint with Gradio UI setup
├── chat.py             # Chat handling logic including tool calls
├── config.py           # Environment variables and constants
├── image.py            # Image generation with OpenAI DALL·E
├── prompts.py          # System and image prompts
├── tools.py            # Tool for price
└── README.md           # This readme file
```

---

## 💡 Usage

1. Type your queries into the chatbox (e.g., "How much is a ticket to Paris?") ✍️
2. The assistant will reply with the ticket price and generate a pop-art style image of the city. 🏙️🖼️
3. Use the Clear button to reset the chat history. 🧹

---

## 🔧 Customization

- Add more ticket prices: Modify ticket_prices dictionary inside tools.py or query price from your database 💵
- Change AI behavior: Edit the system_message in prompts.py to adjust the assistant’s personality or response style. 🎭
- Image styles: Modify the prompt in prompts.py's gen_image_message function to change the art style. 🎨


