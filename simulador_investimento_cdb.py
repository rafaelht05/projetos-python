#-- Simulador de Investimentos (CDB) --

quantia = float(input("Quanto você deseja investir:R$"))
mes = int(input("Por quantos tempo (meses):"))

taxa_cdb = 1.13 / 100
retorno = 0

for mes in range(1, mes + 1):
    retorno = retorno * (1 + taxa_cdb)
    retorno = retorno + quantia
    print(f"mes {mes}: R$ {retorno: .2f}")
print(f"O valor total ao final:{retorno: .2f}")

#Nome: Rafael Henrique Trajano Série: 2F
