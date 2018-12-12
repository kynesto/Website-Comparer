import os
import codecs
from ocr import Image2Text 
from html_parser import Website2Text
from comparetext import StringHelper
os.chdir('media')

# # comment out to test only the comparer
# image2Text = Image2Text()
# website2Text = Website2Text()

# imtext = image2Text.get('BowleWiki_small.png')
# webtext = website2Text.get('https://de.wikipedia.org/wiki/Bowle')

# with codecs.open("imtext.txt", "w", "utf-8-sig") as temp:
#     temp.write(imtext)

# with codecs.open("webtext.txt", "w", "utf-8-sig") as temp:
#     temp.write(webtext)

# only needed in testing otherwise live strings are used, to be commented out in production
with codecs.open("imtext.txt", "r", "utf-8-sig") as temp:
    imtext = temp.read()
with codecs.open("webtext.txt", "r", "utf-8-sig") as temp:
    webtext = temp.read()

# imtext = "hello world thhis is a test, grabl grabl bu hu hu"
# webtext = " test hello garbage   lots of html and other :DSNJ AWworld thhis is a test, grabl grabl bu hu hu"

# sorts and compares the list of strings
imtextList = imtext.split()
imtextList.sort()
print(imtextList)
print("--------------------------------------------------------------------/n")

webtextList = webtext.split()
webtextList.sort()
print(webtextList)

print("--------------------------------------------------------------------/n")

while webtextList != imtextList:
    for web, img in zip(webtextList, imtextList):
        if web != img:
            # print(web)
            webtextList.remove(web)
            print("--------------------------------------------------------------------/n")
            print(webtextList)
            break

print(webtextList)

# indexToStartComp = stringHelper.getStart(SampleText1, SampleText2, 7)

# print(indexToStartComp)
# print(stringHelper.getDiffs(SampleText1, SampleText2[indexToStartComp:]))
