
fin = open('sample.txt')

fout = open('output.txt', 'w')

for line in fin:
    fout.write(line.replace('function', ''))

fin.close()
fout.close()