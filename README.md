
# 📄 Resume Standardization System

### AI-Powered Resume Transformation using Gemini AI

An intelligent resume standardization platform built with **Streamlit**, **Google Gemini AI**, **OpenCV**, and **Python-Docx** that automatically transforms resumes from multiple formats into standardized corporate templates.

Supports **PDF, DOCX, JPG, and PNG** resumes and generates professional recruiter-ready resume formats.

---

## 🚀 Features

✅ Multi-format Resume Upload (PDF, DOCX, JPG, PNG)

✅ AI-Powered Resume Understanding using Gemini

✅ Automatic Resume Standardization

✅ Education, Skills & Experience Extraction

✅ Project Experience Generation

✅ Passport Photo Extraction

✅ Bulk Resume Processing

✅ Multiple Corporate Templates

✅ ZIP Download Support

✅ Streamlit Web Interface

---

# 🏗️ System Architecture

```mermaid
flowchart LR

A[Resume Upload] --> B{Input Type}

B --> C[PDF]
B --> D[DOCX]
B --> E[Image]

C --> F[Text Extraction]
D --> F
E --> G[Gemini Vision OCR]

G --> F

F --> H[Google Gemini AI]

H --> I[Name Extraction]
H --> J[Summary Generation]
H --> K[Skills Extraction]
H --> L[Education Parsing]
H --> M[Certification Detection]
H --> N[Project Experience Extraction]

I --> O[Resume Standardization Engine]
J --> O
K --> O
L --> O
M --> O
N --> O

O --> P[Internal Template]
O --> Q[Client Template]
O --> R[Client Template + Photo]

P --> S[DOCX Output]
Q --> S
R --> S

S --> T[ZIP Packaging]
T --> U[Download]
```

---

# 🤖 AI Processing Pipeline

```mermaid
flowchart TD

A[Resume Input] --> B[Text Extraction]

B --> C[Gemini 2.5 Flash]

C --> D1[Extract Name]
C --> D2[Generate Professional Summary]
C --> D3[Extract Skills]
C --> D4[Extract Education]
C --> D5[Extract Certifications]
C --> D6[Extract Projects]

D1 --> E[Structured Resume Data]
D2 --> E
D3 --> E
D4 --> E
D5 --> E
D6 --> E

E --> F[Template Population]

F --> G[Formatting Engine]

G --> H[Final Standardized Resume]
```

---

# 📷 Client Template With Photo Workflow

One of the unique features of this project is automatic passport-photo generation from resumes.

```mermaid
flowchart TD

A[Resume Upload] --> B[Convert Resume to PDF]

B --> C[PDF to Image]

C --> D[Face Detection OpenCV]

D --> E[Passport Photo Extraction]

E --> F[Photo Cropping]

F --> G[Insert Photo into Template]

G --> H[Generate Final Resume]
```

---

# 🧩 Component Architecture

```mermaid
graph TB

subgraph Frontend
A[Streamlit UI]
end

subgraph AI Layer
B[Google Gemini AI]
end

subgraph Processing Layer
C[PDF Parser]
D[DOCX Parser]
E[Image Parser]
F[Resume Analyzer]
end

subgraph Template Engine
G[Internal Template]
H[Client Template]
I[Client Template + Photo]
end

subgraph Output
J[DOCX Generator]
K[ZIP Generator]
end

A --> C
A --> D
A --> E

C --> F
D --> F
E --> F

F --> B

B --> G
B --> H
B --> I

G --> J
H --> J
I --> J

J --> K
```

---

# 📊 Technology Stack

| Category              | Technology              |
| --------------------- | ----------------------- |
| Frontend              | Streamlit               |
| LLM                   | Google Gemini 2.5 Flash |
| Vision AI             | Gemini Vision           |
| PDF Processing        | PyMuPDF                 |
| DOCX Processing       | python-docx             |
| Image Processing      | OpenCV                  |
| Face Detection        | Haar Cascade            |
| PDF Generation        | ReportLab               |
| Environment Variables | python-dotenv           |
| Packaging             | ZipFile                 |

---

# 📁 Project Structure

```text
Resume-Standardization-System/
│
├── app.py
├── all_functions.py
├── .env
│
├── Templates/
│   ├── Kasukabe_template.docx
│   ├── Client sample format.docx
│   └── Client sample format-2.docx
│
├── agilisium_resume_internal_template/
├── agilisium_resume_client_format/
├── agilisium_resume_client_format_2/
│
├── passport_photo.png
│
└── README.md
```

---

# ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/resume-standardization-system.git

cd resume-standardization-system
```

### Create Virtual Environment

```bash
python -m venv venv
```

Linux/Mac

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file

```env
GEMINI_API_KEY=YOUR_API_KEY
```

### Run Application

```bash
streamlit run app.py
```

---

# 🔄 Resume Processing Workflow

```text
Resume Upload
      │
      ▼
Format Detection
      │
      ▼
Text Extraction
      │
      ▼
Gemini AI Analysis
      │
      ▼
Information Categorization
      │
      ├── Name
      ├── Education
      ├── Skills
      ├── Certifications
      ├── Experience
      └── Projects
      │
      ▼
Template Population
      │
      ▼
Document Formatting
      │
      ▼
ZIP Generation
      │
      ▼
Download
```

---

# 🎯 Business Use Cases

### HR Teams

* Resume Standardization
* Candidate Profiling
* Skill Inventory Creation

### Recruitment Agencies

* Bulk Resume Processing
* Client Format Generation
* Faster Candidate Submission

### Staffing Companies

* Automated Resume Enhancement
* Professional Resume Presentation
* Template Compliance

---

# 📈 Future Enhancements

* ATS Score Calculation
* Resume Ranking System
* JD Matching Engine
* Resume Skill Gap Analysis
* Multi-Language Resume Support
* Resume-to-LinkedIn Converter
* AI Career Advisor
* Dashboard Analytics
* Cloud Deployment

---

# ⭐ Project Highlights

* AI-powered Resume Understanding
* Gemini Vision Integration
* Passport Photo Extraction
* Multiple Resume Templates
* Bulk Processing Support
* Corporate Recruitment Ready
* End-to-End Automation
* Modern Streamlit Interface

---

## 📸 Screenshots

Add application screenshots here:

```md
![Home Page](images/home.png)

![Processing](images/processing.png)

![Output](images/output.png)
```

---

## 👨‍💻 Author

**Arnab Giri**

M.Sc. Computer Science | AI & Machine Learning Enthusiast

GitHub: `arnabgiri85-ai`

---

This version is much more professional and visually appealing for recruiters, GitHub visitors, internship applications, and project demonstrations.
****
