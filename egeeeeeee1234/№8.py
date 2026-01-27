from itertools import *
k=0
c=0
for w in product('буквы в алфавитном порядке',repeat=кол-во букв в слове):
    k+=1 #общий номер слова
    word=''.join(w)
    if условие: #если не должно быть какой-то буквы - word.count('буква')==0 (или word[0]!='буква'), если слово должно начинаться с какой-либо буквы - word[0]=='буква', заканчиваться - word[-1]=='буква'
        c+=1 # слова, подходящие под условие
        print()


#задание с подбором шифра
from itertools import *
k=0
c=0
for w in product('123456',repeat=5): #всего 6 символов, в каждом коде по 5 символов
    k+=1
    word=''.join(w)
    if ((word.count('3')==1) \
        and ((sum([1 for s in word if int(s)%2==0]))<=(sum([1 for s in word if int(s)%2!=0])))): #в шифре должна быть всего одна тройка, и количество нечётных чисел не должно привышать количества чётных чисел (тобеж меньше или равно). Цикл [1 for s in word if int(s)%2==0 будет добавлять единичку, если цифра (не само число!!!, тобеж не сам код) будет чётной, в конце концов все эти единички будут суммироваться при помощи функции sum, а впоследствии сравниваться с результатом второго цикла, который делает всё тоже самое, но только считает нечётные цифры в шифре.
        c+=1

        print(k,c,word) #первая переменная - общий номер, вторая - номер шифра, подошедшего конкретно под условие, третья - сам шифр.





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
