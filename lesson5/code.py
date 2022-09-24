import requests
response = requests.get("https://hsto.org/getpro/habr/upload_files/fc8/61c/c3e/fc861cc3e025ccc0061de5d4035c9665.jpg")
myimage = open("my.jpg", "wb")
myimage.write(response.content)
myimage.close()
