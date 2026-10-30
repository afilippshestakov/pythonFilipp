# 1. Scrivi una funzione chiamata trova_pari che accetta una lista di numeri interi e restituisce una nuova lista
# contenente solo i numeri pari.

# [1, 2, 3, 4, 5, 6]
# [7, 9, 11]



def trova_pari(num_int):
	num_pari = []
	for a in num_int:
		if not a % 2:
			num_pari.append(a)
	return num_pari


print(trova_pari([7, 1, 2, 3, 4, 5, 6]))
print(trova_pari([7, 9, 11]))