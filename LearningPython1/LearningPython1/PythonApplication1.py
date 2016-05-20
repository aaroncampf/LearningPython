import csv


class Contact(object):
    pass

class Company(object):
    """Represents a company"""

    def __new__(cls):
        cls.Name = ""
        cls.Address = ""
        cls.City = ""
        cls.State = ""
        cls.Zip = ""
        cls.Phone = ""
        cls.Email = ""
        cls.Contacts = [Contact]
        return cls


AJP = Company()
AJP.Name = "AJP Northwest"

Companies = []
Companies.append(AJP)

with open('names.csv', 'wt') as csvfile:
    fieldnames = ["Name", "Address", "City", "State", "Zip", "Phone", "Email"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for x in Companies:
        writer.writerow({"Name": x.Name, "Address": x.Address, "City": x.City, "State": x.State, "Zip": x.Zip, "Phone": x.Phone, "Email": x.Email})
