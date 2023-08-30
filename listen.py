agendatelefonica=[]
i=0
res=0
NomeNum=[]
j=0


while res!=5 :
 
 
 print("1- inserir lista \n")
 print("2- Mostrar contatos")
 print("3- editar contatos")
 print("4- remover Contato \n ")
 print("5- Sair\n")
 res= int (input("O que deseja fazer : "))

 if res==1 :
  nome =input('Digite o nome : ')
  NomeNum.append(nome)
  numero=input('Digite o numero : ')
  NomeNum.append(numero)
  agendatelefonica.append(NomeNum)

 if res==2 :
  for i in agendatelefonica :
    
       print("Contato : ",i[0],"Numero : ",i[1])
     
 if res==3 :
   nome=input("Digite o nome a ser editado : ")
   for i in range(len(agendatelefonica)) :
     if agendatelefonica[i][0]==nome :
      novo_nome=input("Digite o novo nome do contato : ")
      novo_numero= input("Digite o novo numero do contato : ")
      agendatelefonica[i][0]=novo_nome
      agendatelefonica[i][1]=novo_numero
      #os.system('cls')
      break
 
     