import streamlit as st

def main():
        
    st.set_page_config(
        layout="wide",
        page_title="Algorithmic Gardening",
        page_icon = "🪴")
    
    st.markdown("## 🪴 Algorithmic Gardening")
    
    text = st.sidebar.text_input("Write Something")
    
    st.markdown(text)
    
    
    
if __name__ == '__main__':
    main()
    

    
    
