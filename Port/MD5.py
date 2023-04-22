import hashlib

def get_md5_value(src):
    myMd5 = hashlib.md5()
    myMd5.update(src.encode('utf-8'))
    myMd5_Digest = myMd5.hexdigest()
    return myMd5_Digest
