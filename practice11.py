fname = input("Enter file name: ")

lst=list()
fh = open(fname)
count = 0
addr = dict()
for line in fh:
    line = line.rstrip()
    if not line.startswith('From:'): continue
    line = line.split()
    lst.append(line[1])
#print(lst)

counts = dict()

for word in lst:
     counts[word] = counts.get(word, 0)+1
#
# print(counts)
highcount = 0
highvalue = 0
for word, count in counts.items():
    if highcount is None or count > highcount:
        highvalue = word
        highcount = count
print(highvalue, highcount)

    #print(words[1])
    #count =  count+1    


#print("There were", count, "lines in the file with From as the first word")