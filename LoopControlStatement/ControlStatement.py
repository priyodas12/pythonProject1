# break = used to terminate the loop immediately
# continue = skips to the next iteration of the loop
# pass = does nothing, acts as placeholder

while True:
    name= input("Please enter your name:: ")
    if name!="":
        break

pincode_city="BLR_560038"

for i in pincode_city:
    if i== "_":
        # print(i,end="")
        continue # skips this iteration
    print(i,end="")
