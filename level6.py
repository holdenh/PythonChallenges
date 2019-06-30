# this challenge calls for starting with a file and get the name of the next file 
# and following the chain.
#
# inside the readme.txt
# welcome to my zipped list.
#
# hint1: start from 90052
# hint2: answer is inside the zip
#
# .txt file contents : Next nothing is 88244
 

import zipfile, re

#use regex will retrun a list of a single element.
nothing = ['90052']

myWorkspace = 'D:\\PythonChallenges\\channel.zip'
zippedData = zipfile.ZipFile(myWorkspace)

#loop through the file and read each .txt file. 
#   collect all comment from the files along the way.
commentString = ''
while len(nothing)!= 0 :
    data = zippedData.read(str(nothing[0]) + '.txt').decode('utf-8')
    print(data)
    if zippedData.comment != 0 :
        comment = str(zippedData.getinfo(str(nothing[0])+'.txt').comment.decode('utf-8')).lstrip("b'").rstrip("'")
        
        commentString += comment
    nothing = re.findall('Next nothing is ([0-9]+)', data)
        
#loop comments and print out one by one.
testString = "hello\nThere"
print('\n')
print(str(commentString))
