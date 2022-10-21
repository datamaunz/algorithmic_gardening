from src.load_packages import *
from src.load_data import *
from src.plant_distribution_functions import buckets_generator
from src.helper_functions import *

def main():
        
    st.set_page_config(
        layout="wide",
        page_title="Algorithmic Gardening",
        page_icon = "🌾")
    
    st.markdown("## 🪴 Algorithmic Gardening")
    st.markdown("---")
    
    
    df = load_plant_matrix_data("data/outputs/09162022_192558.csv")
    plant_names = df.index
    
    col1, col2 = st.columns([0.8, 0.2])
    selected_plants = col1.multiselect("Select plants for ideal pairing", plant_names)
    n_columns = col2.number_input("Select maximum number of columns per row", value=8)
    
    
    filtered_df = filter_df_by_index(df, selected_plants)
    bucket_dict = buckets_generator(filtered_df)
    
    
    
            
        
    display_plants_per_bucket(bucket_dict, n_columns)
    
    
        
            
        
    
    
if __name__ == '__main__':
    main()
    

    
    
