
SampleText1 = "Hello Fellow Humans"
SampleText2 = "1234 hed ser Hello World Thit it a test long enough?"

class StringHelper:
    # SampleTExt1 Schould be longer than SampleText2, as this is the maximum length the loop will iterate trough, Returns a string with different letters, seperated by ;
    def getDiffs(self, Text1, Text2):
        differences = ";"
        for LetterText1, LetterText2 in zip(Text1, Text2):
            if LetterText1 != LetterText2:
                differences = differences + LetterText2 + ";"
        return differences
    
    #finds where one string starts within the other
    def getStart(self, Text1, Text2, searchLength):
        start = Text1[50:50+searchLength]
        return Text2.find(start)
