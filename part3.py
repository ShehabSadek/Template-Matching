from Globals import *


def multiple_match(grey_img,template,method,img2,threshold):
    h,w  = template.shape[::]

    cannySrc=cv.Canny(grey_img,150,170)
    cannyTemp=cv.Canny(template,150,170)
    # cv.imshow("temp",cannyTemp)
    # cv.waitKey(1) 
    result= cv.matchTemplate(cannySrc,cannyTemp,eval(method))

    location=np.where(result>= threshold)
    if location:
        for point in zip(*location[::-1]):
            cv.rectangle(img2,point,(point[0]+w,point[1]+h),255,2)
    return img2, threshold

def run(num):
    method='cv.TM_CCOEFF_NORMED'
    if(num==1):
        src_img=cv.imread("Images/messiMulti.jpg")
    else:
        src_img=cv.imread("Images/empty.jpg")

    src_img = resize(30,src_img)
    grey_img=cv.cvtColor(src_img,cv.COLOR_BGR2GRAY)

    template=cv.imread("Images/templateFinal.png",0)

    template = resize(30,template)
    img2=src_img.copy()

    img2,threshold = multiple_match(grey_img,template,method,img2,0.34)        
    cv.imshow("Method {}, Threshold {}".format(method,threshold),img2)
    cv.waitKey(0)
    cv.destroyAllWindows()
