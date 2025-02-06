import streamlit as st

# Page Config
st.set_page_config(page_title="Akhil P.S - CV", layout="wide")

# Header Section
st.title("👋 Hi, I'm Akhil Pandaraparambil Suresh")
st.subheader("Software Engineer | Python Developer")
st.write("📍 Location: Deggendorf, Germany")
st.write("📞 Tel: +49 15510248642")
st.write("📧 Email: akhilpsinbox@gmail.com")
st.write("🔗 LinkedIn: [Akhil P.S](https://www.linkedin.com/in/akhil-ps)")
st.write("💻 GitHub: [akhilpsin](https://github.com/akhilpsin)")
st.write("🏠 Address: Detterstraße 21, 94469, Deggendorf, Deutschland")

# Navigation Menu (One-page scrolling design)
sections = ["Summary", "Experience", "Skills", "Education", "Certifications", "Languages", "Hobbies", "Publications", "Contact"]
selected_section = st.radio("Navigate", sections, horizontal=True)

# Summary Section
if selected_section == "Summary":
    st.header("Summary")
    st.write("Experienced Software Engineer with **4.5 years** of expertise in **full-stack development, automation, ETL processes, and AI integration**, delivering scalable and high-performance solutions. Proven track record of collaborating with cross-functional teams in agile environments to align technical solutions with business objectives.")

    st.subheader("Key Skills and Achievements")
    st.write("- **Full-stack Development**: Built web applications and APIs using Flask, Django, React.js, Power Apps, and Streamlit, integrated with SQL databases. Utilized Docker for containerization, Git for version control, and cloud deployment.")
    st.write("- **Python Development & Automation**: Specialized in web automation, OCR, data extraction, and converting legacy macros and RPA processes into efficient Python scripts. Designed GUI tools with Tkinter and automated workflows using VBScript, Excel VBA, and BASH.")
    st.write("- **Data Management & AI Integration**: Proficient in ETL processes and data management with Python, SQL, MongoDB, and Azure. Integrated custom machine learning and LLM-based solutions to enhance workflows.")

# Experience Section
elif selected_section == "Experience":
    st.header("Professional Experience")

    # Senior Software Engineer - Optum
    with st.expander("Senior Software Engineer - Optum Global Solutions India Pvt. Ltd"):
        st.write("**Location:** Hyderabad, India")
        st.write("**Duration:** 27.01.2023 -- 28.12.2024")
        st.write("**Responsibilities:**")
        st.write("- Developed Python backend frameworks to automate auditing processes by interacting with IBM PCOMM and SQL.")
        st.write("- Built full-stack web applications using Flask, React.js, FastAPI, Streamlit, Microsoft SQL, MongoDB, and Docker.")
        st.write("- Integrated Large Language Models (LLM) and AI/ML technologies into new and existing applications.")
        st.write("- Built custom internal tools to assist the development team and conducted multiple internal trainings.")
        st.write("- Created tools to consume live APIs, perform USPS data cleansing, and implement Elasticsearch. Utilized fuzzy matching and NLTK libraries for data engineering and ETL solutions.")
        st.write("- Managed version control with Git and worked with Azure cloud services.")

    # Python Developer - Guidehouse
    with st.expander("Python Developer - Guidehouse India Pvt. Ltd"):
        st.write("**Location:** Thiruvananthapuram, India")
        st.write("**Duration:** 16.02.2022 -- 13.01.2023")
        st.write("**Responsibilities:**")
        st.write("- Implemented web automation, web crawling, data extraction, and other ETL operations using frameworks like Scrapy, Selenium, pandas, NumPy, and Requests.")
        st.write("- Assisted with Salesforce data loading and testing, developed shell scripts for system management, and conducted Python training for colleagues.")
        st.write("- Developed full-stack web applications using Flask, Django, SQL, and Microsoft Power Apps.")

    # Associate - Guidehouse
    with st.expander("Associate - Guidehouse India Pvt. Ltd"):
        st.write("**Location:** Thiruvananthapuram, India")
        st.write("**Duration:** 24.08.2020 -- 15.02.2022")
        st.write("**Responsibilities:**")
        st.write("- Developed Python scripts and optimized SQL queries to automate and verify multiple MIS reports.")
        st.write("- Demonstrated advanced Excel skills, including pivot tables, VLOOKUP, and data analysis.")
        st.write("- Designed and implemented detailed surveys using Qualtrics.")
        st.write("- Participated in full project lifecycle from requirements gathering, estimation, development, and deployments.")

# Skills Section
elif selected_section == "Skills":
    st.header("Technical Skills")
    
    st.subheader("Languages")
    st.write("Python, SQL, VB Script, Golang")
    
    st.subheader("Frameworks")
    st.write("Flask, FastAPI, React.js, Django, Streamlit")
    
    st.subheader("DevOps & Cloud Technologies")
    st.write("Docker, Git, Azure")
    
    st.subheader("AI/ML & NLP")
    st.write("Hugging Face (Transformers, Tokenizers, Datasets), Scikit-learn")
    
    st.subheader("Automation Tools")
    st.write("pywin32, Pyautogui, Power Automate, Tkinter, UI path")
    
    st.subheader("Testing & Utilities")
    st.write("pytest, smtplib, keyboard")
    
    st.subheader("ETL & Data Tools")
    st.write("Pandas, NumPy, Polars, SQLAlchemy, Regex")
    
    st.subheader("Data Extraction & Parsing")
    st.write("Scrapy, Requests, BeautifulSoup, Selenium, Playwright, pdfplumber, PyMuPDF, pytesseract, OpenCV")
    
    st.subheader("Big Data")
    st.write("Azure Data Factory, Elasticsearch")

# Education Section
elif selected_section == "Education":
    st.header("Education")
    
    st.write("**Bachelor of Technology in Computer Science and Engineering**")
    st.write("APJ Abdul Kalam Technological University")
    st.write("Kerala, India | 05.08.2016 - 29.11.2020")
    st.write("**Total Percentage:** 73%")
    st.write("Degree recognized by the German ANABIN database.")
    st.write("**Website:** [KTU](https://www.ktu.edu.in)")

# Certifications Section
elif selected_section == "Certifications":
    st.header("Certifications")
    
    st.write("- **Microsoft Azure AZ-900**: Microsoft Azure Fundamentals")
    st.write("- **Data Analysis with Python**: IBM on Coursera")
    st.write("- **Microsoft Azure Machine Learning**: Microsoft on Coursera")
    st.write("- **Introduction to Git and GitHub**: Google on Coursera")
    st.write("- **Agile Project Management**: Google on Coursera")
    st.write("- **Agile with Atlassian Jira**: Atlassian on Coursera")

# Languages Section
elif selected_section == "Languages":
    st.header("Languages")
    
    st.write("- **English**: Advanced (C1)")
    st.write("- **German**: Intermediate (A2)")
    st.write("- **Malayalam**: Native")
    st.write("- **Hindi**: Upper Intermediate (B2)")

# Hobbies Section
elif selected_section == "Hobbies":
    st.header("Hobbies")
    
    st.write("- **Reading**: I enjoy reading a variety of content, from books and blogs to theses and newspapers. I find it entertaining to observe and understand different perspectives.")
    st.write("- **Pencil Sketch**: During the COVID lockdown, I revived my childhood passion for drawing. I now create pencil portraits and traditional mural art like *Bhittichitra*.")
    st.write("- **Traveling**: Meeting new people, experiencing diverse cultures, and facing new challenges excite me. I particularly enjoy blue beaches, sunny weather, green surroundings, and historic sites.")
    st.write("- **Dance**: I took up dancing in college and found it fascinating how movement synchronizes with music. It has improved my health, confidence, and memory.")

# Publications Section
elif selected_section == "Publications":
    st.header("Publications")
    
    st.write("**Hospital Managing QR Code Web Application Using Django and Python**")
    st.write("IJCRT, Vol 8, Issue 5 May 2020")
    st.write("**Link to paper:** [IJCRT](https://ijcrt.org/papers/IJCRT2005507.pdf)")
    st.write("**Description:** Development and implementation of a web application for hospital management, utilizing QR codes. This application is built using the Django web framework.")

# Contact Section
elif selected_section == "Contact":
    st.header("📞 Contact Me")
    
    # Contact details
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("📧 **Email:** akhilpsinbox@gmail.com")
        st.write("🔗 **LinkedIn:** [Akhil P.S](https://www.linkedin.com/in/akhil-ps)")
        st.write("💻 **GitHub:** [akhilpsin](https://github.com/akhilpsin)")
    
    with col2:
        st.write("📱 **Phone:** +49 15510248642")
        st.write("🏠 **Address:** Detterstraße 21, 94469, Deggendorf, Deutschland")
    
    # Contact form
    st.write("### Send me a message")
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Send")
        
        if submit_button:
            st.success("Thank you for reaching out! I'll get back to you soon.")