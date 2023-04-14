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
print(he.isprintable())

# Slicing Operation

# [start:stop:step]

f_letter=he[0]
print(f_letter)

f_name=he[0:10]
print(f_name)

l_name=he[11:]
print(l_name)

even_chars=he[0:13:3]
print(even_chars)

print(he[::3])

reversed_name=he[::-1]
print(reversed_name)

web1="https://www.g00gle.com"

print("hostname:  "+web1[12:18])