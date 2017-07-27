import ntpath
import os
import os.path


def modifyDirectory(dirPath):
    changList = ""
    for i in dirPath:
        if i == "\\":
            changList = changList + "/"
        else:
            changList = changList + i
    return changList + "/"


def getAllFilesInSub(start):
    fileList = []
    for path, subdirs, files in os.walk(start):
        for name in files:
            # print(path)
            fileList.append(os.path.join(path, name))
    return fileList


def modifyFile(f, outPath, direction=0):
    with open(f, 'r') as file:
        filedata = file.read()
    # Replace the target string
    replacement = [('http://localhost:4000', '{{site.baseurl}}'),
                   ('http:/localhost:4000', '{{site.baseurl}}'),
                   ('http:/localhost:4000', '{{site.baseurl}}'),
                   ('http:localhost:4000', '{{site.baseurl}}'),
                   ('$', '$$')]

    for i in replacement:
        filedata = filedata.replace(i[direction % 2], i[(direction + 1) % 2])
    # Write the file out again4
    with open(outPath + ntpath.basename(f), 'w') as file:
        file.write(filedata)  # Read in the file
    file.close()


# dir = modifyDirectory("D:\OneDrive - Advokaadibüroo Küllike Namm OÜ\HKU\THESIS" \
#        "\TextManagementScripts\Input")
# file = dir + "input.md"
# modifyFile(file)
# 

files = getAllFilesInSub(modifyDirectory('F:\Projects\posts'))
print(len(files))
for file in files:
    print(file)
    modifyFile(file, outPath=modifyDirectory("F:\Projects\jekyll\\blog\_posts"))


