from fastapi import APIRouter
import fastapi as _fastapi
from config.database import collection_name 
from models.blockchain_model import Block
from schemas.blockchain_schemas import serializeList, serializeDict
import blockchain as _blockchain




router = APIRouter()
blockchain = _blockchain.Blockchain()




# endpoint to mine a block
@router.post("/mine_block/")
async def mine_block(data: str):
    cursor = collection_name.find( {},{"_id":0,"Index": 1, "Timestamp": 1,"Data":1,"Nonce":1,"Previous_hash":1})
    for document in cursor:
        blockchain.chain.append(document)
    
    block = blockchain.mine_block(data = data)
    _id =  collection_name.insert_one(block)
    blockchain.chain.clear()
    return serializeList(collection_name.find({"_id": _id.inserted_id}))



# endpoint to return the entire blockchain 
@router.get("/blockchain/")
async def get_blockchain():
    cursor = collection_name.find( {},{"_id":0,"Index": 1, "Timestamp": 1,"Data":1,"Nonce":1,"Previous_hash":1})
    for document in cursor:
        blockchain.chain.append(document) 
        
    chain = serializeList(collection_name.find())
    blockchain.chain.clear()
    return chain

# endpoint to see if the chain is valid
@router.get("/validate/")
async def is_blockchain_valid():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")

    return blockchain.is_chain_valid()


# endpoint to return the last block
@router.get("/blockchain/last/")
async def previous_block():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="The blockchain is invalid")
        
    return blockchain.get_previous_block()