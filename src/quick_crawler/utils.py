import hashlib
import uuid

def quick_id():
    unique_id = uuid.uuid4()
    return unique_id

def quick_md5_id(s):
    unique_id = hashlib.md5(s.encode())
    page_id = str(unique_id.hexdigest())
    return page_id