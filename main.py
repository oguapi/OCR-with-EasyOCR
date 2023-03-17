import cv2
import easyocr
import matplotlib.pyplot as plt

#Read image
#image_path= 'data\img1.jpeg' #Put the path of the image
#image_path= 'data\img2.jpg'
image_path= 'data\img3.jpg'

img= cv2.imread(image_path)

#Instance text detector (instance of the text detector tecnology)
reader= easyocr.Reader(['en'], gpu=False) #firts we put the language of the reader and then the exitend of the gpu 


#Detect text on image
text= reader.readtext(img)

threshold= 0.25

#Draw bbox and text
for t in text:#we iterate to get a better resolt
    print(t)
#we get as result a [bbox,text,score(float)]
    bbox, text, score= t
    #The bbox contain the cornerts where is the text and to draw we 
    # need the upon left cornert (bbox[0]) and the botton right cornert
    # (bbox[2])
    
    #Conversion de float a int
    bbox[0][0],bbox[0][1]= round(bbox[0][0]),round(bbox[0][1])
    bbox[1][0],bbox[1][1]= round(bbox[1][0]),round(bbox[1][1])
    bbox[2][0],bbox[2][1]= round(bbox[2][0]),round(bbox[2][1])
    bbox[3][0],bbox[3][1]= round(bbox[3][0]),round(bbox[3][1])
    
    if score> threshold:
        #cv2.rectangle(img, bbox[0], bbox[2], (0,255,0), 5) #Firts the image, nexts the location, the color and the thickness value
        #Draw lines
        cv2.line(img, bbox[0], bbox[1], (255,0,0),5)
        cv2.line(img, bbox[1], bbox[2], (255,0,0),5)
        cv2.line(img, bbox[2], bbox[3], (255,0,0),5)
        cv2.line(img, bbox[3], bbox[0], (255,0,0),5)

        #Put the text in the image
        cv2.putText(img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 1, (0,10,250),2) #We put the image, text, upon left corner and the font, size, color and thickness value

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
