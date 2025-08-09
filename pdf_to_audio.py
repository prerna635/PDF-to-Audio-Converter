import PyPDF2
import pyttsx3

def pdf_to_audio(pdf_file):
    # Open the PDF file
    with open(pdf_file, 'rb') as book:
        reader = PyPDF2.PdfReader(book)
        speaker = pyttsx3.init()

        for page_num in range(len(reader.pages)):
            text = reader.pages[page_num].extract_text()
            if text:
                speaker.say(text)
                speaker.runAndWait()

if __name__ == "__main__":
    pdf_file = input("Enter the PDF file path: ")
    pdf_to_audio(pdf_file)
