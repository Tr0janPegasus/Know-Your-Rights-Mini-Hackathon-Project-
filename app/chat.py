
# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# from transformers import GPT2TokenizerFast
# from langchain.document_loaders import PyPDFLoader
# from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.embeddings import OpenAIEmbeddings
# from langchain.vectorstores import FAISS
# from langchain.chains.question_answering import load_qa_chain
# from langchain.llms import OpenAI
# from langchain.chains import ConversationalRetrievalChain

# os.environ["OPENAI_API_KEY"] = "{YOURAPIKEY}"

# You MUST add your PDF to local files in this notebook (folder icon on left hand side of screen)

# Advanced method - Split by chunk

# Step 1: Convert PDF to text
# import textract
doc = textract.process("./attention_is_all_you_need.pdf")

# Step 2: Save to .txt and reopen (helps prevent issues)
with open('attention_is_all_you_need.txt', 'w') as f:
    f.write(doc.decode('utf-8'))

with open('attention_is_all_you_need.txt', 'r') as f:
    text = f.read()

