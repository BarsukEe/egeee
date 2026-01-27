from itertools import *
#k=0
#c=0
#for i in product('АГИНРТ',repeat=6):
 #   k+=1
 #   w=''.join(i)
  #  if k%2!=0 and w[0]!='А' and w[0]!='И' and w[0]!='Г' and w.count('А')==1:
  #      print(w,k)
  #      break

#k=0
#c=0

#for w in product('0123456789ABC',repeat=3):
#    k+=1
#    word=''.join(w)
#    word=word.replace('1','*')
 #   word=word.replace('3','*')
#    word=word.replace('5','*')
 #   word=word.replace('7','*')
 #   word=word.replace('9','*')
 #   word=word.replace('B','*')
 #   if word[0]!='0' and k%10==7 and word.count('**')==0:
 #       c+=1
#print(c)    
k=0
c=0
for w in product('0123456789ABC',repeat=6):
    word=''.join(w)
    k+=1
    word=word.replace('A','*')
    word=word.replace('B','*')
    word=word.replace('C','*')
    if word[0]!='0' and word.count('0')>=2 and word.count('**')==1 and word.count('*')==2:
        c+=1
print(c)

