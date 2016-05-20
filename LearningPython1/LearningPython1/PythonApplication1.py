import csv


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


Companies = (
    Company(),
    Company()
)




with open('eggs.csv', 'wt') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ', quotechar=',', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(["Name", "Address", "City", "State", "Zip", "Phone", "Email"])
    spamwriter.writerow([Companies[0]])
    
    #spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    #spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])