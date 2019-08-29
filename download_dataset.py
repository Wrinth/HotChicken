import urllib
import os
import requests

# Open the mapping_list file with read only permit
f = open('./train/mapping_list.txt', encoding='gbk')
# use readline() to read the first line 
line = f.readline()
while line:
    name, type1, type2 = line.split(',')
    directory = 'dataset/'+type2
    if not os.path.exists(directory.rstrip()):
        os.makedirs(directory.rstrip())
    else:
        for root, dirs, files in os.walk(directory):
            for file in files:
                os.remove(os.path.join(root, file))
    line = f.readline()
f.close()

# Open the train file with read only permit
f = open('./train/train.txt')
# use readline() to read the first line 
line = f.readline()
while line:
    url, type1, type2 = line.rsplit(',', 2)
    directory = 'dataset/' + type2

    onlyfiles = next(os.walk(directory.rstrip()))[2]
    filename = format(int(type2), '03d') + '_' + format(len(onlyfiles), '05d') + '.jpg'
    print(filename)
    try:
        r = requests.get(url)
        if r.content:
            open('./' + directory.rstrip() + '/' + filename, 'wb').write(r.content)
    except requests.RequestException as e:
        print(e)

    line = f.readline()
f.close()
