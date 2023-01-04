from sklearn.model_selection import train_test_split
import matplotlib.pyplot as mtp
from sklearn.linear_model import LinearRegression
import pandas as pd
# import linear_model
data = pd.read_csv('data.csv')
x = data.iloc[:, 1]
y = data.iloc[:, 2]

print(x, y)

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=(1/3), random_state=0)

mtp.scatter(x_train, y_train)
mtp.title("Training Data Plot")
mtp.xlabel('A')
mtp.ylabel('B')
mtp.plot()
mtp.show()

mtp.scatter(x_test, y_test)
mtp.title("Testing Data Plot")
mtp.xlabel('A')
mtp.ylabel('B')
mtp.plot()
mtp.show()

mtp.scatter(x_test, y_test)
mtp.scatter(x_train, y_train)
mtp.title("Train & Test Data plot")
mtp.xlabel('x')
mtp.ylabel('y')
mtp.plot()
mtp.show()

reg = LinearRegression()
reg.fit(x_train, y_train)
reg.predict(x_test)

