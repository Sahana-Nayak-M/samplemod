import os.path

lines = (line.rstrip('\n') for line in open("last_test_coverage.txt"))
for line in lines:
    words = line.split()
    fn = words[0].replace(".","/") + ".py"
    if os.path.isfile(fn) and words[3] != "0%":
        print fn