from random import randint

arrDadu = [randint(1,6)]
print(arrDadu[0])
inputan = input('Ingin mengacak lagi [y/n]? : ')
repeat = True
repeated = 1

def getStatistik(dadu):
    dadu.sort()
    strDadu = list(map(str,dadu))
    newArr = [[],[],[],[],[],[]]
    for x in range(len(strDadu)):
        if strDadu[x] == '1':
            newArr[0].append(strDadu[x])
        if strDadu[x] == '2':
            newArr[1].append(strDadu[x])
        if strDadu[x] == '3':
            newArr[2].append(strDadu[x])
        if strDadu[x] == '4':
            newArr[3].append(strDadu[x])
        if strDadu[x] == '5':
            newArr[4].append(strDadu[x])
        if strDadu[x] == '6':
            newArr[5].append(strDadu[x])
    print('Angka "1" keluar ' + str(len(newArr[0])) + '\nAngka "2" keluar ' + str(len(newArr[1])) + '\nAngka "3" keluar ' + str(len(newArr[2])) + '\nAngka "4" keluar ' + str(len(newArr[3])) + '\nAngka "5" keluar ' + str(len(newArr[4])) + '\nAngka "6" keluar ' + str(len(newArr[5])))

while repeat:
    dadu = randint(1,6)
    arrDadu.append(dadu)
    print(dadu)
    inputan = input('Apakah mau mengacak lagi, teracak:' + str(repeated) + '? [y/n] : ')
    mengulang = ('y' or 'Y') in inputan
    repeated += 1
    if inputan == 'n' or inputan == 'N':
        getStatistik(arrDadu)
        break
