import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(page_title='Multi-Tool App', layout='centered')

st.title("Choose an Option")

options = {
    "📝 Form": "form",
    "📄 CSV Uploader": "csv",
    "🖼️ Image Gallery": "gallery"
}

cols = st.columns(3)

for i, (label, key) in enumerate(options.items()):
    with cols[i]:
        if st.button(label):
            st.session_state['selected'] = key

selected = st.session_state.get("selected", None)    

if selected == 'form':
    with st.form("user_info_form"):
        name = st.text_input("", placeholder='Name')
        age = st.text_input("", placeholder="Age")
        feedback = st.text_input("", placeholder="Your feedback")

        gender = st.radio("Gender", ["Male", "Female"], horizontal=True)

        workDays = st.slider("How many days you work in a week?", 0, 7, 5)

        agree = st.checkbox("I agree to the Terms and Conditions")
        
        submitted = st.form_submit_button("Submit")

    if submitted:
        if not agree:
            st.error("You must agree to the Terms and Conditions to proceed.")
        else:
            st.success("Form Submitted Successfully!")
            st.subheader("📋 Submitted Information")
            st.write(f"**Name:** {name}")
            st.write(f"**Age:** {age}")
            st.write(f"**Gender:** {gender}")
            st.write(f"**Work Days per Week:** {workDays}")
            st.write(f"**Feedback:** {feedback}")
    
if selected == 'csv':
    st.header("📄 CSV Uploader")

    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.subheader("📊 Data Table")

        search_term = st.text_input("Search", "")

        if search_term:
            df_filtered = df[df.astype(str).apply(lambda row: row.str.contains(search_term, case=False)).any(axis=1)]
        else:
            df_filtered = df.copy()

        sort_col = st.selectbox("Sort by column", df_filtered.columns)
        sort_order = st.radio("Order", ["Ascending", "Descending"], horizontal=True)
        df_filtered = df_filtered.sort_values(by=sort_col, ascending=(sort_order == "Ascending"))

        page_size = st.slider("Rows per page", min_value=5, max_value=50, value=10, step=5)
        total_rows = len(df_filtered)
        total_pages = (total_rows - 1) // page_size + 1
        page_num = st.number_input("Page", min_value=1, max_value=total_pages, value=1, step=1)

        start_idx = (page_num - 1) * page_size
        end_idx = start_idx + page_size
        paginated_df = df_filtered.iloc[start_idx:end_idx]

        st.dataframe(paginated_df, use_container_width=True)

if selected == 'gallery':
    st.header("🖼️ Image Gallery")

    uploaded_images = st.file_uploader(
        "Upload one or more images", type=["jpg", "jpeg", "png"], accept_multiple_files=True
    )

    if uploaded_images:
        st.subheader("🖼️ Thumbnails")

        # Show thumbnails
        thumb_cols = st.columns(len(uploaded_images))
        for i, image_file in enumerate(uploaded_images):
            with thumb_cols[i]:
                image = Image.open(image_file)
                st.image(image, use_column_width=True, caption=f"Image {i+1}")

        # Select image to preview
        selected_index = st.selectbox(
            "Select an image to view larger",
            options=list(range(len(uploaded_images))),
            format_func=lambda x: f"Image {x+1}",
        )

        selected_image = Image.open(uploaded_images[selected_index])
        st.image(selected_image, caption=f"Image {selected_index + 1}", use_column_width=True)