#ex 1 
import os
path = 'g:\\test\\'
print("Only directories:")
directories = []
for name in os.listdir(path):
    if os.path.isdir(os.path.join(path, name)):
        directories.append(name)
print(directories)

print("\nOnly files:")
files = []
for name in os.listdir(path):
    if not os.path.isdir(os.path.join(path, name)):
        files.append(name)
print(files)
print("\nAll directories and files:")
all_items = []
for name in os.listdir(path):
    all_items.append(name)
print(all_items)

# ex 2
import os
print('Exist:', os.access('c:\\Users\\Public\\C demopathtofile', os.F_OK))
print('Readable:', os.access('c:\\Users\\Public\\C demopathtofile', os.R_OK))
print('Writable:', os.access('c:\\Users\\Public\\C demopathtofile', os.W_OK))
print('Executable:', os.access('c:\\Users\\Public\\C demopathtofile', os.X_OK))

# ex 3
import os

print("Testing if a path exists:")
path1 = r'f:\\demo\\1.txt'
print(os.path.exists(path1))
path2 = r'f:\\demo\\2.txt'
print(os.path.exists(path2)) 
print("\nFile name extracted from the path:")
print(os.path.basename(path2)) 
print("\nDirectory name extracted from the path:")
print(os.path.dirname(path2)) 

# ex5 
with open(r"file.txt", 'r') as fp:
    lines = len(fp.readlines())
    print('Total Number of lines:', lines)

# ex 6 
def generate():
    fn = 65
    for i in range(26):
        letter = chr(fn)  
        with open(f"{letter}.txt", 'w') as f:
            f.write(f"This is the content of {letter}.txt\n")
        fn += 1  
generate()

        
# ex 7 
with open('a.txt','r') as first, open('b.txt','a') as sec: 
    for line in first: 
             sec.write(line)

# ex 8 
import os
if os.path.exists("file.txt"):
  os.remove("file.txt")
else:
  print("The file does not exist")


