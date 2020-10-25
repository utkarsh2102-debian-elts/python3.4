import base64
image = open('recursion.tar.b64', 'rb')
image_read = image.read()
image_64_decode = base64.decodestring(image_read) 
image_result = open('recursion.tar', 'wb') # create a writable image and write the decoding result
image_result.write(image_64_decode)
