from Globals import *


def scale_invariant(grey_img,template,method,img2):
    for scale in np.linspace(1,0.2,100):
        resized = imutils.resize(template,width = int(template.shape[1]*scale),height= int(template.shape[0]*scale))
        h,w  = resized.shape[::]

        cannySrc=cv.Canny(grey_img,150,170)
        cannyTemp=cv.Canny(resized,150,170)
        # cv.imshow("temp",cannyTemp)
        # cv.waitKey(1) 
        result= cv.matchTemplate(cannySrc,cannyTemp,eval(method))
        
        threshold= 0.58
        # print(scale)
        location=np.where(result>= threshold)
        if location:
            for point in zip(*location[::-1]):
                cv.rectangle(img2,point,(point[0]+w,point[1]+h),255,2)
    return img2,threshold
    
def run():
    method='cv.TM_CCOEFF_NORMED'
    src_img=cv.imread("Images/messiScale.jpg")
    src_img = resize(15,src_img)
    grey_img=cv.cvtColor(src_img,cv.COLOR_BGR2GRAY)

    template=cv.imread("Images/templateFinal.png",0)

    template = resize(15,template)
    img2=src_img.copy()
    img2,threshold = scale_invariant(grey_img,template,method,img2)        
    cv.imshow("Method {}, Threshold {}".format(method,threshold),img2)
    cv.waitKey(0)
    cv.destroyAllWindows()
    