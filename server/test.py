# import os
# from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from langchain.chains import RetrievalQA

# load_dotenv()

# GROQ_API_KEY=os.environ.get("GROQ_API_KEY")

# print(GROQ_API_KEY)

import os
from pinecone import Pinecone, ServerlessSpec

api_key = os.environ.get("PINECONE_API_KEY")

pc = Pinecone(api_key=api_key)
pc.create_index(
    name='my_index',
    dimension=1536,
    metric='cosine',
    spec=ServerlessSpec(cloud='aws', region='us-west-2')
)
index = pc.Index('my_index')

# Now you're ready to perform data operations
print(index.query(vector=[...], top_k=10))