fname = input('Enter the file')
try:
    fh = open(fname)
except:
    print('Enter valid file name')
    quit()
count = 0
sum=0
for line in fh:
    
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    count = count + 1
    m = float(line[20:30])
    sum = sum + m
print(sum/count)
    #print(line, count)
    