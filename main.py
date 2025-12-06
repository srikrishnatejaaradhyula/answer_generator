from graph import app

if __name__ == "__main__":
    # Change the filename to test different file types:
    # - "example.txt"           -> Text file
    # - "sample_questions.docx" -> Word document
    # - "sample.pdf"            -> PDF file (read-only, output saved as .docx)
    
    filename = "sample_questions.docx"  # Test with Word document
    
    result = app.invoke({
        "filename": filename,
        "instruction": "Answer the questions in the file and update the file.",
    })
    
    print("\n" + "="*50)
    print("Processing complete!")
    print("="*50)
