class PolicyInfo(object):
    """description of class"""


    def __new__(cls):
        cls.policyID = 0,
        cls.statecode = "",
        cls.county = "",
        cls.eq_site_limit = 0,
        cls.hu_site_limit = 0,
        cls.fl_site_limit = 0,
        cls.fr_site_limit = 0,
        cls.tiv_2011 = 0
        cls.tiv_2012 = 0,
        cls.eq_site_deductible = 0,
        cls.hu_site_deductible = 0,
        cls.fl_site_deductible = 0,
        cls.fr_site_deductible = 0,
        cls.point_latitude = 0,
        cls.point_longitude = 0,
        cls.line = "",
        cls.construction = "",
        cls.point_granularity = 0
        return cls