#!/usr/bin/python
print ("{:>60}".format("barradarcy@hotmail.com"))
print ("{:>60}".format(" "))
npt = raw_input (("26 Char Cyper Sentence: ").lower())
L = list(npt)
r = raw_input ('{name of file}: ')
txt='.txt'
me=r+txt
folder = open(me, 'a')

while True:
 a = L[0];b = L[1];c = L[2];d = L[3];e = L[4];f = L[5];g = L[6];h = L[7];
 i = L[8];j = L[9];k = L[10];l = L[11];m = L[12];n = L[13];o = L[14];p = L[15];
 q = L[16];r = L[17];s = L[18];t = L[19];u = L[20];v = L[21];w = L[22];x = L[23];y = L[24];z = L[25]
 txtt = raw_input (('{\n').lower())
 txt = txtt.lower ()
 new1 = txt.replace ('a', a)
 new2 = new1.replace ('b', b)
 new3 = new2.replace ('c', c)
 new4 = new3.replace ('d', d)
 new5 = new4.replace ('e', e)
 new6 = new5.replace ('f', f)
 new7 = new6.replace ('g', g)
 new8 = new7.replace ('h', h)
 new9 = new8.replace ('i', i)
 new10 = new9.replace ('j', j)
 new11 = new10.replace ('k', k)
 new12 = new11.replace ('l', l)
 new13 = new12.replace ('m', m)
 new14 = new13.replace ('n', n)
 new15 = new14.replace ('o', o)
 new16 = new15.replace ('p', p)
 new17 = new16.replace ('q', q)
 new18 = new17.replace ('r', r)
 new19 = new18.replace ('s', s)
 new20 = new19.replace ('t', t)
 new21 = new20.replace ('u', u)
 new22 = new21.replace ('v', v)
 new23 = new22.replace ('w', w)
 new24 = new23.replace ('x', x)
 new25 = new24.replace ('y', y)
 new26 = new25.replace ('z', z)
 folder.write ((new26).lower ())
 if txtt == '#':
   folder.close
   raw_input ('<quit>')
   quit ()
