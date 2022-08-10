def block_serializer(block) -> dict:
    return {
        "id": str(block["_id"]),
        "Index": block["Index"],
        "Timestamp": block["Timestamp"],
        "Data": block["Data"],
        "Nonce": block["Nonce"],
        "Previous_hash": block["Previous_hash"],
    }
    
   
    

def serializeList(blocks) -> list:
    return [block_serializer(block) for block in blocks]

def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]