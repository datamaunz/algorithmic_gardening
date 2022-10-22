from src.load_packages import *
from src.load_data import *
from src.plant_distribution_functions import buckets_generator
from src.helper_functions import *
from src.explanatory_texts import *
 


def main():
        
    st.set_page_config(
        layout="wide",
        page_title="Algorithmic Gardening",
        page_icon = "🌾")
    
    st.markdown("## 🪴 Algorithmic Gardening")
    
    df = load_plant_matrix_data("data/outputs/09162022_192558.csv")
    plant_names = df.index
    
    display_text_segment_for_general_idea(len(plant_names))
    
    
    #col1, col2 = st.columns([0.8, 0.2])
    selected_plants = st.sidebar.multiselect("Select plants for ideal pairing", plant_names)
    n_columns = st.sidebar.number_input("Select maximum number of columns per row", value=4)
    
    
    filtered_df = filter_df_by_index(df, selected_plants)
    bucket_dict = buckets_generator(filtered_df)
    
    display_network_graph_per_bucket(filtered_df, bucket_dict, n_columns)
    
    
    
    
        
            
        
    
    
if __name__ == '__main__':
    main()
    

    
    
