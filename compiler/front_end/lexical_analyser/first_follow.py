first = {	 "P'":       	 {"inicio"},
			 "P":        	 {"inicio"},
			 "V":        	 {"varinicio"},
			 "A":        	 {"fim", "leia", "escreva", "id", "se"},
			 "ES":       	 {"leia", "escreva"},
			 "CMD":      	 {"id"},
			 "COND":     	 {"se"},
			 "CABEÇALHO":	 {se},
			 "LV":       	 {"id", "varfim"},
			 "D":        	 {"id"},
			 "TIPO":     	 {"int", "real", "lit"},
			 "ARG":      	 {"literal", "num", "id"},
			 "LD":       	 {"id", "num"},
			 "OPRD":     	 {"id", "num"},
			 "CORPO":    	 {"fimse", "leia", "escreva", "id", "se"}
			 "EXP_R":    	 {"id", "num"}
}

follow = {	"P'":     	     {"$"},
			"P":         	 {"$"},
			"V":         	 {"fim", "leia", "escreva", "id", "se"},
			"A":         	 {"$"},
			"ES":        	 {"fimse", "leia", "escreva", "id", "se", "fim"},
			"CMD":       	 {"fimse", "leia", "escreva", "id", "se", "fim"},
			"COND":      	 {"fimse", "leia", "escreva", "id", "se", "fim"},
			"CABEÇALHO": 	 {"fim", "leia", "escreva", "id", "se"},
			"LV":        	 {"fim", "leia", "escreva", "id", "se"},
			"D":         	 {"id", "varfim"},
			"TIPO":      	 {";"},
			"ARG":       	 {";"},
			"LD":        	 {";"},
			"OPRD":      	 {"opm", "opr", ";", ")"},
			"CORPO":     	 {"fimse", "leia", "escreva", "id", "se", "fim"}
			"EXP_R":     	 {")"}

}
