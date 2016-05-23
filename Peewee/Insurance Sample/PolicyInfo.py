import csv
from peewee import *

db = SqliteDatabase('Insurance Sample\InsuranceData.db')


#class PolicyInfo(object):
#    """description of class"""


#    def __new__(cls):
#        cls.policyID = 0,
#        cls.statecode = "",
#        cls.county = "",
#        cls.eq_site_limit = 0,
#        cls.hu_site_limit = 0,
#        cls.fl_site_limit = 0,
#        cls.fr_site_limit = 0,
#        cls.tiv_2011 = 0
#        cls.tiv_2012 = 0,
#        cls.eq_site_deductible = 0,
#        cls.hu_site_deductible = 0,
#        cls.fl_site_deductible = 0,
#        cls.fr_site_deductible = 0,
#        cls.point_latitude = 0,
#        cls.point_longitude = 0,
#        cls.line = "",
#        cls.construction = "",
#        cls.point_granularity = 0
#        return cls

class PolicyInfo(Model):
    """description of class"""

    policyID = IntegerField(),
    statecode = CharField(),
    county = CharField(),
    eq_site_limit = IntegerField(),
    hu_site_limit = IntegerField(),
    fl_site_limit = IntegerField(),
    fr_site_limit = IntegerField(),
    tiv_2011 = IntegerField()
    tiv_2012 = IntegerField(),
    eq_site_deductible = IntegerField(),
    hu_site_deductible = IntegerField(),
    fl_site_deductible = IntegerField(),
    fr_site_deductible = IntegerField(),
    point_latitude = IntegerField(),
    point_longitude = IntegerField(),
    line = CharField(),
    construction = CharField(),
    point_granularity = IntegerField()

    class Meta:
        database = db # this model uses the "people.db" database

    @staticmethod
    def ImportData():
        with open('Insurance Sample\FL_insurance_sample.csv', 'rt') as f:
            reader = csv.reader(f)
            for row in reader:
                if row[0] == 'policyID':
                    continue

                print(row)
                Policy = PolicyInfo()
                Policy.policyID = row[0]
                Policy.statecode = row[1]
                Policy.county = row[2]
                Policy.eq_site_limit = row[3]
                Policy.hu_site_limit = row[4]
                Policy.fl_site_limit = row[5]
                Policy.fr_site_limit = row[6]
                Policy.tiv_2011 = row[7]
                Policy.tiv_2012 = row[8]
                Policy.eq_site_deductible = row[9]
                Policy.hu_site_deductible = row[10]
                Policy.fl_site_deductible = row[11]
                Policy.fr_site_deductible = row[12]
                Policy.point_latitude = row[13]
                Policy.point_longitude = row[14]
                Policy.line = row[15]
                Policy.construction = row[16]
                Policy.point_granularity = row[17]
                #Policies.append(Policy)
                Policy.save()



PolicyInfo.ImportData()