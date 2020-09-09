from datetime import datetime 

nome = input("Qual seu nome? ")
data_nasce = input("Qual sua data de nascimento? ")
data1 = datetime.strptime(data_nasce, "%d/%m/%Y")
data2 = datetime.now()
dataf = data2 - data1
dataf = int(dataf.days/365)
print(f"Voce se chama {nome} e tem {dataf} anos!")