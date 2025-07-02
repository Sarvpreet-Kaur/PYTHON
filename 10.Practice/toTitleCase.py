def toTitle(fname,lname):
    """ This function is user defined function
    to take first name and last name and output
    the title case and concatenation of fname
    and lname"""
    name = ""
    for ch in fname:
        if ch==fname[0]:
            name += ch.upper()
        else:
            name+= ch.lower()
    name += " "
    for ch in lname:
        if ch==lname[0]:
            name += ch.upper()
        else:
            name+= ch.lower()
    return name
#fname.title()
name = toTitle("rEEt", "KaUr")
print(name)
print("reet".title())