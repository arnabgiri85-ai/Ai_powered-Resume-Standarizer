from dotenv import load_dotenv
import streamlit as st, os, tempfile
from google import genai
import fitz  # PyMuPDF
from io import BytesIO
from docx import Document
import re, all_functions as func, shutil, time
from zipfile import ZipFile
from PIL import Image
from google.api_core.exceptions import InvalidArgument

# Load environment variables
load_dotenv()

# Set page configuration
st.set_page_config(page_title="Resume Standardization System", layout="centered")
st.title("📄 Resume Standardization System")

# Initialize session state for trial mode
if "trial_uses" not in st.session_state:
    st.session_state.trial_uses = 0

# Sidebar for API access selection
st.sidebar.subheader("🔐 API Access")
mode = st.sidebar.radio("Choose Access Mode:", ["Use My API Key", "Trial Mode (1 time only)"])

# API key management
api_key = None
client = None

if mode == "Use My API Key":
    api_key = st.sidebar.text_input("Enter your Gemini API key:", type="password")
    if api_key:
        client = genai.Client(api_key=api_key)
    else:
        st.warning("Please enter your API key to proceed.")
elif mode == "Trial Mode (1 time only)":
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        st.error("Trial API key not configured in environment.")
    elif st.session_state.trial_uses >= 1:
        st.error("Trial limit reached. Please use your own API key.")
        api_key = None
    else:
        st.sidebar.success(f"Trial use {st.session_state.trial_uses + 1} of 1")
        client = genai.Client(api_key=api_key)

# Stop execution if no valid API key
if not api_key:
    st.stop()

# ========== IMAGE RESUME PARSER ==========
def image_processing_genai(uploaded_file):
    try:
        image = Image.open(uploaded_file)
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[image, """You are a resume analyzer. Extract A to Z details from the resume image and format them as text. 
            Return a summary that includes personal info, skills, education, experience, certifications, and any relevant projects."""]
        )
        return response.text if response and response.text else "No response received from Gemini."
    except Exception as e:
        st.error(f"Error processing image with Gemini: {e}")
        return ""

# ========== FILE UPLOAD ==========
def file_upload():
    uploaded_files = st.file_uploader("Upload your resumes (PDF, DOCX, JPG, PNG)...", 
                                      type=["pdf", "docx", "jpg", "jpeg", "png"], 
                                      accept_multiple_files=True)
    return uploaded_files if uploaded_files else None

# ========== TEMPLATE PROCESSORS ==========
def process_resume(uploaded_file, filename):
    try:
        if uploaded_file.type == "application/pdf":
            resume_text = func.extract_text_from_pdf(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            resume_text = func.extract_text_from_docx(uploaded_file)
        elif uploaded_file.type in ["image/jpeg", "image/png"]:
            resume_text = image_processing_genai(uploaded_file)
        else:
            st.error("Unsupported file format.")
            return

        name = func.get_name_response(resume_text)
        education = func.get_education_details_overall(resume_text)
        degree_details = func.get_degree_details_response(education)
        education_details = func.get_education_details_response(education)
        education_years = func.get_education_years_response(education)
        summary = func.get_summary_response(resume_text)
        certifications = func.get_certifications_response(resume_text)
        skills = func.get_technical_skills_response2(resume_text)
        work_experience = func.get_work_experience_response(resume_text)

        template_path = 'Templates/Kasukabe_template.docx'
        output_path = f'agilisium_resume_internal_template/{filename}_resume.docx'

        func.fill_invitation(template_path, output_path, name, summary, certifications)
        func.fill_table_degree_details(output_path, output_path, degree_details)
        func.fill_table_institute_details(output_path, output_path, education_details)
        func.fill_table_education_years(output_path, output_path, education_years)
        func.fill_table_skill_set(output_path, output_path, skills)
        func.replace_organization_count(output_path, output_path, work_experience)

        updated_doc = func.replace_hyphens_with_bullet_points(output_path)
        updated_doc.save(output_path)
        func.remove_characters_from_docx2(output_path)
        updated_doc1 = func.replace_symbol_with_dash(output_path)
        updated_doc1.save(output_path)
        time.sleep(2)
        func.process_docx11(output_path)
        func.delete_rows_with_any_empty_cells(output_path)

        st.success(f"{filename} processed successfully.")
    except FileNotFoundError as e:
        st.error(str(e))

def process_resume_2(uploaded_file, filename):
    try:
        if uploaded_file.type == "application/pdf":
            resume_text = func.extract_text_from_pdf(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            resume_text = func.extract_text_from_docx(uploaded_file)
        elif uploaded_file.type in ["image/jpeg", "image/png"]:
            resume_text = image_processing_genai(uploaded_file)
        else:
            st.error("Unsupported file format.")
            return

        summary = func.get_summary_response(resume_text)
        project_experience = func.relevant_project_experience(resume_text)
        skills = func.get_technical_skills_response2(resume_text)
        certifications = func.get_certifications_response(resume_text)
        template_path = 'Templates/Client sample format.docx'
        output_path = f'agilisium_resume_client_format/{filename}_resume.docx'

        func.fill_invitation2(template_path, output_path, summary, skills, project_experience, certifications, "Summary Placeholder")
        education = func.get_education_details_overall(resume_text)
        func.fill_table_degree_details(output_path, output_path, func.get_degree_details_response(education))
        func.fill_table_institute_details(output_path, output_path, func.get_education_details_response(education))
        func.fill_table_education_years(output_path, output_path, func.get_education_years_response(education))

        updated_doc = func.replace_hyphens_with_bullet_points(output_path)
        updated_doc.save(output_path)
        time.sleep(2)
        func.process_docx11(output_path)
        func.delete_rows_with_any_empty_cells(output_path)
        func.remove_characters_from_docx2(output_path)

        st.success(f"{filename} processed successfully.")
    except FileNotFoundError as e:
        st.error(str(e))

def process_resume_3(uploaded_file, filename):
    try:
        if uploaded_file.type == "application/pdf":
            resume_text = func.extract_text_from_pdf(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            resume_text = func.extract_text_from_docx(uploaded_file)
        elif uploaded_file.type in ["image/jpeg", "image/png"]:
            resume_text = image_processing_genai(uploaded_file)
        else:
            st.error("Unsupported file format.")
            return

        name = func.get_name_response(resume_text)
        summary = func.get_summary_response(resume_text)
        skills = func.get_technical_skills_response2(resume_text)
        education = func.get_education_details_overall(resume_text)
        template_path = 'Templates/Client sample format-2.docx'
        output_path = f'agilisium_resume_client_format_2/{filename}_resume.docx'

        func.fill_invitation3(template_path, output_path, name, summary)
        func.fill_table_skill_set(output_path, output_path, skills)
        func.fill_table_degree_details(output_path, output_path, func.get_degree_details_response(education))
        func.fill_table_institute_details(output_path, output_path, func.get_education_details_response(education))
        func.fill_table_education_years(output_path, output_path, func.get_education_years_response(education))
        func.replace_organization_count2(output_path, output_path, func.get_work_experience_response2(resume_text))

        updated_doc = func.replace_hyphens_with_bullet_points(output_path)
        updated_doc.save(output_path)
        func.remove_characters_from_docx2(output_path)
        func.replace_symbol_with_dash(output_path).save(output_path)
        time.sleep(2)
        func.process_docx11(output_path)
        func.delete_rows_with_any_empty_cells(output_path)

        filename = func.save_document(uploaded_file)
        filename = func.convert_to_pdf_if_docx(filename)
        out_path = func.pdf_to_image(filename)
        func.extract_and_save_passport_photo(out_path)
        func.replace_placeholder_with_image(output_path, 'passport_photo.png')
        func.remove_pdf_and_docx_files_in_script_directory()

        st.success(f"{filename} processed successfully.")
    except FileNotFoundError as e:
        st.error(str(e))


# ========== GENERIC PROCESSOR ==========
def process_and_save(uploaded_files, process_func, folder_path):
    if uploaded_files:
        if mode == "Trial Mode (1 time only)":
            st.session_state.trial_uses += 1

        os.makedirs(folder_path, exist_ok=True)
        for file in uploaded_files:
            filename = os.path.splitext(file.name)[0]
            process_func(file, filename)

        zipped = func.zip_folder_to_bytesio(folder_path)
        st.download_button("📦 Download Processed ZIP", data=zipped, file_name=f"{folder_path}.zip", mime="application/zip")

# ========== MAIN INTERFACE ==========
directories = ["agilisium_resume_internal_template", "agilisium_resume_client_format", "agilisium_resume_client_format_2"]
func.delete_directories(directories)
func.remove_pdf_and_docx_files_in_script_directory()

with st.expander("📎 Upload Resumes"):
    uploaded_files = file_upload()

st.sidebar.subheader("🧾 Choose Output Template")
if st.sidebar.button("Internal Template") and uploaded_files:
    process_and_save(uploaded_files, process_resume, "agilisium_resume_internal_template")

if st.sidebar.button("Client Template") and uploaded_files:
    process_and_save(uploaded_files, process_resume_2, "agilisium_resume_client_format")

if st.sidebar.button("Client Template with Photo") and uploaded_files:
    process_and_save(uploaded_files, process_resume_3, "agilisium_resume_client_format_2")
