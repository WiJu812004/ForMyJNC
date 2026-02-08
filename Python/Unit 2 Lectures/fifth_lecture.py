fin = open('names.out', 'r')
fout = open('names.out.out', 'w')

k = -1
for line in fin:
  line = line.rstrip()
  for c in line:
    fout.write(chr(ord(c) + k))
  fout.write("\n")
fout.close()