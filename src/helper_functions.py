from src.load_packages import *

@st.cache()
def filter_df_by_column(df, column, filter_list):
    if len(filter_list) > 0:
        return df[df[column].isin(filter_list)]
    else:
        return df
    
@st.cache()
def filter_df_by_index(df, filter_list):
    if len(filter_list) != 0:
        return df.loc[filter_list, filter_list]
    else:
        return df

def display_plants_per_bucket(bucket_dict, n_columns):
    if n_columns >= len(bucket_dict.keys()):
        n_columns = len(bucket_dict.keys())
    
    bucket_keys_list = list(bucket_dict.keys())
    bucket_keys_array = np.array(bucket_keys_list)
    
    missing_items = bucket_keys_array.shape[0]%n_columns
    augmented_bucket_keys_array = np.append(bucket_keys_array, np.zeros((n_columns-missing_items, 1)))
    
    reshaped_bucket_key_array = np.reshape(augmented_bucket_keys_array, (int(len(augmented_bucket_keys_array)/n_columns), n_columns))
    for i, row in enumerate(reshaped_bucket_key_array):
        st.markdown("---")
        columns = st.columns(n_columns)
        for j, bucket in enumerate(row):
            plant_names = bucket_dict.get(bucket, None)
            
            if plant_names != None:
                columns[j].markdown(f"### field {i * n_columns + j + 1}")
                
                for plant in plant_names:
                    columns[j].markdown(plant)