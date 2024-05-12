# files with .gif .jpg .jpeg .png .pdf .txt .zip
# show their file type image/gif
# or show application/octet-stream

"""
image/gif 
image/jpg 
image/jpeg 
image/png 
application/pdf 
text/plain
application/zip
"""


"""
file = input("file name: ").strip().lower()
fir, last = file.split(".")

types = {
    "gif" : "image/gif", "jpg" : "image/jpg",
     "jpeg" : "image/jpeg", "png" : "image/png", 
     "pdf" : "application/pdf", "txt" :"text/plain",
     "zip" : "application/zip"
}

if (last==("gif") | last==("jpeg") | last==("jpg") ):
    print(types[last])
elif ( last==("png") | last==("pdf") | last==("txt") ):
    print(types[last])
elif ( last==("zip")):
    print(types[last])
else:
    print("application/octet-stream")
"""


#seems the limit of or is just 3
# just one missing = messed up 10min
# overcomplication again instead of using endswith and if elif for each file

file= input("file: ")

if (file.endswith("jpe")):
    print("image/jpeg")
else:
    print("application/octet-stream") 

