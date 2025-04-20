import pandas as pd

def load_data(uploaded_file):
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            return df
        except Exception as e:
            print(f"Error loading file: {e}")
            return None
    else:
        return None