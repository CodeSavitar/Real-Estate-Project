import pandas as pd
from sklearn.tree import DecisionTreeRegressor
import pickle

df = pd.read_csv(r"C:\Users\adhit\OneDrive\Desktop\sample\New folder\Python-Flask-Real-Estate-Web-Application-master\Python-Flask-Real-Estate-Web-Application-master\RealEstate-Flask\land1.csv")
cdf =df[['Price','Size','Cost','Appreciation Value']]
x = cdf.iloc[:, :3]
y = cdf.iloc[:, -1]

dtr = DecisionTreeRegressor()
dtr.fit(x,y)

pickle.dump(dtr, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
