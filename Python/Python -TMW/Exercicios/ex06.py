#Faça um programa que exiba a seguinte receita de bolo de chocolate. Exiba um item por vez, conforme a pessoa aperte “enter”.

intro = int(input("""
O que voce gostaria de saber sobre a receita de bolo de chocolate?
1 - Ingredientes
2 - Modo de preparo
              """))

if intro == 1:
    input("2 xícaras de farinha de trigo")
    input("1 xícara de açúcar")
    input("1/2 xícara de cacau em pó")
    input("1 colher de chá de fermento em pó")
    input("1/2 xícara de óleo vegetal")
    input("1 colher de chá de bicarbonato de sódio")
    input("2 ovos")
    input("1/2 colher de chá de sal")
    input("1 xícara de leite")
    input("2 colheres de chá de extrato de baunilha")
    input("1 xícara de água fervente")
elif intro == 2:
    input("Pré-aqueça o forno a 180°C. Unte uma forma de bolo com manteiga e farinha, ou forre-a com papel manteiga.")
    input("Em uma tigela grande, peneire a farinha de trigo, o açúcar, o cacau em pó, o fermento em pó, o bicarbonato de sódio e o sal. Misture bem.")
    input("Em outra tigela, bata os ovos levemente. Adicione o leite, o óleo vegetal e o extrato de baunilha. Misture bem.")
    input("Despeje os ingredientes líquidos na mistura de ingredientes secos e mexa até que tudo esteja bem combinado.")
    input("Adicione a água fervente à massa e misture até que a massa fique homogênea. A massa ficará líquida, mas é normal.")
    input("Despeje a massa na forma preparada e leve ao forno pré-aquecido")
    input("Asse por cerca de 30-35 minutos, ou até que um palito inserido no centro do bolo saia limpo.")
    input("Retire o bolo do forno e deixe esfriar na forma por alguns minutos. Em seguida, transfira para uma grade de resfriamento para esfriar completamente.")
    input("Depois de esfriar, você pode servir o bolo simples ou decorá-lo com cobertura de sua preferência, como ganache de chocolate ou glacê de chocolate.")
else:
    print("Nenhuma opcao certa foi escolhida")
    
