# regras de produção da gramática implementadas na forma de um dicionário.
# chaves: número da regra (como string)
# valores: dupla de listas aonde o primeiro elemento é o lado esquerdo da produção,
# e o segundo elemento é uma lista com o lado direito

# exemplo: primeiras regras de produção da gramática mgol
production_rule = {
    # P'->P
    '1': ('P\'', ['P']),
    # P -> inicio V A
    '2': ('P', ['inicio', 'V', 'A'])
}