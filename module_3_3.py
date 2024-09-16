def print_params(a=1, b="string", c=True):
    print(f"{a}, {b}, {c}")


print_params(a=2)
print_params(b="plop", c=not True)
print_params(a=int("1"), b="".join(["a", "b", "c"]), c=not True)
print_params()

print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [True, "plop", ()]
values_dict = {"b": True, "c": 1, "a": "string"}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [0.1, []]
print_params(*values_list_2, 42)
