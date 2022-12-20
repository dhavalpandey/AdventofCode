import re

total_size = 70000000
free_space_needed = 30000000
with open('Day7Input.txt', 'r') as f:
    txt = f.read().strip().split('\n')

filesys = {}
path = ''

for i in range(len(txt)):
    if re.match('\$ cd ', txt[i]):
        d = re.findall('\$ cd (.*)', txt[i])[0]
        if (d != '..'):
            path += '/' + d
            filesys[path] = {'Files': [], 'Folders': [], 'Size': 0}
        else:
            size = filesys[path]['Size']
            path = ''.join([x + '/' for x in path.split('/')[:-1]])[:-1]
            filesys[path]['Size'] += size

    elif re.match('\$ ls', txt[i]):
        i += 1
        while not re.match('\$', txt[i]):
            x = re.findall('dir (.)', txt[i])
            if x:
                filesys[path]['Folders'].extend(x[0])
            else:
                file = txt[i].split(' ')
                filesys[path]['Files'].append(file[1])
                filesys[path]['Size'] += int(file[0])
            i += 1
            if i >= len(txt):
                break

while (path != '//'):
    size = filesys[path]['Size']
    path = ''.join([x + '/' for x in path.split('/')[:-1]])[:-1]
    filesys[path]['Size'] += size

ts = sum([f['Size'] for f in filesys.values() if f['Size'] <= 100000])

curr_unused_space = total_size - filesys['//']['Size']
sizetodel = min([f['Size'] for f in filesys.values() if f['Size'] + curr_unused_space > free_space_needed])

print("Part1 = ", ts)
print("Part2 = ", sizetodel)