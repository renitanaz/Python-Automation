
#opening file 
f= open('Files_automation\\Exercise Files\\inputFile.txt','r')
#looping thru every line 
for line in f:
    # splitting line to get the third word
    line_split = line.split()
    if (line_split[2] == 'P'):
        print(line)
f.close