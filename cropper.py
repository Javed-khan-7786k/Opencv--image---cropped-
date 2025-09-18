import cv2
drawing=False
ix,iy=-1,-1
rect=None
def draw(event,x,y,flags,param):
    global ix,iy,drawing,rect
    if event==cv2.EVENT_LBUTTONDOWN:
        ix,iy=x,y
        drawing=True
    elif event==cv2.EVENT_MOUSEMOVE and drawing:
        rect=(ix,iy,x,y)
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        rect=(ix,iy,x,y)

r_img=cv2.imread("1757951821170.jpg")
h,w=r_img.shape[:2]
max_h,max_w= 900,1600
scale=min(max_w/w,max_h/h)
new_w,new_h=int(w*scale),int(h*scale)
img=cv2.resize(r_img,(new_w,new_h))



cv2.namedWindow("cropping")
cv2.setMouseCallback("cropping",draw)

while True:
    temp=img.copy()
    if rect:
        cv2.rectangle(temp,(rect[0],rect[1]),(rect[2],rect[3]),(0,0,255),2)
    cv2.imshow("cropping",temp)
    if cv2.waitKey(1) & 0xff==ord("y"):
        x1, y1, x2, y2 = rect
        rect_x1, rect_x2 = sorted([x1, x2])
        rect_y1, rect_y2 = sorted([y1, y2])
        cv2.destroyAllWindows()
        break
new=img[rect_y1:rect_y2,rect_x1:rect_x2]

cv2.imshow("cropping",new)
cv2.waitKey(0)
cv2.destroyAllWindows()