from Globals import *
import part1 


# methods = ['cv.TM_CCOEFF', 'cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR',
#             'cv.TM_CCORR_NORMED', 'cv.TM_SQDIFF', 'cv.TM_SQDIFF_NORMED']



def all_invariants(src_img,grey_img,template):
    img2=src_img.copy()
    methods=['cv.TM_CCOEFF_NORMED']
    for method in methods:
        for scale in np.linspace(1,0.2,100):
            resized = imutils.resize(template,width = int(template.shape[1]*scale),height= int(template.shape[0]*scale))
            img2, threshold=part1.rotation_invariant(grey_img,resized,method,img2,threshold=0.26)
            
        cv.imshow("Method {}, Threshold {}".format(method,threshold),img2)
        cv.waitKey(0)
        cv.destroyAllWindows()

    cv.waitKey(0)
def run():
    src_img=cv.imread("Images/messi.jpg")
    src_img = resize(15,src_img)
    grey_img=cv.cvtColor(src_img,cv.COLOR_BGR2GRAY)
    template=cv.imread("Images/templateFinal.png",0)
    template = resize(15,template)
    all_invariants(src_img,grey_img,template)
