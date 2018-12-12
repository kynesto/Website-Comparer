from PIL import Image, ImageFilter
import pytesseract

class Image2Text:
    # Grabs the text on the image, also sharpens the image beforehand

    def get(self, PathToImage):

        #Read image
        im = Image.open(PathToImage)

        #Applying a filter to the image
        im_sharp = im.filter( ImageFilter.SHARPEN )

        return(pytesseract.image_to_string(im_sharp, lang='deu'))
