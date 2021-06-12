def defang(Ip_address):
    split_address=Ip_address.split(".")
    seperator="[.]"
    new_address=seperator.join(split_address)
    return new_address
print(defang("1.2.4.5.anil"))
