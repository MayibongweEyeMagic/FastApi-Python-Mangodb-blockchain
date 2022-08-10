from pymongo import MongoClient


client = MongoClient("mongodb+srv://mayibongwe:blockchain@cluster0.c6dii.mongodb.net/mydatabase?retryWrites=true&w=majority")

db = client.mydatabase 

collection_name = db["blockschain"]






 
