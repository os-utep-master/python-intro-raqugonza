import sys        # command line arguments
import re         # regular expression tools

inputFile = sys.argv[1] 
#outputFile = sys.argv[2]

master ={}
count = 0
repeat = False
with open(inputFile, 'r') as inName:
    for line in inName:
        # get rid of newline characters
        line = line.strip()
        # split line on whitespace and punctuation
        word = re.split('[ \t]', line)
        
        for i in range(len(word)):
            for j in range(len(master)) :
                if master[j] == word[i]:
                    repeat = True
            if repeat == False:       
                master[count] = word[i]
                print(master[count])
                count = count+1
                
            repeat = False    
                
    
       # master[word[0]] = int(word[1])
