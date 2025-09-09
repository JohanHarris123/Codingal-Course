fn1 = open('Codingal.txt', 'r')

for line in fn1.readlines():
    if len(line.split()) >= 10:
        fn1.write(line.upper())
    else:
        fn1.write(line.lower())

fn1.close()