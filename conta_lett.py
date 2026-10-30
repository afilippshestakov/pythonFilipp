# 2. Scrivi una funzione chiamata conta_lettere che accetta una stringa come argomento e restituisce un dizionario.
# Il dizionario deve contenere ogni carattere della stringa come chiave e il numero di volte che appare come valore.

# "banana"
# "programma"




def conta_lettere(str_input: str) -> dict:
  result_dict = {}
  for c in str_input:
    if c in result_dict:
      # result_dict[c] = result_dict.get(c) + 1 
    	result_dict[c] += 1
    else:
      result_dict[c] = 1
  return result_dict


print(conta_lettere("banana"))
     