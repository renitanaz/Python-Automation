# this writes data from one file into another file
#opening file 
f= open('Files_automation\\Exercise Files\\inputFile.txt','r')
PassFile = open('Files_automation\\Exercise Files\\passfile.txt', 'w')
FailFile = open('Files_automation\\Exercise Files\\Failfile.txt', 'w')
#looping thru every line 
for line in f:
    # splitting line to get the third word
    line_split = line.split()
    if (line_split[2] == 'P'):
        PassFile.write(line)
    else:
        FailFile.write(line)
f.close()
PassFile.close()
FailFile.close()