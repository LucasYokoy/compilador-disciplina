# tabela de transição implementada na forma de dicionário aonde as chaves são duplas e os valores são strings
# syntactic_table[(estado_atual, entrada)] = ação
# se não houver o símbolo na tabela, retornar ERROR
class SyntacticTable:
    def __init__(self, _table):
        self.syntactic_table = _table

    def action(self, state, symbol):
        try:
            return self.syntactic_table[(state, symbol)]
        except KeyError:
            return 'ERROR'


table = {
    ('estado', 'símbolo_de_entrada'): 'ação'
}

syntactic_table = SyntacticTable(table)
