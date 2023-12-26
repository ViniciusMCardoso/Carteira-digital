vendedores=[]
valores=[]
nloja=[]
comissões=[]
continuar = 1
mv=0


while continuar == 1:
    vendedor=input("Digite o nome do vendedor: ")
    vendedores.append(vendedor)


    loja=input("Digite o numero da loja: ")
    nloja.append(loja)


    valor=float(input("Digite o valor mensal vendido: "))
    valores.append(valor)


    comissões.append(valor*0.08)
    if valor>mv:
        mv=valor
        vmv= vendedor
    continuar = int(input("Adcionar mais um vendedor? digite 1 para sim; 2 para não\n"))


print("\nVendedor com maior venda mensal:",vmv,"/ Com um total de:",mv)
print("\nComissões por vendedor:",comissões)
print("\nBonus para:",vmv,"/ Total de:",mv+300)