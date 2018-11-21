from datetime import datetime
from datetime import date
def main():
    now = datetime.now()
    marca = []
    modelo = []
    ano = []
    codigo = []
    valor = []
    status = []
    alugado = 0
    cod = 0
    a = 0
    atrasado = 0
    hj = date.today()
    while True:
        print("╔═══════════════════════════════════════════╗")
        print("║           Bem-vindo                       ║")
        print("╠═══════════════════════════════════════════╣")
        print("║ 1- Consultar veículos                     ║")
        print("║ 2- Adicionar veículos                     ║")
        print("║ 3- Alugar/Reservar veículos               ║")
        print("║ 4- Devolver/Liberar veículos              ║")
        print("║ 5- Excluir veículos                       ║")
        print("║ 6- Avançar data atual                     ║")
        print("║ 7- Sair                                   ║")
        print("║                        Data:",hj,"  ║")
        print("║     Quantidade de veiculos cadastrados:",len(marca),            "║")
        print("║     Quantidade de veiculos alugados:",alugado,                  "   ║")
        print("║     Quantidade de veiculos atrasados:",atrasado,                "  ║")
        print("╚═══════════════════════════════════════════╝")

        opcao = int(input("Escolha a opção desejada:"))
        if(opcao == 1):
           if len(marca) == 0:
               print("Não temos veículos cadastrados.")
           else:
               print("Códigos: ",codigo)
               print("Modelos: ",modelo)
               print("Status do veículo: ", status)
               detalhes = input("Deseja ver detalhes? s/n: ")
               if(detalhes == 's'):
                   print("Marcas: \n",marca,"\nAno: \n",ano, "\nValor da diária:", valor)
        if(opcao == 2):
            marca.append (input("Qual a marca do veículo? \n"))
            modelo.append (input("Qual o modelo do veículo? \n"))
            ano.append(input("Qual o ano do veículo? \n"))
            valor.append(input("Qual o valor da diária do veículo? \n"))
            status.append('Disponível')
            cod=cod+1
            codigo.append(cod)
        if(opcao == 3):
            op = input("Deseja alugar ou reservar um veículo: (alugar/reservar)")
            if(op == 'alugar'):
                 codigo = input("Escreva o código do veículo que deseja alugar: ")
                 if codigo in codigo:
                     b = int(codigo)- 1
                     if status[b] == 'Alugado':
                         print("Veículo já alugado")
                     if status[b] == 'Reservado':
                         print("Impossível alugar o veículo, pois o mesmo se encontra reservado. Tente outro por favor!")
                     else:
                         aluguel = (input("Deseja alugar o veículo?(s/n)"))
                         if(aluguel == 's'):
                             status.remove('Disponível')
                             nome = input("Qual o seu nome? ")
                             data = date.fromordinal(hj.toordinal()+(int(input("Quantos dias deseja alugar o veículo?"))))
                             total = data - hj
                             pagar = total.days
                             a = int(codigo) - 1
                             b = float(valor[a])
                             print("Senhor: ",nome, "O valor do aluguel do veículo é: ",pagar*b,"reais")
                             confirmar = input("Deseja confirmar o aluguel?(s/n)")
                             if confirmar == 's':
                                     diferenca = data - hj
                                     diasAlugado = diferenca.days
                                     if diasAlugado >=0:
                                         status.append('Alugado')
                                         alugado = alugado+1
                                 
            if(op == 'reservar'):
                 codigo = input("Escreva o código do veículo que deseja reservar: ")
                 if codigo in codigo:
                     b = int(codigo)- 1
                     if status[b] == 'Reservado':
                         print("O veículo já encotra-se Reservado.")
                     if status[b] == 'Alugado':
                         print("Impossível reservar o veículo, pois o mesmo se encontra alugado. Tente outro por favor!")
                     else:
                         reservar = (input("Deseja reservar o veículo?(s/n)"))
                     if(reservar == 's'):
                         status.remove('Disponível')
                         nome = input("Qual o seu nome? ")
                         data = date.fromordinal(hj.toordinal()+(int(input("Quantos dias deseja reservar o veículo?"))))
                         diferenca = data - hj
                         dias = diferenca.days
                         if dias >=0:
                             status.append('Reservado')
        if(opcao ==4):
            ope = input("Deseja entregar ou liberar veículo de reserva?(Se entregar digite 1, se liberar digite 2)")
            if(ope == '1'):
                codigo = input("Escreva o código do veículo que deseja entregar: ")
                if codigo in codigo:
                     print("Senhor: ",nome)
                     resposta = input("Deseja entregar o veículo?(s/n)")
                     if (resposta == 's'):
                         if (atrasado > 0):
                             multa = (atrasado*pagar) + (pagar * b)
                             print("O valor é: ", pagar*b," como teve um atraso de: ", atrasado, "O valor a ser pago é: ",multa)
                             status.remove('Atrasado')
                             status.append('Disponivel')
                             alugado = alugado-1
                             atrasado = atrasado - 1
                         else:
                            status.remove('Atrasado')
                            status.append('Disponivel')
                            alugado = alugado-1
                            atrasado = atrasado - 1
            if (ope == '2'):
                codigo = input("Escreva o código do veículo que deseja entregar: ")
                if codigo in codigo:
                        print("Senhor: ",nome)
                        resposta = input("Deseja liberar o veículo?(s/n)")
                        if (resposta == 's'):
                            status.remove('Reservado')
                            status.append('Disponivel')
                            atrasado = atrasado-1
        if(opcao == 5):
            codigo = input("Escreva o código do veículo que deseja excluir: ")
            if codigo in codigo:
                    resposta = input("Deseja excluir o veículo?(s/n)")
                    if (resposta == 's'):
                      status.remove('Disponível')
                      a = int(codigo)- 1
                      del marca[a]
                      del modelo[a]
                      del ano[a]
                      print("Veículo excluído ccom sucesso")
        if(opcao == 6):
            if len(codigo) == 0:
                futuro = date.fromordinal(hj.toordinal()+1)
                hj=futuro
            else:
                futuro = date.fromordinal(hj.toordinal()+1)
                hj=futuro
                diasAlugado = diasAlugado-1
                if diasAlugado < 0:
                        a = int(codigo)- 1
                        del status[a]
                        status.append('Atrasado')
                        atrasado = atrasado+1
        if(opcao == 7):
            break
        if(opcao>7):
            print("Opção inválida.\n Escolha outra opção")
            break
        
main() 
