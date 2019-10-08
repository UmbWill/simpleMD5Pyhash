import hashlib
import os

BUF_FILESIZE = 65536 #64k buffer



def get_hash_md5(file_name):
 
 if not os.path.exists(file_name):
  print("Enter a valid file.")
  return
 
 md5 = hashlib.md5()
 try:
  with open(file_name, "rb") as f:
   while True:
    data = f.read(BUF_FILESIZE)
    if not data:
     break
    md5.update(data)
  print("MD5 : {0}".format(md5.hexdigest()))     
 except IOError as err:
  print("Error to open file. ", err )
 

if __name__ == "__main__":
 print("**** start hash *****")
 get_hash_md5("test.txt")
 