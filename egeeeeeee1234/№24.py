#s=open('24-1.txt').readline()
#m=0
#s='ABBBFHRGHDUGERGHSIUFDHOIUDSHGIOUHGUIOSDHFGOHDASOFGHSOIDGHOIEHG'
#for l in range(len(s)):
  #  for r in range(l,len(s)):
    #    c=s[l:r+1]
      #  if 'D' not in c:
        #    m=max(len(c),m)
        #else:
          #  break
#print(m)

#s=open('24-2.txt').readline()
#m=0
#for l in range(len(s)):
  #  for r in range(l+m,len(s)):
    #    c=s[l:r+1]
      #  if 'PR' not in c and 'RP' not in c:
        #    m=max(len(c),m)
        #else:
          #  break
#print(m)

#s=open('24-3.txt').readline()
#m=0
#for c in s:
  #  if c in 'QWERTYUIOPASDFGHJKLZXCVBNM':
    #    s=s.replace(c,'*')
#for c in s:
  #  if c in '0123456789':
    #    s=s.replace(c,'?')
#for l in range(len(s)):
  #  for r in range(l+m,len(s)):
    #    c=s[l:r+1]
      #  if '**' not in c and '??' not in c:
           # m=max(len(c),m)
        #else:
          #  break
#print(m)

#s=open('24-4.txt').readline()
#m=0
#for l in range(len(s)):
  #  for r in range(l+m,len(s)):
    #    c=s[l:r+1]
      #  k=0
        #for i in range(len(c)-1):
          #  if c[i]!=c[i+1]:
            #    k+=1
        #if k==len(c)-1:
          #  m=max(len(c),m)
        #else:
          #  break
#print(m)


#или

#s=open('24-4.txt').readline()
#m=0
#for l in range(len(s)):
  #  for r in range(l+m,len(s)):
    #    c=s[l:r+1]
      #  if all(c[i]!=c[i+1] for i in range(len(c)-1)):
        #    m=max(len(c),m)
        #else: break
#print(m)





#s=open('24-5.txt').readline()
#m=0
#for l in range(len(s)):
  #  for r in range(l+m,len(s)):
    #    c=s[l:r+1]
      #  if all(c[i]+c[i+1]+c[i+2]!=c[i+3]+c[i+4]+c[i+5] for i in range(len(c)-5)):
        #    m=max(len(c),m)
        #else:
          #  break
#print(m)




#s=open('24-6.txt').readline()
#m=0
#for l in range(len(s)):
  #  for r in range(l+m,len(s)):
    #    c=s[l:r+1]
      #  if all(c[i]+c[i+1] in 'ZX' or c[i]+c[i+1] in 'ZY' for i in range(0,len(c)-1,2)):
        #    m=max(len(c),m)
        #else:
          #  break
#print(m/2)
        



s=open('24-7.txt').readline()
m=0
for l in range(len(s)):
    for r in range(l+m,len(s)):
        c=s[l:r+1]
        if all(c[i]+c[i+1] in 'AA' or c[i]+c[i+1] in 'CC' for i in range(0,len(c)-1,2)):
            m=max(len(c),m)
        else:
            break
print(m//2)















