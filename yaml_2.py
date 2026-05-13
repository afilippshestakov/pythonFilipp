# Taken from mission YAML. Simple Dict

def yaml(a: str) -> dict:
    # your code here
    result_dict = {}
    #startswith
    #endswith
    #k.strip
    a_lst = a.split('\n')
    for b in a_lst:
        if not b:
            continue
        k, v = b.split(":")
        k = k.strip()
        v = v.strip()
        if v.endswith('"') and v.startswith('"'):
            v = v[1:-1]
            v = v.replace('\\"', '"')
        else:
            if v == 'false':
                v = False
            elif v == 'true':
                v = True 
            elif v == '':
                v = None
            elif v == 'null':
                v = None
            elif v.isdigit():
                v = int(v)


        result_dict[k] = v
    return result_dict



print("Example:")
print(yaml('name: "Bob Dylan"\nchildren: 6\ncoding: "null" '))

# These "asserts" are used for self-checking
assert yaml("name: Alex\nage: 12") == {"name": "Alex", "age": 12}
assert yaml("name: Alex Fox\nage: 12\n\nclass: 12b") == {
    "name": "Alex Fox",
    "age": 12,
    "class": "12b",
}
assert yaml('name: "Alex Fox"\nage: 12\n\nclass: 12b') == {
    "name": "Alex Fox",
    "age": 12,
    "class": "12b",
}
assert yaml('name: "Alex \\"Fox\\""\nage: 12\n\nclass: 12b') == {
    "name": 'Alex "Fox"',
    "age": 12,
    "class": "12b",
}
assert yaml('name: "Bob Dylan"\nchildren: 6\nalive: false') == {
    "name": "Bob Dylan",
    "children": 6,
    "alive": False,
}
assert yaml('name: "Bob Dylan"\nchildren: 6\ncoding:') == {
    "name": "Bob Dylan",
    "children": 6,
    "coding": None,
}
assert yaml('name: "Bob Dylan"\nchildren: 6\ncoding: null') == {
    "name": "Bob Dylan",
    "children": 6,
    "coding": None,
}
assert yaml('name: "Bob Dylan"\nchildren: 6\ncoding: "null" ') == {
    "name": "Bob Dylan",
    "children": 6,
    "coding": "null",
}

print("The mission is done! Click 'Check Solution' to earn rewards!")