def translation(ntext: str) -> str:
    """ transforma le frasi degli uccelli in frasi degli umani """
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

print("Example:")
print(translation("hieeelalaooo"))

# These "asserts" are used for self-checking
assert translation("hieeelalaooo") == "hello"
assert translation("hoooowe yyyooouuu duoooiiine") == "how you doin"
assert translation("aaa bo cy da eee fe") == "a b c d e f"
assert translation("sooooso aaaaaaaaa") == "sos aaa"

print("The mission is done! Click 'Check Solution' to earn rewards!")