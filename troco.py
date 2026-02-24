valor = float(input("Digite o valor do produto ").replace(",", "."))
pago = float(input("Digite o valor que voce pagou ").replace(",", "."))
troco = pago - valor

if troco > 0:
    print(f"O seu troco é de \033[92mR$ {troco:.2f}\033[0m reais ")
elif troco == 0:
    print("Você pagou o valor completo, muito obrigado pela compra ")
else:
    print(f"Você pagou R$ {pago:.2f} e ficou devendo \033[91mR$ {abs(troco):.2f}\033[0m reais ")

