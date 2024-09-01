
# Smart Querying for PDFs

A brief description of what this project does and who it's for

## Introduction

This application provides a interface for querying a pdf file smartly .It performs detailed text extraction from pdf using tessaract and preprocessing, including text cleaning and segmentation into manageable chunks. These chunks are embedded using the sentence-transformers/all-mpnet-base-v2 model and stored in a FAISS vector database for efficient similarity searches. Users can input queries related to the PDF content, with responses generated by the t5-large model, which synthesizes information from relevant text chunks to deliver precise answers. 

## Project Flow
![alt text]([https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true](https://github.com/Ayush-Singh677/PDF-Answering-Chatbot/blob/main/assets/image.png))


## Setup

Ensure you have latest version of python installed.

1. Install all the required libraries.
```
pip install -r requirements.txt
```

2. Download all the required models.
```
python3 download_models.py
```

3. Run the streamlit app
```
streamlit run app.py
```
