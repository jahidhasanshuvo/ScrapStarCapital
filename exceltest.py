import pandas as pd
from connection import Connection
from models import StarCapitalScrapeUld


conn = Connection()

session = conn.session
objects = []
df = pd.read_excel('demo_starcapital_output_2020-01-17-12-09-23.xlsx')
# data = df[0:1].to_dict('r')[0]
# print(data['RS 52W'])
df = df.fillna(0)
for index, row in df.iterrows():
    objects.append(StarCapitalScrapeUld(row.to_dict()))
print(objects[0])
session.bulk_save_objects(objects)
session.commit()