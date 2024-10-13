# exercicio
p = 10
while True:
    age = input("Para saber o preço do seu ingresso, digite sua idade (em anos) ou, se quiser sair, digite 'q' : ")
    
    if age == "q":
        print("Até breve")
        break
    else: 
        age = int(age)
    
    if age <= 5:
        print("o preço do seu ingresso é: ", 0*p)
    elif 5 < age <= 12:
        print("o preço do seu ingresso é: ", 0.5*p)   
    elif 12 < age <= 17:
        print("o preço do seu ingresso é: ", 0.8*p)
    elif 17 < age <= 70:
        print("o preço do seu ingresso é: ", p)
    else:
        print("O preço do seu ingresso é: ", 0*p)
