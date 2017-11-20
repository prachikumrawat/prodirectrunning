import re
import csv

class Restrictions(object):
    def __init__(self, sku_suffix):
        self.sku_suffix = sku_suffix
        self.file_path = "utilities/bin/restricted/Restricted_Brands.csv"

    def parse_restrictions(self, product_dict):
        for restrictions in Restrictions.__dict__.values():
            print restrictions
            function_name = str(restrictions).split('function ')[-1].split(' ')[0]
            if callable(restrictions) and function_name not in ['__init__', 'parse_restrictions']:
                restriction_bool, reason = restrictions(self, product_dict)
                if restriction_bool:
                    return restriction_bool, reason
        else:
            return False, None

    def parse_brands(self, product_dict):
        restricted_file_path = self.file_path
        brand_name = product_dict['brand_name']

        with open(restricted_file_path, 'r') as restricted_brands_file:
            for row in csv.reader(restricted_brands_file):
                brand = row[0].strip()
                if brand:
                    restricted_brand = re.findall('\\b'+brand+'\\b', brand_name, flags=re.IGNORECASE)
                    if restricted_brand:
                        return True, "Restricted Brands {}".format(brand)

        return False, None
