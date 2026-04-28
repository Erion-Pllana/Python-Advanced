import streamlit as st

tab1,tab2,tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])

with tab1:
    st.header("This is Tab 1 header")
    st.write("This is a text of Tab 1")

with tab2:
    st.header("This is Tab 2 header")
    st.write("This is a text of Tab 2")

with tab3:
    st.header("This is Tab 3 header")
    st.write("This is a text of Tab 3")