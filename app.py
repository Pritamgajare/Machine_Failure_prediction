# import streamlit as st
# import pandas as pd
# import pickle

# # Load trained model
# with open('trained_model.pkl', 'rb') as file:
#     model = pickle.load(file)

# # Load LabelEncoder and StandardScaler objects
# with open('preprocessing_objects.pkl', 'rb') as file:
#     label_encoder, scaler = pickle.load(file)

# # Define preprocessing function
# def preprocess_data(df):
#     test_data_id = df['id']
#     # Feature Engineering (Temperature Difference)
#     df['Temperature Difference'] = df['Air temperature [K]'] - df['Process temperature [K]']
#     # Drop 'id' and 'Product ID' columns
#     df.drop(columns=['id', 'Product ID'], inplace=True)
#     # Encoding categorical variables
#     df['Type'] = label_encoder.transform(df['Type'])
#     # Define numerical features
#     numerical_features = ['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']
#     # Scaling numerical features
#     df[numerical_features] = scaler.transform(df[numerical_features])
#     return df, test_data_id

# # Define prediction function
# def predict(data):
#     processed_data, test_data_id = preprocess_data(data)
#     predictions = model.predict(processed_data)
#     return predictions, test_data_id

# # Streamlit UI
# st.title('Machine Failure Prediction')

# uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

# if uploaded_file is not None:
#     test_data = pd.read_csv(uploaded_file)
#     predictions, test_data_id = predict(test_data)
#     predictions_df = pd.DataFrame({'id': test_data_id, 'Machine failure': predictions})
#     st.write(predictions_df)

#     # Download predictions as CSV
#     csv = predictions_df.to_csv(index=False)
#     st.download_button(label="Download Predictions CSV", data=csv, file_name='predictions.csv', mime='text/csv')


# import streamlit as st
# import pandas as pd
# import pickle
# import random

# # Load trained model
# with open('trained_model.pkl', 'rb') as file:
#     model = pickle.load(file)

# # Load LabelEncoder and StandardScaler objects
# with open('preprocessing_objects.pkl', 'rb') as file:
#     label_encoder, scaler = pickle.load(file)

# # Define preprocessing function
# def preprocess_data(df):
#     test_data_id = df['id']
#     # Feature Engineering (Temperature Difference)
#     df['Temperature Difference'] = df['Air temperature [K]'] - df['Process temperature [K]']
#     # Drop 'id' and 'Product ID' columns
#     df.drop(columns=['id', 'Product ID'], inplace=True)
#     # Encoding categorical variables
#     df['Type'] = label_encoder.transform(df['Type'])
#     # Define numerical features
#     numerical_features = ['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']
#     # Scaling numerical features
#     df[numerical_features] = scaler.transform(df[numerical_features])
#     return df, test_data_id

# # Define prediction function
# def predict(data):
#     processed_data, test_data_id = preprocess_data(data)
#     predictions = model.predict(processed_data)
#     return predictions, test_data_id

# # List of machine failure reasons
# machine_failure_reasons = [
#     "High air temperature leading to overheating of components",
#     "Fluctuations or deviations from optimal process temperature",
#     "Excessive or inconsistent rotational speed causing mechanical stress",
#     "High torque levels indicating increased resistance or load",
#     "Elevated levels of tool wear leading to decreased performance",
#     "Failure related to tool wear (TWF)",
#     "Failure related to inadequate heat dissipation (HDF)",
#     "Failure related to power supply issues (PWF)",
#     "Failure related to overload conditions (OSF)",
#     "Random failure without clear patterns or specific causes (RNF)"
# ]

# # Streamlit UI
# st.title('Machine Failure Prediction')

# uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

# if uploaded_file is not None:
#     test_data = pd.read_csv(uploaded_file)
#     predictions, test_data_id = predict(test_data)
    
#     # Randomly select failure reasons for predictions
#     failure_reasons = [random.choice(machine_failure_reasons) for _ in range(len(predictions))]
    
#     predictions_df = pd.DataFrame({'id': test_data_id, 'Machine failure': predictions, 'Failure Reason': failure_reasons})
#     st.write(predictions_df)

#     # Download predictions as CSV
#     csv = predictions_df.to_csv(index=False)
#     st.download_button(label="Download Predictions CSV", data=csv, file_name='predictions.csv', mime='text/csv')


# import streamlit as st
# import pandas as pd
# import pickle
# import random

# with open('trained_model.pkl', 'rb') as file:
#     model = pickle.load(file)

# with open('preprocessing_objects.pkl', 'rb') as file:
#     label_encoder, scaler = pickle.load(file)

# def preprocess_data(df):
#     test_data_id = df['id']
#     test_data_pid = df['Product ID']
#     df['Temperature Difference'] = df['Air temperature [K]'] - df['Process temperature [K]']
#     df.drop(columns=['id', 'Product ID'], inplace=True)

#     df['Type'] = label_encoder.transform(df['Type'])

#     numerical_features = ['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']

#     df[numerical_features] = scaler.transform(df[numerical_features])
#     return df, test_data_id, test_data_pid


# def predict(data):
#     processed_data, test_data_id, test_data_pid = preprocess_data(data)
#     df1 = processed_data
#     predictions = model.predict(processed_data)
#     return predictions, test_data_id, test_data_pid, df1


# def get_reason(row):
#     # if row['Machine failure'] == 0:
#     #     return 'No failure'
#     reasons = []
#     if row['TWF'] == 1:
#         reasons.append('Tool wear failure')
#     if row['HDF'] == 1:
#         reasons.append('Air and Process temperature is high')
#     if row['PWF'] == 1:
#         reasons.append('Occurred due to power supply problem')
#     if row['OSF'] == 1:
#         reasons.append('High rotational speed and high torque')
#     if row['RNF'] == 1:
#         reasons.append('Failed due to random reason')
#     return ', '.join(reasons)

# # Streamlit UI
# st.title('Machine Failure Prediction')

# # Heading for required columns
# st.markdown("### Required Columns in CSV File:")
# st.markdown("id, Product ID, Type, Air temperature [K], Process temperature [K], Rotational speed [rpm], Torque [Nm], Tool wear [min], TWF, HDF, PWF, OSF, RNF")

# uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

# if uploaded_file is not None:
#     test_data = pd.read_csv(uploaded_file)
#     predictions, test_data_id, test_data_pid, df1 = predict(test_data)

#     failure_reasons = ""
#     for predic in predictions:
#         if predic == 0:
#             failure_reasons.append("No Failure")
#         else:
#             failure_reasons = [get_reason(row) for index, row in df1.iterrows()]
      
#     predictions_df = pd.DataFrame({'PID':test_data_pid,'id': test_data_id, 'Machine failure': predictions, 'Failure Reason': failure_reasons})
#     st.write(predictions_df)

#     # Download predictions as CSV
#     csv = predictions_df.to_csv(index=False)
#     st.download_button(label="Download Predictions CSV", data=csv, file_name='predictions.csv', mime='text/csv')

import streamlit as st
import pandas as pd
import pickle
import random

with open('trained_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('preprocessing_objects.pkl', 'rb') as file:
    label_encoder, scaler = pickle.load(file)

def preprocess_data(df):
    test_data_id = df['id']
    test_data_pid = df['Product ID']
    df['Temperature Difference'] = df['Air temperature [K]'] - df['Process temperature [K]']
    df.drop(columns=['id', 'Product ID'], inplace=True)

    df['Type'] = label_encoder.transform(df['Type'])

    numerical_features = ['Air temperature [K]', 'Process temperature [K]', 'Rotational speed [rpm]', 'Torque [Nm]', 'Tool wear [min]']

    df[numerical_features] = scaler.transform(df[numerical_features])
    return df, test_data_id, test_data_pid


def predict(data):
    processed_data, test_data_id, test_data_pid = preprocess_data(data)
    df1 = processed_data
    predictions = model.predict(processed_data)
    return predictions, test_data_id, test_data_pid, df1

def get_reason(row):
    reasons = []
    if row['TWF'] == 1:
        reasons.append('Tool wear failure')
    if row['HDF'] == 1:
        reasons.append('Air and Process temperature is high')
    if row['PWF'] == 1:
        reasons.append('Occurred due to power supply problem')
    if row['OSF'] == 1:
        reasons.append('High rotational speed and high torque')
    if row['RNF'] == 1:
        reasons.append('Failed due to random reason')
    if len(reasons) == 0:
        reasons.append('Failed due to unavoidable circumstances.')
    return ', '.join(reasons) 


# machine_failure_reasons = [
#     "Fluctuations or deviations from optimal process temperature",
#     "Excessive or inconsistent rotational speed causing mechanical stress",
#     "High torque levels indicating increased resistance or load",
#     "Elevated levels of tool wear leading to decreased performance",
#     "Failure related to tool wear (TWF)",
#     "Failure related to inadequate heat dissipation (HDF)",
#     "Failure related to power supply issues (PWF)",
#     "Failure related to overload conditions (OSF)",
#     "Random failure without clear patterns or specific causes (RNF)"
# ]

# Streamlit UI
st.title('Machine Failure Prediction')

# Heading for required columns
st.markdown("### Required Columns in CSV File:")
st.markdown("id, Product ID, Type, Air temperature [K], Process temperature [K], Rotational speed [rpm], Torque [Nm], Tool wear [min], TWF, HDF, PWF, OSF, RNF")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    test_data = pd.read_csv(uploaded_file)
    predictions, test_data_id, test_data_pid, df1 = predict(test_data)
    failure_reasons = []
    for prediction, (_, row) in zip(predictions, df1.iterrows()):
        if prediction == 0:
            failure_reasons.append("No Failure")
        else:
            failure_reasons.append(get_reason(row))
    predictions_df = pd.DataFrame({'PID':test_data_pid, 'id': test_data_id, 'Machine failure': predictions, 'Failure Reason': failure_reasons})
    st.write(predictions_df)

    # Download predictions as CSV
    csv = predictions_df.to_csv(index=False)
    st.download_button(label="Download Predictions CSV", data=csv, file_name='predictions.csv', mime='text/csv')
