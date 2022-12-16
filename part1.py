from Globals import *


def rotation_invariant(grey_img,template,method,img2,threshold):
    for angle in np.arange(0,360,15):
        rotated  = imutils.rotate(template, angle)
        h,w  = rotated.shape[::]

        cannySrc=cv.Canny(grey_img,150,170)
        cannyTemp=cv.Canny(rotated,150,170)
        # cv.imshow("temp",cannyTemp)
        # cv.waitKey(1) 
        result= cv.matchTemplate(cannySrc,cannyTemp,eval(method))

        print(angle)
        location=np.where(result>= threshold)
        if location:
            for point in zip(*location[::-1]):
                cv.rectangle(img2,point,(point[0]+w,point[1]+h),255,2)
    return img2, threshold

def run():
    method='cv.TM_CCOEFF_NORMED'
    src_img=cv.imread("Images/messiRotate.jpg")

    src_img = resize(15,src_img)
    grey_img=cv.cvtColor(src_img,cv.COLOR_BGR2GRAY)

    template=cv.imread("Images/templateFinal.png",0)

    template = resize(15,template)
    img2=src_img.copy()

    img2,threshold = rotation_invariant(grey_img,template,method,img2,0.62)        
    cv.imshow("Method {}, Threshold {}".format(method,threshold),img2)
    cv.waitKey(0)
    cv.destroyAllWindows()
