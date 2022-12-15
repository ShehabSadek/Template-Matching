import cv2 as cv
import numpy as np
import imutils
from matplotlib import pyplot as plt
from scipy.ndimage import rotate as rotate_image

# methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
#             'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']
methods=['cv.TM_CCOEFF_NORMED']
# src_img=cv.imread("Images/test.jpg")
src_img=cv.imread("Images/messi3.jpg")


scale_percent = 15
width = int(src_img.shape[1] * scale_percent / 100)
height = int(src_img.shape[0] * scale_percent / 100)
dim = (width, height)
src_img = cv.resize(src_img, dim, interpolation = cv.INTER_AREA)


# src_img = cv.fastNlMeansDenoisingColored(src_img,None,10,10,7,21)

grey_img=cv.cvtColor(src_img,cv.COLOR_BGR2GRAY)

# template=cv.imread("Images/temp.jpg",0)
template=cv.imread("Images/temp2.png",0)
scale_percent = 15

width = int(template.shape[1] * scale_percent / 100)
height = int(template.shape[0] * scale_percent / 100)
dim = (width, height)
template = cv.resize(template, dim, interpolation = cv.INTER_AREA)

# h,w = template.shape[::]

 

 
def invariants(src_img,template):
    h,w = template.shape[::]
    img2=src_img.copy()
    visited=[]
    for method in methods:
        for scale in np.linspace(1,0.2,100):
            for angle in np.arange(0,360,15):
                resized = imutils.resize(template,width = int(template.shape[1]*scale),height= int(template.shape[0]*scale))
                print(angle)
                rotated  = imutils.rotate(resized, angle)
                h,w  = rotated.shape[::]

                # cv.imshow("temp",rotated)
                # cv.waitKey(1) 

                cannySrc=cv.Canny(grey_img,150,170)
                cannyTemp=cv.Canny(rotated,150,170)
                cv.imshow("temp",cannyTemp)
                cv.waitKey(1) 
                result= cv.matchTemplate(cannySrc,cannyTemp,eval(method))
                # loc=np.where(result)
                # for point in zip(*loc[::-1]):
                #     img3=src_img.copy()
                #     cv.rectangle(img3,point,(point[0]+w,point[1]+h),255,2)
                #     cv.imshow("temp",img3)
                #     cv.waitKey(1) 

                threshold= 0.26


                # plt.imshow(result, cmap='Greys')
                # plt.waitforbuttonpress(0)
                location=np.where(result>= threshold)
                if location:
                    for point in zip(*location[::-1]):
                        if point[0] not in visited:
                            cv.rectangle(img2,point,(point[0]+w,point[1]+h),255,2)
                            # cv.putText(img2, ("{}".format(point)), (point[0]+w+5,point[1]+h+5), cv.FONT_HERSHEY_PLAIN, 1, (0,255,0), 1);
                            cv.imshow("Method {}, Threshold {}".format(method,threshold),img2)
                            visited.append(point[0])

        cv.waitKey(0)
        cv.destroyAllWindows()

    cv.waitKey(0)
invariants(src_img,template)


# for method in methods:
#     img2=src_img.copy()
#     print(method)

#     result= cv.matchTemplate(grey_img,template,eval(method))

#     # plt.imshow(result, cmap='gray')
#     # plt.waitforbuttonpress(0)

#     val_min, val_max, i_min, i_max =  cv.minMaxLoc(result)
#     # print(val_min, val_max, i_min, i_max)

#     #SINGLE
#     # if method in ['cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']:
#     #     loc=i_min
#     # else:
#     #     loc=i_max
#     # cv.rectangle(img2,loc,(loc[0]+w,loc[1]+h),(0,255,0),2)
#     # cv.imshow("Method {}".format(method),img2)


#     #MULTIPLE

#     threshold= 0.95
#     location=np.where(result>= threshold)
#     for point in zip(*location[::-1]):
#         cv.rectangle(img2,point,(point[0]+w,point[1]+h),255,2)

#     # print(location)
#     cv.imshow("Method {}, Threshold {}".format(method,threshold),img2)
#     cv.waitKey(0)
#     # if location:
#     #     color=0
#     #     for loc in location:
#     #         cv.rectangle(img2,loc,(loc[0]+w,loc[1]+h),color,2)
#     #         color=color+30
#     #         if color >= 255:
#     #             color=0
#     #         scale_percent = 60
#     #         width = int(img2.shape[1] * scale_percent / 100)
#     #         height = int(img2.shape[0] * scale_percent / 100)
#     #         dim = (width, height)
#     #         resized = cv.resize(img2, dim, interpolation = cv.INTER_AREA)
#     #         cv.imshow("Method {}, Threshold {}".format(method,threshold),resized)
#     #         cv.waitKey(0)

#     cv.waitKey(0)
#     cv.destroyAllWindows()