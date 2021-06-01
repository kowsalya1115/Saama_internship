import sys
if len(sys.argv) < 3:
    print("Wrong parameter")
    print("./copyfile.py file1 file2")
    sys.exit(1)
with open(sys.argv[1]) as f1:
    s = f1.read()
with open(sys.argv[2], 'w') as f2:
    f2.write(s)

