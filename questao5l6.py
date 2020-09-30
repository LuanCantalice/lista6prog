x = str(input("Se deseja converter de C(elsius) para F(arenheit) digite 1\nSe deseja converter de F(arenheit) para C(elsius) digite 2\n:"))

if(x=="1"):
    temp = float(input("Digite a temperatura em Celsius: "))
    grauconv = (9*temp+160)/5
    print(temp, "Graus Celsius convertidos para Farenheit da o total de %.1f" %grauconv, "Graus Farenheit")
else:
    temp = float(input("Digite a temperatura em Farenheit: "))
    grauconv = (temp-32)/1.8
    print(temp, "Graus Farenheit convertidos para Celsius da o total de %.1f" %grauconv, "Graus Celsius")
