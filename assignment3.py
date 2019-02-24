v = []

def add(v,n) :
    v.append(n)

def ins(v,n,i) :
    v.insert(i,n)

def remove_index(v,i) :
    v.pop(i)
def remove_range(v,start,end) :
    del v[start:end]


i = 0

while i < 10 :
    n = int(input("Introduceti un element care sa fie adaugat la sfarsitul sirului :"))

    print("Elementele sirului inainte sa adaugam noul element sunt sunt")

    for j in range(len(v)):
        print(v[j])

    add(v,n)

    print("Noul sir obtinut dupa adaugarea la sfarsit al elementului " , n)

    for j in range(len(v)) :
        print(v[j])

    a = int(input("Introduceti un numar care sa fie adaugar pe pozitia k "))

    k = int(input("Introduceti pozitia k pe care sa fie inserat elementul a "))

    print("sirul initial :")

    for j in range(len(v)) :
        print(v[j])

    ins(v,a,k)

    print("noul sir :")

    for j in range(len(v)) :
        print(v[j])
    
    b = int(input("Introduceti pozitia care sa fie stearsa : " ))

    print("sirul initial ")

    for j in range(len(v)) :
        print(v[j])

    remove_index(v,b)

    print("noul sir :")

    for j in range(len(v)) :
        print(v[j])

    i = i + 1

