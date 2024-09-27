# Groq
An attempt to  build projects using  Groq APi key

You can get your groq key from here : https://console.groq.com

`Model`: ***llama3-8b-8192***


`chatbot.py`:
It is a personal chatbot application that uses the Groq API to engage in conversation and summarize chat history after `exit` keyword is triggered . It is designed to be a supportive and affectionate chatbot, capturing the essence of friendly interactions. 

## Features

- **Chatting**: Engage in real-time conversation with the chatbot.
- **Chat Summarization**: At the end of the chat, the conversation is summarized, and the summary is saved to a JSON file.
- **Previous Summary Loading**: Load and display the previous chat summary when starting the chatbot.

## Snapshot of Json file:

![json ](https://github.com/user-attachments/assets/4f2445d5-ec6d-4e9b-bf74-23e0cb7cda6b)


---

`cover_letter.py`:
This allows you to generate personalized cover letters based on your CV extracted from a PDF file. It utilizes the `Groq API` for natural language processing and the `PyPDF2` library to extract text from PDF files. 

## Features

- **PDF Text Extraction**: Easily extract text from your CV in PDF format.
- **Personalized Cover Letters**: Generate a tailored cover letter for a specific job position at a given company.
- **User-Friendly Interface**: Simple file dialog for selecting your CV and straightforward command-line prompts for input.

## Snapshot of Cover letter:

![Screenshot 2024-09-27 155435](https://github.com/user-attachments/assets/def744dc-5243-435c-a443-506c96733cf8)

