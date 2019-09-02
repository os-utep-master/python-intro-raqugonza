import sys        # command line arguments
import re         # regular expression tools

inputFile = sys.argv[1] 
outputFile = sys.argv[2]

master ={}
counter = {}
combination = {}
count = 0
repeat = False
with open(inputFile, 'r') as inName:
    for line in inName:
        # get rid of newline characters
        line = line.strip()
        # split line on whitespace and punctuation
        word = re.split('[ \t]', line)
        for a in range(len(word)):
            if "." in word[a] or "," in word[a] or ":" in word[a]  :
                string = word[a]
                word[a]= string[0:-1]
        for i in range(len(word)):
            for j in range(len(master)) :
                if master[j].lower() == word[i].lower():
                    repeat = True
                    counter[j] = counter[j] + 1
            if repeat == False:       
                master[count] = word[i].lower()
                counter[count] = 1
                count = count+1            
            repeat = False   

for i in range(len(master)) :
    combination[i] = master[i] +" " +str(counter[i]) + "\n"
f = open(outputFile, "w")
c = combination.keys()   
for i in sorted(c) :
    f.write(combination[i])
