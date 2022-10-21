from src.load_packages import *

@st.cache()
def load_plant_matrix_data(path):
    df = pd.read_csv(path)
    df = df.set_index("Unnamed: 0")
    return df