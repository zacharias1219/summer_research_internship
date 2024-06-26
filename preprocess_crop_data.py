import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_crop_yield_data(data_path, output_path):
    # Step 1: Load the dataset
    data = pd.read_csv(data_path)
    
    # Step 2: Handle missing values (Forward fill)
    data = data.fillna(method='ffill')
    
    # Step 3: Scale the features using StandardScaler
    scaler = StandardScaler()
    data_scaled = scaler.fit_transform(data)
    
    # Convert the scaled data back to a DataFrame
    data_scaled_df = pd.DataFrame(data_scaled, columns=data.columns)
    
    # Step 4: Save the preprocessed data to a new CSV file
    data_scaled_df.to_csv(output_path, index=False)
    
    print(f"Preprocessed data saved to {output_path}")

# Paths to the input and output files
crop_yield_data_path = "./data/crop_yield/df_modifed.csv"
preprocessed_data_path = "data/crop_yield/df_modifed_preprocessed.csv"

# Preprocess the crop yield data
preprocess_crop_yield_data(crop_yield_data_path, preprocessed_data_path)
