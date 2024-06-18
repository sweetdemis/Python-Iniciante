#sets só podem ter itens removidos e adicionados, e não editados
#eles tambem sao desordenados, nao da pra prever a ordem que vai ser impressa
#nao aceita valores duplicados, mas aceita todo tipo de dado, inclusive misturados
frutas = {"banana", "melancia", "pera", "banana"} #chaves
print(frutas)

frutas.add("maça")

frutas.remove("banana")
frutas.pop() #como a lista nao é ordenada nao da pra saber qual vai ser removido

set1 = {"fubanga", 28, False}
print(set1)

