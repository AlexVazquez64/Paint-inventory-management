import pandas as pd
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv('paint_sales_data.csv')

# Split data into training and testing sets
train_data = data.sample(frac=0.8, random_state=1)
test_data = data.drop(train_data.index)

# Train linear regression model to predict demand
model = LinearRegression()
model.fit(train_data[['month', 'year']], train_data['sales'])

# Use model to predict demand for next month
next_month = pd.DataFrame({'month': [13], 'year': [2023]})
predicted_demand = model.predict(next_month)

# Calculate optimal restocking schedule
inventory_level = 500
order_size = 1000
lead_time = 30
reorder_point = predicted_demand * lead_time + inventory_level
if reorder_point > inventory_level:
    order_quantity = order_size
else:
    order_quantity = 0

# Print results
print('Predicted demand for next month:', predicted_demand[0])
print('Reorder point:', reorder_point[0])
print('Order quantity:', order_quantity)
