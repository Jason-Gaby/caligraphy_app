import pandas as pd


class Address:
    def __init__(self, address1=None, address2=None, city=None, state=None, zip_code=None):
        self.address1 = address1
        self.address2 = address2
        self.city = city
        self.state = state
        self.zip = zip_code


def get_addresses(file):
    excel = pd.read_excel(file, dtype=str)
    for col in excel.columns:
        excel.loc[excel[col].apply(type) != type("str"), col] = ""
    addresses = excel.apply(create_addresses, axis=1)
    return addresses.tolist()


def create_addresses(row):
    address1 = row["Address 1"]
    address2 = row["Address 2"]
    city = row["City"]
    state = row["State"]
    zip_code = row["Zip Code"]
    return Address(address1, address2, city, state, zip_code)

