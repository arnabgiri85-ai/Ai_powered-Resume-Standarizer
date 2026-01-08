# Ai_powered-Resume-Standarizer

🤖 AI-Powered Resume Standardization System

The **AI-Powered Resume Standardization System** is an end-to-end automation pipeline designed to solve the critical challenge of inconsistent resume formats in corporate HR workflows. In modern recruitment, resumes arrive in a myriad of unstructured formats—ranging from diverse PDF layouts to handwritten or image-based CVs—which often require manual, error-prone data entry for internal documentation.

This system leverages a **Hybrid AI Architecture** to fully automate the transformation of any resume into a clean, uniform corporate document. By integrating the multimodal intelligence of **Gemini 2.5 Pro** with a deterministic **Template Filling Engine**, the platform ensures 100% format fidelity while significantly reducing the time HR professionals spend perusing and editing documents.

 🚀 Key Technical Highlights

* **Multimodal Intelligence:** Utilizes **Gemini 2.5 Pro** to process and extract semantic data from PDFs, DOCX files, and raw images (JPG/PNG), overcoming the limitations of traditional text-only parsers.
* **Prompt-Engineered Extraction:** Employs sophisticated **Zero-Shot Learning** and custom delimiters to force the LLM into outputting predictable, structured data for complex fields like education and professional experience.
* **Automated Format Fidelity:** Features a modular engine built on `python-docx` that programmatically maps extracted data into three distinct corporate templates.
* **Vision-Integrated Features:** Includes a specialized **OpenCV** module that uses Haar Cascade classifiers to detect, crop, and insert candidate photos into the final document.
* **Streamlit Powered UI:** A responsive, user-friendly web interface for bulk resume processing and instant ZIP-packaged downloads.

🏗️ Proposed Architecture

The system operates on a dual-component logic:

1. **Generative AI Extraction Layer:** Handles semantic comprehension and data segmentation.
2. **Template Formatting Engine:** Executes rigid post-processing rules (auto-bulleting, bolding, and table cleanup) to guarantee visual perfection.

