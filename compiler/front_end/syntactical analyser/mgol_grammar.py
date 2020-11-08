# regras de produção da gramática implementadas na forma de um dicionário.
# chaves: número da regra (como string)
# valores: dupla de listas aonde o primeiro elemento é o lado esquerdo da produção,
# e o segundo elemento é uma lista com o lado direito

# exemplo: primeiras regras de produção da gramática mgol
production_rule = {
    # P'->P
    '1': ('P\'', ['P']),
    # P -> inicio V A
    '2': ('P', ['inicio', 'V', 'A']),
    # V -> varinicio LV
	'3': ('V', ['varinicio', 'LV']),
	# LV -> D LV
	'4': ('LV', ['D', 'LV']),
	# LV -> varfim;
	'5': ('LV', ['varfim']),
	# D -> id TIPO;
    '6': ('D', ['id', 'TIPO']),
	# TIPO -> int
    '7': ('TIPO', ['int']),
	# TIPO -> real
    '8': ('TIPO', ['real']),
	# TIPO -> lit
    '9': ('TIPO', ['lit']),
	# A -> ES A
	'10': ('A', ['ES', 'A']),
    # ES -> leia id;
	'11': ('ES', ['leia', 'id', ';']),
    # ES -> escreva ARG;
	'12': ('ES', ['escreva', 'ARG', ';']),
    # ARG -> literal
	'13': ('ARG', ['literal']),
    # ARG -> num
	'14': ('ARG', ['num']),
    # ARG -> id
	'15': ('ARG', ['id']),
    # A -> CMD A
	'16': ('A', ['CMD', 'A']),
    # CMD -> id rcb LD;
	'17': ('CMD', ['id', 'rcb', 'LD']),
    # LD -> OPRD opm OPRD
	'18': ('LD', ['OPRD', 'opm', 'OPRD']),
    # LD -> OPRD
	'19': ('LD', ['OPRD']),
    # OPRD -> id
	'20': ('OPRD', ['id']),
    # OPRD -> num
	'21': ('OPRD', ['num']),
    # A -> COND A
	'22': ('A', ['COND', 'A']),
    # COND -> CABEÇALHO CORPO
	'23': ('COND', ['CABEÇALHO', 'CORPO']),
    # CABEÇALHO -> se (EXP_R) então
	'24': ('CABEÇALHO', ['se', '(', 'EXP_R', ')', 'então']),
    # EXP_R -> OPRD opr OPRD
	'25': ('EXP_R', ['OPRD', 'opr', 'OPRD']),
    # CORPO -> ES CORPO
	'26': ('CORPO', ['ES', 'CORPO']),
    # CORPO -> CMD CORPO
	'27': ('CORPO', ['CMD', 'CORPO']),
    # CORPO -> COND CORPO
	'28': ('CORPO', ['COND', 'CORPO']),
    # CORPO -> fimse
	'29': ('CORPO', ['fimse']),
    # A -> fim
    '30': ('A', ['fim'])
}