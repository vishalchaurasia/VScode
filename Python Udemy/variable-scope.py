example="hello world" #global
def loc():
    example="this is a string" #local
    return example

print(example)
print(loc())