from src.load_packages import *

def add_bucket(bucketdict, plants_dict): 
    # Creates a new bucket + fills it with element 0:
    """Creates a new bucket + fills it with element 0"""

    n=len(bucketdict.keys())+1
    
    # Adds a new bucket key + initial fill:
    bucketdict[f"bucket_{n}"] = [list(plants_dict.keys())[n-1]]


def safety_check(df, plant,bucket_plants_list):
    # Checks if a plant is harmful to other plants in the bucket or harmed by other plants in bucket (Returns True if harm is detected)
    '''This method checks if the plants are safe with/for other plants in the bucket'''
    for looper in bucket_plants_list:
        if df.loc[plant][looper] == -1 or df.loc[looper][plant] == -1:
          
            return False
    return True
    

def add_items(df, bucket_plants_list, plants_dict):
    '''This method fills the buckets with plants under the conditions that none of the plants to be added have negative effect with other ones in the bucket & do not already exist in the bucket they're being added to'''
    
    # Method call example: bucketdict['bucket_1']
    current_plant = bucket_plants_list[-1]
    
    # Loops through the plants in the helping list of current plant (in plants_dict):
    for plant in plants_dict[current_plant][0]:
        
        # If current_plant does not harm the looping plant and looping plant is not in list: 
        if safety_check(df, plant,bucket_plants_list) and plant not in bucket_plants_list:
            bucket_plants_list.append(plant)
                    #print (current_plant,plant)
            add_items(df, bucket_plants_list, plants_dict)
            
    #print(bucket_plants_list)
    return bucket_plants_list


@st.cache()
def buckets_generator(df):
    bucketdict={}
    plants_dict={}
    filtered_pos = []
    filtered_neg = []
    
    # Creates plants dictionary holding helping & avoid lists with plant names as keys:
    for plant in df.index:
        plants_dict[plant]=[[],[]]
    
    for index, row in df.iterrows():
    
        frame = pd.DataFrame(row)
        frame = frame[frame[index] == 1]
        for col in frame.columns:
            temp_list=list(frame.index)
            if len(temp_list)>0:
                filtered_pos.append([col,temp_list])
                plants_dict[col][0]=temp_list
    
        frame = pd.DataFrame(row)

        frame = frame[frame[index] == -1]    
    for col in frame.columns:
        temp_list=list(frame.index)
        if len(temp_list)>0:
            filtered_neg.append([col,temp_list])
            plants_dict[col][-1]=temp_list
            
    for plant in plants_dict:
        if len(bucketdict.keys())<len(plants_dict.keys()):
            add_bucket(bucketdict,plants_dict)
    
    for key in bucketdict.keys():
        bucketdict[key]=add_items(df, bucketdict[key],plants_dict)
    return bucketdict