from os import listdir
from os.path import isfile, join

path = './company-profiles'
onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
result_files = []
for file in onlyfiles:
    content = open(join(path,file)).read()
    if 'Java ' in content or 'java ' in content:
    #if 'Android' in content :
        result_files.append(file)
print("\n".join(sorted(result_files)))
print('Files: ')
print(len(result_files))