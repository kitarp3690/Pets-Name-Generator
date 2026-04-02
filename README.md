# 🐾 Animal Name Suggester — LangChain + Groq

A simple CLI app that takes an **animal** and a **color** as input and returns
**5 creative name suggestions** using Groq's blazing-fast LLM API via LangChain.

---

## 🚀 Setup

### 1. Clone the repo
```bash
git clone https://github.com/your-username/Pets-Name-Generator.git
cd Pets-Name-Generator
```

### 2. Create and activate a virtual environment
```bash
python -m venv llmenv
# Windows
llmenv\Scripts\activate
# macOS/Linux
source llmenv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set your Groq API key
```bash
# Windows
set GROQ_API_KEY=gsk_your-key-here

# macOS/Linux
export GROQ_API_KEY="gsk_your-key-here"
```
> Get your free API key at [https://console.groq.com](https://console.groq.com)

### 5. Run the app
```bash
python main.py
```

---

## 💡 Example

```
🐾 Animal Name Suggester (powered by Groq + LangChain)
---------------------------------------------
Enter animal name (e.g. cat, dog, rabbit): rabbit
Enter color (e.g. golden, black, spotted): white

✨ Here are 5 name suggestions for your white rabbit:

1. Pearl
2. Snowdrop
3. Ghost
4. Cotton
5. Luna
```

---

## 🧱 Project Structure

```
Pets-Name-Generator/
├── main.py            # Main application
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

---

## ⚙️ How It Works

| Component | Role |
|---|---|
| `ChatGroq` | Connects to Groq's LLM API |
| `ChatPromptTemplate` | Structures the system + user prompt |
| `StrOutputParser` | Parses the LLM response to plain text |
| LCEL `\|` chain | Wires prompt → LLM → parser together |

---

## 🤖 Model Used

`llama-3.1-8b-instant` — fast and free on Groq.

Other supported models you can swap in `main.py`:

| Model | Speed | Quality |
|---|---|---|
| `llama-3.1-8b-instant` | ⚡ Fastest | Good |
| `llama-3.3-70b-versatile` | Medium | ⭐ Best |
| `mixtral-8x7b-32768` | Fast | Good |

---

## 📦 Dependencies

```
langchain
langchain-groq
langchain-core
groq
```

---

## 📄 License
MIT