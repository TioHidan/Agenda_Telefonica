agendatelefonica=[]
i=0
NomeNum=[]

nome =input('Digite o nome : ')
numero=input('Digite o numero : ')
NomeNum.insert(0,nome)
NomeNum.insert(1,numero)
agendatelefonica.append(NomeNum)

for i in agendatelefonica :
    print(i)
