import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from tools import read_any_file, write_any_file

# Load environment variables from .env file
load_dotenv()

# Get API key and model from environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found. Please set it in your .env file.")

llm = ChatGoogleGenerativeAI(model=GEMINI_MODEL, api_key=GOOGLE_API_KEY)

def read_and_update_file(filename: str, instruction: str):
    """
    Read any supported file (txt, pdf, docx), process with LLM, and update.
    Note: PDF files are read-only, updates will be saved as .docx
    """
    extension = os.path.splitext(filename)[1].lower()
    
    print(f"Reading file: {filename}...")
    old_content = read_any_file.invoke(filename)
    print("File read successfully.")
    
    # Check if file read was successful
    if old_content.startswith("Error:"):
        print(f"Error reading file: {old_content}")
        return old_content

    prompt = f"""
    You are a helpful assistant that can read and update a file.
    The file is {filename}.
    The instruction is {instruction}.
    The old content is:
    
    {old_content}
    
    Return only the updated complete file content.
    Do not include any markdown code fences or explanatory text.
    """
    
    print("Generating response...")
    new_content = llm.invoke([HumanMessage(content=prompt)]).content
    print("Response generated.")

    # Handle PDF special case - save as docx instead
    if extension == ".pdf":
        output_filename = filename.replace(".pdf", "_updated.docx")
        print(f"Note: PDF is read-only. Saving output to: {output_filename}")
    else:
        output_filename = filename

    print(f"Writing file: {output_filename}...")
    result = write_any_file.invoke({"file_path": output_filename, "text": new_content})
    print(f"File written. {result}")

    return new_content
