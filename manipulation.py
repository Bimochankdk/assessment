import cv2 as cv



def readImage():
    img = cv.imread('nepal.jpg')
    return img

def convert_to_grayscale(img):
    """Convert a BGR image to grayscale."""
    grey_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imwrite('.\\output\\grey_img.jpg', grey_img)
    cv.imshow('grey_img',grey_img)
    cv.waitKey(0)
    return grey_img

def apply_gaussian_blur(image, kernel_size=(7, 7), sigma=0):
    """Apply Gaussian blur to reduce noise."""
    gaussianblur = cv.GaussianBlur(image, kernel_size, sigma)
    cv.imwrite('.\\output\\gaussianblur.jpg', gaussianblur)
    cv.imshow('gaussianblur',gaussianblur)
    cv.waitKey(0)
    return gaussianblur


def detect_edges(image, threshold1=50, threshold2=100):
    canny_edge = cv.Canny(image, threshold1, threshold2)
    cv.imwrite('.\\output\\canny_edge.jpg', canny_edge)
    cv.imshow('canny_edge',canny_edge)
    cv.waitKey(0)
    return canny_edge

if __name__ == '__main__':
    img = readImage()
    convert_to_grayscale(img)
    apply_gaussian_blur(img)
    detect_edges(img)