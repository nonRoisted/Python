import urllib.request
file = urllib.request.urlopen("http://dfedorov.spb.ru/python3/sport.txt").read().decode('cp1251').split("\n")[1:]
sports = {}
for line in file:
    new_line = line.split("\t")
    if len(new_line) == 7:
        sport = new_line[3].split(',')
        for name in sport:
            name = name.strip()
            if name in sports and name != '':
                sports[name] += 1
            else: sports[name] = 1
sort_sports = list(dict(sorted(sports.items(), key = lambda item: item[1], reverse=True)))[:3]
for ind in range(3):
    print(ind+1, 'place -->', sort_sports[ind])