import csv
from peewee import *
from builtins import staticmethod



db = SqliteDatabase('Insurance Sample\InsuranceData.db')

class PolicyInfo(Model):
    """description of class"""

    policyID = IntegerField()
    statecode = CharField()
    county = CharField()
    eq_site_limit = FloatField()
    hu_site_limit = FloatField()
    fl_site_limit = FloatField()
    fr_site_limit = FloatField()
    tiv_2011 = FloatField()
    tiv_2012 = FloatField()
    eq_site_deductible = FloatField()
    hu_site_deductible = FloatField()
    fl_site_deductible = FloatField()
    fr_site_deductible = FloatField()
    point_latitude = FloatField()
    point_longitude = FloatField()
    line = CharField()
    construction = CharField()
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

#db.create_tables([PolicyInfo])
#PolicyInfo.ImportData()

Test = PolicyInfo()
Test = PolicyInfo.select().first()

print(Test)