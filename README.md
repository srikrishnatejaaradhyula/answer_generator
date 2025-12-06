# 🤖 AI Answer Generator Agent

An intelligent AI agent that reads questions from files (TXT, PDF, Word documents), generates answers using Google Gemini AI, and updates the files with the answers.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-Powered-green.svg)
![Gemini](https://img.shields.io/badge/Google-Gemini_AI-orange.svg)

## ✨ Features

- 📄 **Multi-Format Support** - Works with TXT, PDF, and Word documents (.docx)
- 🧠 **AI-Powered Answers** - Uses Google Gemini AI for intelligent responses
- 🔄 **Auto File Updates** - Automatically updates files with generated answers
- 🏗️ **LangGraph Architecture** - Built using LangGraph for robust workflow management
- 🔒 **Secure Configuration** - API keys stored in environment variables

## 📁 Supported File Types

| Format | Read | Write | Notes |
|--------|------|-------|-------|
| `.txt` | ✅ | ✅ | Plain text files |
| `.md` | ✅ | ✅ | Markdown files |
| `.docx` | ✅ | ✅ | Microsoft Word documents |
| `.pdf` | ✅ | ❌ | Read-only, output saved as `.docx` |
| `.json` | ✅ | ✅ | JSON files |

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd answer_genrate
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   
   # Windows
   .venv\Scripts\activate
   
   # Linux/Mac
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env and add your API key
   GOOGLE_API_KEY=your_api_key_here
   GEMINI_MODEL=gemini-2.5-flash
   ```

### Usage

1. **Create a file with questions** (e.g., `questions.txt`)
   ```
   1. What is the capital of France?
   2. Explain machine learning in simple terms.
   3. What is the speed of light?
   ```

2. **Update `main.py`** with your filename
   ```python
   filename = "questions.txt"  # or "questions.docx" or "questions.pdf"
   ```

3. **Run the agent**
   ```bash
   python main.py
   ```

4. **Check the output** - Your file will be updated with answers!

## 📂 Project Structure

```
answer_genrate/
├── .env                  # Environment variables (API keys) - DO NOT COMMIT
├── .env.example          # Template for environment variables
├── .gitignore            # Git ignore rules
├── requirements.txt      # Python dependencies
├── main.py               # Entry point - run this to start the agent
├── graph.py              # LangGraph workflow definition
├── file_process.py       # File processing and LLM integration
├── tools.py              # Custom tools for reading/writing files
├── example.txt           # Sample questions file
└── README.md             # This file
```

## 🛠️ How It Works

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│  Read File  │ ──▶ │  Generate    │ ──▶ │ Write File  │
│  (any type) │     │  Answers     │     │ (updated)   │
└─────────────┘     │  with Gemini │     └─────────────┘
                    └──────────────┘
```

1. **Read File** - The agent reads the content from your file (TXT, PDF, or DOCX)
2. **Generate Answers** - Google Gemini AI processes the questions and generates answers
3. **Write File** - The file is updated with the questions and their answers

## 🔧 Configuration

### Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `GOOGLE_API_KEY` | Your Google Gemini API key | Required |
| `GEMINI_MODEL` | Gemini model to use | `gemini-2.5-flash` |

### Available Models

- `gemini-2.5-flash` - Fast and efficient (recommended)
- `gemini-2.5-pro` - More capable, slower
- `gemini-1.5-flash` - Previous generation, stable

## 📝 Examples

### Text File Example

**Input (`questions.txt`):**
```
1. What is Python?
2. Who created JavaScript?
```

**Output (after running):**
```
1. What is Python?
Python is a high-level, interpreted programming language known for its simplicity and readability.

2. Who created JavaScript?
JavaScript was created by Brendan Eich in 1995.
```

### Word Document Example

Works the same way with `.docx` files - just change the filename in `main.py`:
```python
filename = "questions.docx"
```

### PDF Example

PDFs are read-only. The agent will read the PDF and save the output as a `.docx` file:
```python
filename = "questions.pdf"
# Output will be saved as "questions_updated.docx"
```

## 🔒 Security Notes

- **Never commit your `.env` file** - It contains your API key
- The `.gitignore` file is configured to exclude `.env`
- Share `.env.example` instead for other developers

## 📦 Dependencies

- `langchain` - LLM framework
- `langchain-google-genai` - Google Gemini integration
- `langgraph` - Workflow management
- `python-dotenv` - Environment variable management
- `pypdf` & `pdfplumber` - PDF reading
- `python-docx` - Word document support

## 🐛 Troubleshooting

### API Quota Exceeded
```
429 You exceeded your current quota
```
**Solution:** Wait for quota reset (~1 hour) or use a different API key.

### File Not Found
```
Error: File './path/file.txt' not found
```
**Solution:** Ensure the file exists in the project directory and the filename is correct.

### Module Not Found
```
ModuleNotFoundError: No module named 'dotenv'
```
**Solution:** Run `pip install -r requirements.txt`

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

Made with ❤️ using LangChain and Google Gemini AI
