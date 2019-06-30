import pickle
import urllib.request

#upon looking in the source code, I found a web link to the below url. 
# at the link there is data that is scrambled.
# must notice that 'peak hell' sounds like 'pickle' 
page= urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/banner.p").read()
pageData = pickle.loads(page)
output = ''
# the output data is of the form Dictionary[subdict[tuples()]]
#step into dict.
for subDict in pageData :
    output = ''
    #loop through sub dict.
    for j in range(len(subDict)) :
        #loop from 0 to the second number of tuples.
        for k in range((subDict[j][1])) :
            #add the first tiem of the tuple till the second number is hit, which is k.
            output = output + subDict[j][0]

    #print the whole line out. 
    print(output)