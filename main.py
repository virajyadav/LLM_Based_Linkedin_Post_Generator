import streamlit as st
from few_short import FewShort
from post_generator import generate_post



def main():
    st.title("LinkedIn Post Generator : Rupali Sweetheart")
    fs = FewShort()
    length_options = ["Short", "Medium", "Long"]
    language_options = ["English"]
    col1 , col2 , col3 = st.columns(3)
    with col1:
        selected_tag = st.selectbox("Title", options=fs.get_unique_tags(),help="Select the title of the post")
    with col2:
        selected_length = st.selectbox("Length", options=length_options,help="Select the length of the post")
    with col3:
        selected_language = st.selectbox("Language", options=language_options,help="Select the language of the post")

    if st.button("Generate"):
        post = generate_post(selected_tag, selected_length,selected_language)
        st.write(post)




if __name__ == "__main__":
    main()