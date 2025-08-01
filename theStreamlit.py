import streamlit as st

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