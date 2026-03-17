def translatio(ntext: str) -> str:
    # your code here
    ndx_c = 0
    nuova_frase = ""
    for ndx_t, e in enumerate(text[:-1]):
        if e == " ":
            nuova_frase = nuova_frase + " "
            ndx_c = ndx_t + 1
            continue
        elif ndx_t == ndx_c:
            nuova_frase = nuova_frase + e
        elif ndx_t >= len(text) - 1:
            break
        else:
            continue
        if e in "aeiouy":
            ndx_c = ndx_c + 3
        else:
            ndx_c = ndx_c + 2
    return nuova_frase