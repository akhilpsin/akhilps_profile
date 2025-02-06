import streamlit as st
from PIL import Image

# Page Config (MUST BE THE FIRST STREAMLIT COMMAND)
st.set_page_config(page_title="Akhil P.S - CV", layout="wide")

# Custom CSS for dark theme and minimal design
st.markdown(
    """
    <style>
    /* Dark theme */
    .stApp {
        background-color: #1e1e1e;
        color: #ffffff;
        font-family: 'Arial', sans-serif;
    }
    .stHeader {
        font-size: 3rem;
        font-weight: bold;
        color: #ffffff;
        text-align: center;
        margin-bottom: 20px;
    }
    .stSubheader {
        font-size: 1.5rem;
        font-weight: bold;
        color: #cccccc;
        text-align: center;
        margin-bottom: 40px;
    }
    .stCard {
        background-color: #2d2d2d;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        margin-bottom: 20px;
        color: #ffffff;
    }
    .stButton button {
        background-color: #0078d7;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        border: none;
        font-size: 16px;
        width: 100%;
    }
    .stButton button:hover {
        background-color: #005a9e;
    }
    .stFooter {
        text-align: center;
        padding: 20px;
        background-color: #1e1e1e;
        color: white;
        margin-top: 40px;
    }
    /* Navigation menu */
    .stRadio > div {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-bottom: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header Section
st.markdown('<div class="stHeader">AKHIL P.S</div>', unsafe_allow_html=True)
st.markdown('<div class="stSubheader">I\'M A SOFTWARE ENGINEER</div>', unsafe_allow_html=True)

# Download CV Button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    with open("CV/Akhil_PS_CV.pdf", "rb") as pdf_file:
        st.download_button(
            label="📄 DOWNLOAD CV",
            data=pdf_file,
            file_name="Akhil_PS_CV.pdf",
            mime="application/pdf",
        )

# Navigation Menu
sections = ["About Me", "Work Experience", "Skills", "Education", "Languages", "Courses/Certificates", "Publication", "Contact Me"]
selected_section = st.radio(" ", sections, horizontal=True)

# About Me Section
if selected_section == "About Me":
    st.markdown('<div class="stHeader">ABOUT ME</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="stCard">
            <p>Experienced Software Engineer with <strong>4.5 years</strong> of expertise in <strong>full-stack development, automation, ETL processes, and AI integration</strong>, delivering scalable and high-performance solutions. Proven track record of collaborating with cross-functional teams in agile environments to align technical solutions with business objectives.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Work Experience Section
elif selected_section == "Work Experience":
    st.markdown('<div class="stHeader">WORK EXPERIENCE</div>', unsafe_allow_html=True)

    # Senior Software Engineer - Optum
    with st.expander("🔧 Senior Software Engineer - Optum Global Solutions India Pvt. Ltd"):
        st.markdown(
            """
            <div class="stCard">
                <p><strong>Location:</strong> Hyderabad, India</p>
                <p><strong>Duration:</strong> 27.01.2023 -- 28.12.2024</p>
                <p><strong>Responsibilities:</strong></p>
                <ul>
                    <li>Developed Python backend frameworks to automate auditing processes by interacting with IBM PCOMM and SQL.</li>
                    <li>Built full-stack web applications using Flask, React.js, FastAPI, Streamlit, Microsoft SQL, MongoDB, and Docker.</li>
                    <li>Integrated Large Language Models (LLM) and AI/ML technologies into new and existing applications.</li>
                    <li>Built custom internal tools to assist the development team and conducted multiple internal trainings.</li>
                    <li>Created tools to consume live APIs, perform USPS data cleansing, and implement Elasticsearch. Utilized fuzzy matching and NLTK libraries for data engineering and ETL solutions.</li>
                    <li>Managed version control with Git and worked with Azure cloud services.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Python Developer - Guidehouse
    with st.expander("🐍 Python Developer - Guidehouse India Pvt. Ltd"):
        st.markdown(
            """
            <div class="stCard">
                <p><strong>Location:</strong> Thiruvananthapuram, India</p>
                <p><strong>Duration:</strong> 16.02.2022 -- 13.01.2023</p>
                <p><strong>Responsibilities:</strong></p>
                <ul>
                    <li>Implemented web automation, web crawling, data extraction, and other ETL operations using frameworks like Scrapy, Selenium, pandas, NumPy, and Requests.</li>
                    <li>Assisted with Salesforce data loading and testing, developed shell scripts for system management, and conducted Python training for colleagues.</li>
                    <li>Developed full-stack web applications using Flask, Django, SQL, and Microsoft Power Apps.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

    # Associate - Guidehouse
    with st.expander("👨‍💻 Associate - Guidehouse India Pvt. Ltd"):
        st.markdown(
            """
            <div class="stCard">
                <p><strong>Location:</strong> Thiruvananthapuram, India</p>
                <p><strong>Duration:</strong> 24.08.2020 -- 15.02.2022</p>
                <p><strong>Responsibilities:</strong></p>
                <ul>
                    <li>Developed Python scripts and optimized SQL queries to automate and verify multiple MIS reports.</li>
                    <li>Demonstrated advanced Excel skills, including pivot tables, VLOOKUP, and data analysis.</li>
                    <li>Designed and implemented detailed surveys using Qualtrics.</li>
                    <li>Participated in full project lifecycle from requirements gathering, estimation, development, and deployments.</li>
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Skills Section
elif selected_section == "Skills":
    st.markdown('<div class="stHeader">SKILLS</div>', unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="stCard">
            <p><strong>💻 Languages:</strong> Python, SQL, VB Script, Golang</p>
            <p><strong>📚 Frameworks:</strong> Flask, FastAPI, React.js, Django, Streamlit</p>
            <p><strong>☁️ DevOps & Cloud Technologies:</strong> Docker, Git, Azure</p>
            <p><strong>🤖 AI/ML & NLP:</strong> Hugging Face (Transformers, Tokenizers, Datasets), Scikit-learn</p>
            <p><strong>⚙️ Automation Tools:</strong> pywin32, Pyautogui, Power Automate, Tkinter, UI path</p>
            <p><strong>🧪 Testing & Utilities:</strong> pytest, smtplib, keyboard</p>
            <p><strong>📊 ETL & Data Tools:</strong> Pandas, NumPy, Polars, SQLAlchemy, Regex</p>
            <p><strong>🔍 Data Extraction & Parsing:</strong> Scrapy, Requests, BeautifulSoup, Selenium, Playwright, pdfplumber, PyMuPDF, pytesseract, OpenCV</p>
            <p><strong>📈 Big Data:</strong> Azure Data Factory, Elasticsearch</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Education Section
elif selected_section == "Education":
    st.markdown('<div class="stHeader">EDUCATION</div>', unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="stCard">
            <p><strong>Bachelor of Technology in Computer Science and Engineering</strong></p>
            <p>APJ Abdul Kalam Technological University</p>
            <p>Kerala, India | 05.08.2016 - 29.11.2020</p>
            <p><strong>Total Percentage:</strong> 73%</p>
            <p>Degree recognized by the German ANABIN database.</p>
            <p><strong>Website:</strong> <a href="https://www.ktu.edu.in">KTU</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Languages Section
elif selected_section == "Languages":
    st.markdown('<div class="stHeader">LANGUAGES</div>', unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="stCard">
            <ul>
                <li><strong>English</strong>: Advanced (C1)</li>
                <li><strong>German</strong>: Intermediate (A2)</li>
                <li><strong>Malayalam</strong>: Native</li>
                <li><strong>Hindi</strong>: Upper Intermediate (B2)</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Courses/Certificates Section
elif selected_section == "Courses/Certificates":
    st.markdown('<div class="stHeader">COURSES/CERTIFICATES</div>', unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="stCard">
            <ul>
                <li><strong>Microsoft Azure AZ-900</strong>: Microsoft Azure Fundamentals</li>
                <li><strong>Data Analysis with Python</strong>: IBM on Coursera</li>
                <li><strong>Microsoft Azure Machine Learning</strong>: Microsoft on Coursera</li>
                <li><strong>Introduction to Git and GitHub</strong>: Google on Coursera</li>
                <li><strong>Agile Project Management</strong>: Google on Coursera</li>
                <li><strong>Agile with Atlassian Jira</strong>: Atlassian on Coursera</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Projects Section
elif selected_section == "Projects":
    st.markdown('<div class="stHeader">PROJECTS</div>', unsafe_allow_html=True)
    
    st.markdown(
        """
        <div class="stCard">
            <p><strong>Hospital Managing QR Code Web Application Using Django and Python</strong></p>
            <p>IJCRT, Vol 8, Issue 5 May 2020</p>
            <p><strong>Link to paper:</strong> <a href="https://ijcrt.org/papers/IJCRT2005507.pdf">IJCRT</a></p>
            <p><strong>Description:</strong> Development and implementation of a web application for hospital management, utilizing QR codes. This application is built using the Django web framework.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Contact Me Section
elif selected_section == "Contact Me":
    st.markdown('<div class="stHeader">CONTACT ME</div>', unsafe_allow_html=True)
    
    # Contact details
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(
            """
            <div class="stCard">
                <p>📧 <strong>Email:</strong> akhilpsinbox@gmail.com</p>
                <p>🔗 <strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/akhil-ps">Akhil P.S</a></p>
                <p>💻 <strong>GitHub:</strong> <a href="https://github.com/akhilpsin">akhilpsin</a></p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    with col2:
        st.markdown(
            """
            <div class="stCard">
                <p>📱 <strong>Phone:</strong> +49 15510248642</p>
                <p>🏠 <strong>Address:</strong> Detterstraße 21, 94469, Deggendorf, Deutschland</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    
    # Contact form
    st.markdown('<div class="stSubheader">📩 Send me a message</div>', unsafe_allow_html=True)
    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Send")
        
        if submit_button:
            st.success("Thank you for reaching out! I'll get back to you soon.")

# Footer
st.markdown(
    """
    <div class="stFooter">
        <p>© 2024 Akhil P.S</p>
    </div>
    """,
    unsafe_allow_html=True,
)