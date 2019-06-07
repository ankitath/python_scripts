fname = input('Enter the file')
try:
    fh = open(fname)
except:
    print('Enter valid file name')
    quit()
f = fh.read()
print(f.upper())