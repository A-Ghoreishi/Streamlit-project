# Streamlit Multi-Tool App

This Streamlit application provides users with three distinct interactive tools accessible from a simple option menu:

---

## Features

### 1. 📝 User Information Form
- A user-friendly form wrapped in an `st.form` context for proper submission handling.
- Input fields:
  - Name (text input with placeholder)
  - Age (text input with placeholder)
  - Feedback (text input with placeholder)
  - Gender selection via radio buttons (Male/Female)
  - Workdays per week (slider from 0 to 7)
  - Terms and Conditions agreement (checkbox)
- Form submission button validates that the user has agreed to terms.
- Upon successful submission, displays all entered information clearly on the same page.

---

### 2. 📄 CSV Uploader and Data Table Viewer
- File uploader accepts CSV files.
- Once a CSV is uploaded, the data is displayed as a table with:
  - **Search functionality:** Filters rows based on a case-insensitive search term applied across all columns.
  - **Sortable columns:** User can select which column to sort by, and choose ascending or descending order.
  - **Pagination:** Controls for rows per page (slider from 5 to 50) and page navigation via a number input.
- Displays only the filtered and paginated subset of data in a scrollable table.

---

### 3. 🖼️ Image Gallery
- Allows uploading multiple image files (`jpg`, `jpeg`, `png`).
- Displays small thumbnail previews of all uploaded images in a horizontal row.
- Provides a dropdown (`selectbox`) to select an image to view in a larger format below the thumbnails.
- Images are displayed with captions indicating their index in the gallery.

---

## Technical Details

- The app uses Streamlit's session state to maintain the selected tool across reruns.
- `st.set_page_config` is set for a centered layout and custom page title.
- Uses Pandas for CSV reading and data filtering/sorting.
- Uses Pillow (`PIL.Image`) to open and display images.
- Proper use of Streamlit components ensures a smooth, interactive user experience.

---

## Usage

1. Run the app with:
   ```bash
   streamlit run your_script.py
