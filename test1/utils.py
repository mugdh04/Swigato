import os
import pickle
import faiss
from dotenv import load_dotenv, find_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import AzureOpenAIEmbeddings
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import json

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Google Generative AI configuration
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize Google Generative AI model
llm = GoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=GOOGLE_API_KEY)

def process_message(message):
    try:
        # Load PDF containing food information
        pdf_path = "test1/documents/input.pdf"
        pdf_loader = PyPDFLoader(pdf_path)
        data = pdf_loader.load()

        # Split the text from the PDF into chunks
        text_splitter = CharacterTextSplitter(separator='\n', chunk_size=1000, chunk_overlap=200)
        docs = text_splitter.split_documents(data)

        # Generate embeddings using Azure OpenAI
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

        # Check if FAISS store exists
        faiss_store_path = "faiss_store"
        # if not os.path.exists(faiss_store_path):
            # Create FAISS vector store from the documents
        vectorStore_openAI = FAISS.from_documents(docs, embeddings)
        vectorStore_openAI.save_local(faiss_store_path)
        # else:
        #     print("FAISS store already exists. Skipping creation.")

        # Load the FAISS store and create the QA chain
        ret = FAISS.load_local(faiss_store_path, embeddings, allow_dangerous_deserialization=True)

        # Extract products and categories
        extract_products_system_prompt = """You are an assistant for extracting food items, their categories and all the other information provided in the pdf only. \
        Extract the information from the pdf correctly and do not leave a single piece of information from the pdf. \
        Use the following pieces of retrieved context to extract the food items and their categories. \
        If you don't know the category, just say that you don't know. \
        use the pdf only for the output. and if you dont get anything just say i dont know \
        Give the accurate answers only and extract the products which are good match do not try to match the items with the input if they are not a good match. \
        Use five sentences maximum and keep the answer concise. \
        If someone ask anything out of the pdf's information or anything unrelated to the food items or something which you think should not be asked from a Food recommendation Model then answer something humorous to tell them that you are a food recommendation model and do not extract any food item in that case. \
        Don't mention the word document in the answer and do not tell from where you are extracting the information. \
        I should get the dictionary of answer variable with whole answer and category and product variable with category and product name. \
        Output format:
        {{
            "answer": "AI's concise answer",
            "products": [
                {{"category": "category1", "product": "Item ID1", "name": "Item Name1", "price": "Price1", "rating": "Rating1"}},
                {{"category": "category2", "product": "Item ID2", "name": "Item Name2", "price": "Price2", "rating": "Rating2"}},
                ...
            ]
        }}
        {context}"""
        extract_products_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", extract_products_system_prompt),
                ("human", "{input}"),
            ]
        )
        question_answer_chain = create_stuff_documents_chain(llm, extract_products_prompt)
        rag_chain = create_retrieval_chain(ret.as_retriever(), question_answer_chain)
        
        result = rag_chain.invoke({"input": message})
        
        json_str = result["answer"].replace('```json', '').replace('```', '').strip()
        data = json.loads(json_str)
        
        products = data['products'] 
        answer = data['answer']      
        return products, answer

    except Exception as e:
        print(f"An error occurred: {e}")
        return [], ""