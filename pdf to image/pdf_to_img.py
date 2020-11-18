# import module 
from pdf2image import convert_from_path 
  
# Storing Pdf with convert_from_path function 
images = convert_from_path('D:\\Personal\\Practice\\CodeCell_Hackathon\\PDF2.pdf') 
idx=0
for img in images:
    idx+=1
    img.save('output-'+str(idx)+".jpg", 'JPEG')