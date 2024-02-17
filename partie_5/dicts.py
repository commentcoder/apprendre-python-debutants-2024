nombres = {"un": 1, "deux": 2, "trois": 3}

print(nombres["un"])
print(nombres.get("deux"))
print(nombres.get("quatre", "4 n'est pas dans le dictionnaire"))
nombres.update({"quatre": 4})
nombres.pop("trois")

print(nombres.keys())
print(nombres.values())
print(nombres.items())
