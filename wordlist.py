import os
os.system('clear')
m = '\033[1;32m'
c = '\033[3;31m'
b="\033[0;34m"
g="\033[1;32m"
w="\033[1;37m"
r="\033[1;31m"
y="\033[1;33m"
cyan = "\033[0;36m"
lgray = "\033[0;37m"
dgray = "\033[1;30m"
ir = "\033[0;101m"
reset = "\033[0m"
print(b)
os.system
print(w)

print('########################################')

print(r)

print('    Author  : Mr.B3604')

print(cyan)

print('    Tool    : Hack Instagram v.1')

print(lgray)

print('    YouTube : GUNAWAN ID')

print(w)

print('########################################')
print('\r')
os.system('print "\033[1;33m"')
aaa=input('ketik (pass.txt) : ')
os.system('clear')
print(w)

print('########################################')

print(r)

print('    Author  : Mr.B3604')

print(cyan)

print('    Tool    : Hack Instagram v.1')

print(lgray)

print('    YouTube : GUNAWAN ID')

print(w)

print('########################################')
os.system('print "\033[1;33m"')
file=open(aaa,'w')
aa=set([])
oio=set([])
#iio=set([112233,332211,000,445566,'$'*1,'$'*2,'$'*3,'@'*1,'@'*2,'@'*3,'€'*1,'€'*2,'€'*3,'&'*1,'&'*2,'&'*3,'¥'*1,'¥'*2,'¥'*3,'*'*1,'*'*2,'*'*3,'+'*1,'+'*2,'+'*3])
kk=1
while True :
    b=input('\033[1;33mpassword {} : '.format(kk))
    if b=='save' :
        print('\033[3;33m')
        file.close()
        qq=open(aaa, 'r' )
        ll=len(qq.readlines())
        os.system('printf "\033[3;33m"')
        print('÷'*40)
        print(' {} password di simpan ---> {} '.format(ll, aaa))
        print('÷'*40)
        break ;
    aa.add(b)
    for i in aa:
        if len(i) >= 6 and i not in oio :
            oio.add(i)
            file.write(i)
            file.write('\n')
            #for o in iio:
             #   uau='{}{}'.format(i,o)
              #  ubu='{}{}{}'.format(o,i,o)
               # ucu='{}{}{} '.format(i,o,i)
                #if len(uau)>= 6:
                   # file.write(uau)
                  #  file.write('\n')
               # if len(ubu) >= 6 and ubu != uau :
                   # file.write(ubu)
                   # file.write('\n')
                #if len(ucu) >= 6 and ucu != uau and ucu != ubu:
                  #  file.write(ucu)
                  #  file.write('\n')

        c=b+i
        d=i+b
        if len(c) >= 6 :
            file.write(c)
            file.write('\n')
        if c != d and len(d) >= 6:
            file.write(d)
            file.write('\n')
    kk=int(kk)+1
    print('-'*40)
