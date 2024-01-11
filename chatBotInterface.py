import streamlit as st
from PIL import Image

# Function to display an image
def load_and_display_image(path, width):
    image = Image.open(path)
    st.image(image, width=width, use_column_width=False)

# Set page configuration
st.set_page_config(layout="wide")

# Initialize session state for navigation
if 'started' not in st.session_state:
    st.session_state['started'] = False

# Define the homepage layout
def homepage():
    col1, col2 = st.columns([1, 7])

    with col1:
        load_and_display_image('/Users/likai/Desktop/trans.png', width=115)

    with col2:
        st.markdown("<h2 style='margin-top:20px;'>Document Compliance Checker</h2>", unsafe_allow_html=True)

    # User Login Section
    left, mid, right = st.columns([3, 2, 1])
    with left:
        st.write("## User Login")
        username = st.text_input("Username", key="username", label_visibility="collapsed")
        password = st.text_input("Password", key="password", type="password", label_visibility="collapsed")
        if st.button("Login", key="login"):
            st.info("Login functionality not implemented.")

    # Button to continue without signing in
    if st.button('Get Started without signing in', key='start_button',
                 on_click=lambda: setattr(st.session_state, 'started', True)):
        pass

    # Sidebar with information about the tool
    st.sidebar.title("Learn about this tool")
    st.sidebar.markdown(
        "<p style='color: grey;'>We are making a tool which automatically generates an in-depth compliance report "
        "explaining how well a company complies with its chosen regulation/standards.</p>",
        unsafe_allow_html=True)
    st.sidebar.markdown(
        "<p style='color: grey;'>All the user has to do (all via our website) is submit their input documents "
        "(including company policies, carbon emissions, client surveys etc.), and a copy of the standard they are "
        "complying with(e.g. DeTAC, FCA etc.).</p>",
        unsafe_allow_html=True)

# Define the main application layout
def main_application():
    # Back button
    if st.button('<', key='backwards-button'):
        st.session_state.started = False

    st.title("Document Compliance Checker")
    st.markdown("<p style='color: grey;'>To check if your documents comply with the latest regulations and standards here.</p>", unsafe_allow_html=True)

    # Sidebar for settings
    st.sidebar.header("Settings")
    st.sidebar.info("Configure your analysis settings here.")

    # Standards selection in the sidebar
    st.sidebar.subheader("Standards Selection")
    standards_list = ["DeTAC", "FCA", "ISO 9001", "ISO 27001", "GDPR", "HIPAA", "Other - Upload Below"]
    selected_standard = st.sidebar.selectbox("Choose a Standard", standards_list)

    # Upload custom standard
    st.sidebar.subheader("Upload Custom Standard")
    uploaded_standard = st.sidebar.file_uploader("Upload a Standard File", type=['txt', 'pdf'])

    # Application tabs
    tab1, tab2 = st.tabs(["Text Input", "File Upload"])

    # Text Input Tab
    with tab1:
        st.subheader("Text Input")
        text_input = st.text_area("Enter or paste your text here:", height=300, placeholder="Paste your text here...",
                                  label_visibility="collapsed")
        if st.button("Analyze Text"):
            with st.spinner("Analyzing..."):
                result = handle_text_input(text_input)
                st.success(result)

    # File Upload Tab
    with tab2:
        st.subheader("File Upload")
        st.write("Supported formats: .txt, .docx, .pdf")
        uploaded_file = st.file_uploader("", type=['txt', 'docx', 'pdf'], label_visibility="collapsed")
        if uploaded_file is not None:
            with st.spinner("Processing File..."):
                file_result = handle_file_upload(uploaded_file)
                st.success(file_result)

        # Report Generation
        if st.button("Generate Report"):
            with st.spinner("Generating Report..."):
                embed_input_files()
                embedd_standard(os.path.join("standard_docs", "dummy_regulation.txt"))
                categorisation_and_coverage()
                st.success("Report Generated. Check your email or designated output location.")

    # Footer
    st.markdown("---")
    st.markdown("Developed by [UCL and CarefulAI Ltd](www.carefulai.com)")

    # Sidebar - Help & Documentation
    st.sidebar.markdown("## Help & Documentation")
    st.sidebar.markdown("Find more information about how to use this tool [here](Documentation-Link).")


# Display the homepage or the main application based on session state
if not st.session_state.get('started'):
    homepage()
else:
    main_application()

# import streamlit as st
# from PIL import Image
#
#
# def load_and_display_image(path, width):
#     image = Image.open(path)
#     st.image(image, width=width, use_column_width=False)
#
# st.set_page_config(layout="wide")
#
# col1, col2 = st.columns([1, 7])
#
# # Initialize session state for navigation
# if 'started' not in st.session_state:
#     st.session_state['started'] = False
#
# # Homepage
# if not st.session_state.get('started'):
#     with col1:
#         logo = Image.open('/Users/likai/Desktop/trans.png')
#         st.image(logo, width=115)
#
#     with col2:
#         st.markdown("<h2 style='margin-top:20px;'>Document Compliance Checker</h2>", unsafe_allow_html=True)
#
#     left, mid, right = st.columns([3, 2, 1])
#     with left:
#         st.write("## User Login")  # Title for the login section
#         username = st.text_input("Username", key="username")
#         password = st.text_input("Password", key="password", type="password")
#
#         if st.button("Login", key="login"):
#             st.info("Login functionality not implemented.")
#
#     # Customized button
#     if st.button('Get Started without signing in', key='start_button', on_click=lambda: setattr(st.session_state, 'started', True)):
#         pass
#
#     st.sidebar.title("Learn about this tool")
#     st.sidebar.markdown(
#         "<p style='color: grey;'>We are making a tool which automatically generates an in-depth compliance report "
#         "explaining how well a company complies with its chosen regulation/standards.</p>",
#         unsafe_allow_html=True)
#     st.sidebar.markdown(
#         "<p style='color: grey;'>All the user has to do (all via our website) is submit their input documents "
#         "(including company policies, carbon emissions, client surveys etc.), and a copy of the standard they are "
#         "complying with(e.g. DeTAC, FCA etc.).</p>",
#         unsafe_allow_html=True)
#
# # Main application after clicking Get Started
# else:
#     if st.button('<', key='backwards-button', on_click=lambda: setattr(st.session_state, 'started', False)):
#         pass
#
#     st.title("Document Compliance Checker")
#     st.markdown(
#         "<p style='color: grey;'>To check if your documents comply with the latest regulations and standards here.</p>",
#         unsafe_allow_html=True)
#
#     # Sidebar for settings
#     st.sidebar.header("Settings")
#     st.sidebar.info("Configure your analysis settings here.")
#
#     # Standards selection
#     st.sidebar.subheader("Standards Selection")
#     standards_list = ["DeTAC", "FCA", "ISO 9001", "ISO 27001", "GDPR", "HIPAA", "Other - Upload Below"]
#     selected_standard = st.sidebar.selectbox("Choose a Standard", standards_list)
#
#     # Upload custom standard
#     st.sidebar.subheader("Upload Custom Standard")
#     uploaded_standard = st.sidebar.file_uploader("Upload a Standard File", type=['txt', 'pdf'])
#
#     # Main application tabs
#     tab1, tab2 = st.tabs(["Text Input", "File Upload"])
#
#     # Tab for Text Input
#     with tab1:
#         st.subheader("Text Input")
#         text_input = st.text_area("Enter or paste your text here:", height=300, placeholder="Paste your text here...")
#
#         if st.button("Analyze Text"):
#             with st.spinner("Analyzing..."):
#                 result = handle_text_input(text_input)
#                 st.success(result)
#
#     # Tab for File Upload
#     with tab2:
#         st.subheader("File Upload")
#         st.write("Supported formats: .txt, .docx, .pdf")
#         uploaded_file = st.file_uploader("", type=['txt', 'docx', 'pdf'])
#
#         if uploaded_file is not None:
#             with st.spinner("Processing File..."):
#                 file_result = handle_file_upload(uploaded_file)
#                 st.success(file_result)
#
#         # Report Generation
#         if st.button("Generate Report"):
#             with st.spinner("Generating Report..."):
#                 embed_input_files()
#                 embedd_standard(os.path.join("standard_docs", "dummy_regulation.txt"))
#                 categorisation_and_coverage()
#                 st.success("Report Generated. Check your email or designated output location.")
#
#     # Footer
#     st.markdown("---")
#     st.markdown("Developed by [UCL and CarefulAI Ltd](www.carefulai.com)")
#
#     # Sidebar - Help & Documentation
#     st.sidebar.markdown("## Help & Documentation")
#     st.sidebar.markdown("Find more information about how to use this tool [here](Documentation-Link).")
#
