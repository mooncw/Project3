import json
import pickle

data = None

with open('metabase.json','r') as json_file:
    data = json.load(json_file)

    
model = None

with open('model.pkl','rb') as pickle_model:
    model = pickle.load(pickle_model)

import sqlite3

conn = sqlite3.connect("metabase.db")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS testset;")

cur.execute("""CREATE TABLE testset(
                age INTEGER,
                gender INTEGER,
                height INTEGER,
                weight REAL,
                ap_hi INTEGER,
                ap_lo INTEGER,
                cholesterol INTEGER,
                gluc INTEGER,
                smoke INTEGER,
                alco INTEGER,
                active INTEGER,
                cardio INTEGER,
                proba REAL);
""")

for i in range(len(data)):
    v = list(data[i].keys())
    v.append('proba')
    x = list(data[i].values())
    r = x.pop()
    mx = [x]
    proba = round(model.predict_proba(mx)[0][1],2)
    x.append(r)
    x.append(proba)
    x[0]=int(x[0]/365)
    cur.execute(f"INSERT INTO testset {tuple(v)} VALUES {tuple(x)};")

conn.commit()

cur.close()
conn.close()