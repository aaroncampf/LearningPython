import csv
from PolicyInfo import *

Samples = []
Samples.append(PolicyInfo())


with open('data\FL_insurance_sample.csv', 'rt') as f:
    reader = csv.reader(f)
    for row in reader:
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

