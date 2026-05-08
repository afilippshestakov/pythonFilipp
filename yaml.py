def yaml(a: str) -> dict:
    # your code here
    result_dict = {}
    
    a_lst = a.split('\n')
    for b in a_lst:
        if not b:
            continue
        k, v = b.split(": ")
        try:
            v = int(v)
        except ValueError as e:
            pass

        result_dict[k] = v



    return result_dict
    

print("Example:")
print(yaml("name: Alex\nage: 12"))

# These "asserts" are used for self-checking
assert yaml("name: Alex\nage: 12") == {"name": "Alex", "age": 12}
assert yaml("name: Alex Fox\nage: 12\n\nclass: 12b") == {
    "age": 12,
    "name": "Alex Fox",
    "class": "12b",
}

print("The mission is done! Click 'Check Solution' to earn rewards!")