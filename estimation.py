import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
import shap

data = pd.read_csv('insurance.csv')


# # Very Basic estimation
# def estimate(age, sex, bmi, children, smoker, region):
#     filtered_data = data[(data['age'] == age) & (data['sex'] ==sex) & (data['bmi'] == bmi) &
#                           (data['children'] == children) & (data['smoker'] == smoker) & (data['region'] == region)]
    



#     if not filtered_data.empty:

#         estimated_rate = round(filtered_data['charges'].mean(), 2)

#         return estimated_rate
#     else:
#         # If no exact match, estimate based on characteristics that are close
#         similar_data = data[(data['age'] == age) & (data['sex'] == sex) & (data['region'] == region)]
#         if not similar_data.empty:
#             estimated_rate = round(similar_data['charges'].mean(), 2)
#             return f"Estimate based on similar characteristics: {estimated_rate}"
#         else:
#             return "No matching or similar records found."
    
# age = 28
# sex = 'male'
# bmi = 25
# children = 1
# smoker = 'no'
# region = 'southwest'

# estimate = estimate(age, sex, bmi, children, smoker, region)
# print(estimate)



# Assume 'charges' is the dependent variable, and other columns are features
X = data.drop('charges', axis=1)  # Features
y = data['charges']  # Target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the preprocessing steps
numeric_features = ['age', 'bmi', 'children']
categorical_features = ['sex', 'smoker', 'region']

numeric_transformer = StandardScaler()
categorical_transformer = OneHotEncoder(drop='first')

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

# Create the pipeline with preprocessing and regression
model = Pipeline(steps=[('preprocessor', preprocessor),
                        ('regressor', LinearRegression())])

# Fit the model on the training data
model.fit(X_train, y_train)

# Make predictions on the test data
predictions = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
rmse = np.sqrt(mse)
print(f"Root Mean Squared Error: {rmse}")

# SHAP values for post-analysis
explainer = shap.Explainer(model.named_steps['regressor'])
shap_values = explainer.shap_values(preprocessor.transform(X_test))

# Summary plot of SHAP values
shap.summary_plot(shap_values, X_test, feature_names=preprocessor.get_feature_names_out())
