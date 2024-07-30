class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Gourmet'
restaurante_praca.ativo = True

restaurante_pizza = Restaurante()    

restaurantes = [restaurante_praca, restaurante_pizza]

print(restaurantes)
