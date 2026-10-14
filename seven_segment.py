
'''
div_indicators() deve dividere i dati(prima il primo e poi il secondo indicatore)

convert_cifra() coverte set di lettere in cifra
'''

DICT_CONV = {
    ''.join(sorted("bc")): 1,
    ''.join(sorted("degba")): 2,
    ''.join(sorted("dcgba")): 3,
    ''.join(sorted("bcgf")): 4,
    ''.join(sorted("dcgfa")): 5,
    ''.join(sorted("acdefg")): 6,
    ''.join(sorted("abc")): 7,
    ''.join(sorted("abcdefg")): 8,
    ''.join(sorted("abcdfg")): 9,
    ''.join(sorted("abcdef")): 0
    }



def seven_segment(lit_seg, broken_seg):
    lit_primo, lit_secondo = div_indicator(lit_seg)
    broken_primo, broken_secondo = div_indicator(broken_seg)
    mask_primo = set(lit_primo + broken_primo)
    mask_secondo = set(lit_secondo + broken_secondo)

    dict_lit = {}
    for key_lett,val_num in DICT_CONV.items():
        if ''.join(sorted(lit_primo)).lower() in key_lett:
            dict_lit[key_lett] = val_num

    conteiner_1 = []
    for key_lett,val_num in dict_lit.items():
        out_seg = mask_select(mask_primo, key_lett)
        if out_seg == key_lett:
            conteiner_1.append(val_num)
            print(conteiner_1)

    dict_lit = {}
    for key_lett,val_num in DICT_CONV.items():
        if ''.join(sorted(lit_secondo)).lower() in key_lett:
            dict_lit[key_lett] = val_num

    conteiner_2 = []       
    for key_lett,val_num in dict_lit.items():  
        out_seg = mask_select(mask_secondo, key_lett)
        if out_seg == key_lett:
            conteiner_2.append(val_num)
            print(conteiner_2)
    num_comb = len(conteiner_1) * len(conteiner_2)
    print(f"le combinazioni sono: {num_comb}")

    return num_comb

def div_indicator(duble_set):
    mai_ind = []
    min_ind = [] 
    for e in duble_set:
        if e.isupper():
            mai_ind.append(e)
        else:
            min_ind.append(e)

    return mai_ind, min_ind 

def convert_ind(lett_ind):
    lett_ind = ''.join(sorted(lett_ind)).lower()

    return DICT_CONV[lett_ind]

def mask_select(mask_seg, num_lett):
    out_seg = ""
    mask_seg_str = ''.join(mask_seg).lower()

    for s in num_lett:
        if s in mask_seg_str:
            out_seg = out_seg + s

    return ''.join(sorted(out_seg.lower()))


if __name__ == '__main__':
    # simple_set = {'B', 'C', 'b', 'c'}
    # broken_seg = {"A"}
    # print(f"function result: {seven_segment(simple_set, broken_seg)}")
    # # print(simple_set)
    # # primo_ind, secondo_ind = div_indicator(simple_set)
    # # print(broken_seg)
    # mask_primo = {'B', 'C', 'A'}
    # mask_secondo = {'b', 'c'}


    # conteiner_1 = []
    # for key_lett,val_num in DICT_CONV.items():
    #     out_seg = mask_select(mask_primo, key_lett)
    #     if out_seg == key_lett:
    #         conteiner_1.append(val_num)
    #         print(conteiner_1)

    # conteiner_2 = []       
    # for key_lett,val_num in DICT_CONV.items():  
    #     out_seg = mask_select(mask_secondo, key_lett)
    #     if out_seg == key_lett:
    #         conteiner_2.append(val_num)
    #         print(conteiner_2)
    # num_comb = len(conteiner_1) * len(conteiner_2)
    # print(f"le combinazioni sono: {num_comb}")
    
    print(f"il result e stato {seven_segment({'B', 'C', 'b', 'c'}, {'A'})}")
    assert seven_segment(["A","B","C","D","E","F","a","b","c","d","e","f"],["G","g"]) == 4
    assert seven_segment({'A', 'B', 'C', 'D', 'E', 'F', 'a', 'b', 'c', 'd', 'e', 'f'}, {'G', 'g'}) == 4    #0, 8, 80, 88                
    assert seven_segment({'B', 'C', 'b', 'c'}, {'A'}) == 2, '11, 71'
    print(seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}))
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'e'}) == 6, '15, 16, 35, 36, 75, 76'
    assert seven_segment({'B', 'C', 'a', 'f', 'g', 'c', 'd'}, {'A', 'G', 'D', 'F', 'b', 'e'}) == 20, '15...98'
    print('"Run" is good. How is "Check"?')