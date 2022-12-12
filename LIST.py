#nimi=input("Mis on sinu nimi?: ")
#tahed=list(nimi)
#n=len(tahed)
#print(f"{n} tahed: {tahed}")
#print("Remove kasutamine")
#t=input("Sisesta taht, mis vaja kustutada ara")
#nt=tahed.count(t)
#print(nt)
#j=0
#if nt==0:
#    print(f"{t} ei ole listis")
#else:
#    for i in range(len(tahed)):
#        if tahed [i-j]==t: 
#            tahed.pop(i-j)
#            j+=1
#    print(f"Nuud {t} ei ole listis, on jaanud {tahed}")
#    else:
#        t=input("Mis taht on vaja otsida?")
#        print(f"Taht {t} seiseb {tahed.index(t)+1} positsioonil")
#j=0


#Практическая работа. Тема Списки
index=input("Postiindeks: ")
tahed=list(index)
n=len(tahed)
print(f"{n} tahed: {tahed}")
index_list=list(index)
if index_list[1]==1:
    print("jää koju!!!")
elif index_list[1]==2:
    print("jää koju!!!")
elif index_list[1]==3:
    print("jää koju!!!")
else:
    print("Kanna maski!!!")