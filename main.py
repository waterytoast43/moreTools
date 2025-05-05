import os
import moreTools

t = moreTools.listFiles("c:/VS Code/shizzy")
print(t)
a = moreTools.fileExists("main.py","c:/VS Code/shizzy")

if a:
    print("File exists")
else:
    print("File does not exist")

b = moreTools.listProcesses()
print(b[10])

c = moreTools.checkConnection()

if c:
    print("Google connection successful")
else:
    print("Google connection failed")

d = moreTools.listOpenPorts()
#print(d)

moreTools.typeWriter("The quick brown fox jumps over the lazy dog", 0.05)

e = moreTools.scrapeLinks("https://www.example.com")
print(e)

moreTools.scrapeImages("https://picsum.photos/200", open_in_browser=True)
