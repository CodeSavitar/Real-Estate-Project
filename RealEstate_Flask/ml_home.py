import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle

df = pd.read_csv(r"C:\Users\Aadhi\Desktop\sample\New folder\Python-Flask-Real-Estate-Web-Application-master\Python-Flask-Real-Estate-Web-Application-master\RealEstate-Flask\buyhome1.csv")
cdf =df[['Bed','Bath','Price','Number','Appreciation Value']]

x = cdf.iloc[:, :4]
y = cdf.iloc[:, -1]

rfr = RandomForestRegressor(n_estimators = 10)
rfr.fit(x,y)

pickle.dump(rfr, open('model1.pkl','wb'))
model = pickle.load(open('model1.pkl','rb'))
#df = df.reset_index()
