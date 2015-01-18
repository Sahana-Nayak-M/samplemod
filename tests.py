import os

os.system("git status --porcelain > git-status-bare.txt")

tests = set()

gitStatus = open('git-status-bare.txt')
for statusLine in iter(gitStatus):
    if statusLine.startswith(" M "):
        sourcefile=statusLine[3 : statusLine.index(".py")+ 3]
        testmap = open('meta/impact-map.txt')
        for mapentry in iter(testmap):
            if mapentry.startswith(sourcefile + " "):
                tests.add(mapentry[mapentry.index(" ")+1 : len(mapentry)-1])
        testmap.close()
    # TODO - tests that are new should be added to the list
    # TODO - tests might have been deleted, yet could still be in the map.
gitStatus.close()

if len(tests) > 0:
    commandSeparatedTests = ",".join(tests)
    print "Tests to be run: " + commandSeparatedTests
    os.system("nosetests --tests=" + commandSeparatedTests)
else:
    print "No tests impacted by changes"