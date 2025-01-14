import hashlib

def hash_Compare(file1 , file2):

    h1 = hashlib.sha1() # 20 bayt
    h2 = hashlib.sha1()

    with open(file1 , "rb") as file:
        byteAmount = 1024
        context = file.read(byteAmount)
        while len(context)>0:
            h1.update(context)
            context = file.read(byteAmount)

    with open(file2 , "rb") as file:
        byteAmount = 1024
        context = file.read(byteAmount)
        while len(context)>0:
            h2.update(context)
            context = file.read(byteAmount)
    
    return h1.hexdigest() , h2.hexdigest()

msg1, msg2 = hash_Compare(r"C:\Users\y.pdf",r"C:\Users\x.pdf") 
  
if(msg1 != msg2): 
    print("These files are not identical") 
else: 
    print("These files are identical") 