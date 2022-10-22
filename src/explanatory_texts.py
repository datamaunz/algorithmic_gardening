from src.load_packages import *


    
def display_text_segment_for_general_idea(n_of_plants):
    
    paragraph_1 = f"Plant species can have positive or negative effects on each other when planted together. To facilitate optimal\
    plant selection, we scraped data about these relationships from [Wikipedia](https://en.wikipedia.org/wiki/List_of_companion_plants),\
        cleaned it, and compiled it to give you gardening ideas about the most beneficial combinations. Currently our collection comprises {n_of_plants} plant species.\
            By improving the data cleaning process, we will add more over time."
    paragraph_2 = "Pick your species of interest on the sidebar. No selection will show the combinations for all available species. Enjoy!"
    paragraph_3 = "Read the direction of an arrow from `A` to `B` as `A is beneficial for B`."
    st.markdown(paragraph_1)
    st.info(paragraph_2)
    st.markdown(paragraph_3)
    