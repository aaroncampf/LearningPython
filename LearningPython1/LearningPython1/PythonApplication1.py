class Contact(object):
    pass

class Company(object):
    """Represents a company"""
    Name = ""
    Address=""
    City=""
    State=""
    Zip=""
    Phone=""
    Email=""
    Contacts = [Contact]

    def __new__(cls):
        cls.Contacts.clear()
        return cls

AJP = Company()
AJP.Contacts

print(len(AJP.Contacts))
