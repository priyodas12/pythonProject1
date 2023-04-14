he = "Priyobrato Das"
she = " Priya Das "
print(len(he))
print(he.find("r"))  # 1
print(he.rfind("r"))  # 6
print(he.capitalize())  # Priyobratodas
print(he.upper())  # PRIYOBRATODAS
print(he.lower())  # priyobratodas
print(he.isdigit())  # False
print(he.isalpha())  # False
print(he.count("a"))  # 2
print(he.replace("a", "x"))  # Priyobrxto Dxs
print(he * 3)  # display 3 times he
print(he.split("r"))  # ['P', 'iyob', 'ato Das']
print(she.strip())  # Removes white spaces in front and back
