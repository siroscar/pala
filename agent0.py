print("WAGWANFAMALAM!")

import os
import pdfplumber
from dotenv import load_dotenv
from google import genai          

print("--- Script started! ---")
#Load API key from .env 
load_dotenv(dotenv_path="key.env")

#Extract text from the PDF 
def extract_pdf_text(path):
    with pdfplumber.open(path) as pdf:
        text = ""
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

# language model analysis
def analyze_themes(poem_text):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    prompt = f"""You are a literary analyst. Read the poem below, identify a famous poet with a similar style and identify its main themes.

For each theme:
- Give it a short name
- Explain in 2 sentences why it fits the poem
- Quote a short line from the poem that supports it

Poem:
---
{poem_text}
---
"""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt,
    )
    return response.text

#EXECUTE
if __name__ == "__main__":
    poem = extract_pdf_text("poem.pdf")

    print("=== EXTRACTED POEM ===\n")
    print(poem)
    print("\n=== THEMES ===\n")

    themes = analyze_themes(poem)
    print(themes)