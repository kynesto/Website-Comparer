import os
from ocr import Image2Text 
os.chdir('media')

image2Text = Image2Text()

print(image2Text.convert('BowleWiki_small.png'))
