
# coding: utf-8

# In[71]:


import cv2


# In[72]:


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


# In[73]:


# capture = cv2.VideoCapture(0)


# In[81]:


while True:
#     status , img = capture.read()
    img = cv2.imread('group_pic.jpg')
#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img , 1.1 ,4)
    for (x,y,w,h) in faces:
        cv2.rectangle(img , (x,y) , (x+w , y+h) , (181,55,251) ,2)
        cv2.putText(img, 'Surya' ,(30,70),cv2.FONT_HERSHEY_SIMPLEX ,1, (177,106,57), 2, cv2.LINE_AA)
        cv2.putText(img, 'Praveen' ,(190,70),cv2.FONT_HERSHEY_SIMPLEX ,1, (177,106,57), 2, cv2.LINE_AA)
        cv2.putText(img, 'Shannu' ,(20,350),cv2.FONT_HERSHEY_SIMPLEX ,1, (177,106,57), 2, cv2.LINE_AA)
        cv2.putText(img, 'Sony' ,(200,350),cv2.FONT_HERSHEY_SIMPLEX ,1, (177,106,57),2, cv2.LINE_AA)
#         gray_img = gray[y:y+h , x:x+w]
        eye_img = img[y:y+h , x:x+w]
        eyes = eye_cascade.detectMultiScale(gray_img)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(eye_img , (ex,ey) ,(ex+ew , ey+eh),(0,255,255) ,2)
    cv2.imshow('Sony' , img)
    k = cv2.waitKey(30) & 0xff
    if(k==27):
        break
    
capture.release()
cv2.destroyAllWindows()

