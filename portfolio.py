import streamlit as st
from pathlib import Path
import base64

# --- Load image and encode it as base64 ---
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        b64 = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{b64}"

# --- Page Config ---
st.set_page_config(
    page_title="Suraj Bakawat | Portfolio", 
    layout="wide",
    initial_sidebar_state="auto",
    menu_items=None,
)

linkedin_icon_base64 = get_base64_image("linkedin_icon.png")

# --- Header ---
st.title("Suraj Bakawat", anchor=False)
st.subheader("Software Engineer", anchor=False)
st.write("📞 +91 8839148272")
st.write("📧 [surajbakawat1@gmail.com](mailto:surajbakawat1@gmail.com)")
linkedin_icon_base64 = get_base64_image("linkedin_icon.png")
st.markdown(
    f"""
    <a href="https://linkedin.com/in/surajbakawat-5b5a85195/" target="_blank" style="text-decoration: none;">
        <img src="{linkedin_icon_base64}" width="22" style="vertical-align:middle; margin-right:5px;" />
        LinkedIn Profile
    </a>
    """,
    unsafe_allow_html=True,
)
st.markdown("")

# --- Short Introduction ---
st.markdown(
    """
    <div style='
        background-color: #313131;
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #e0e0e0;
        margin-bottom: 20px;
    '>
        Hello, I'm Suraj Bakawat, a Computer Science and Engineering graduate from IIT Patna. At WinZO, Talentica, and Reliance Games, I’ve worked across SDKs, backend services, GenAI features, and large-scale game systems. I enjoy solving complex problems, collaborating across teams, and continuously learning. To stay ahead of the curve, I'm dedicated to personal growth, continuously learning and adapting to industry trends and technologies. I'm eager to connect with developers and creators who share the excitement for crafting exceptional experiences, both within and beyond the corporate landscape! 
    </div>
    """,
    unsafe_allow_html=True
)


# --- Resume Download ---
with open("Suraj_Bakawat_Resume.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(
    label="Download Resume",
    data=PDFbyte,
    file_name="Suraj_Bakawat_Resume.pdf",
    mime="application/pdf",
)

st.markdown("---")

# --- Sidebar ---
st.sidebar.title("Skills & Tools")
st.sidebar.subheader("Languages")
st.sidebar.write("C++, C, C#, Python, Golang, Java")

st.sidebar.subheader("Engines and Tools")
st.sidebar.write("Unreal Engine, Unity, Android Studio, SFML & OpenGL")

st.sidebar.subheader("Technical Skills")
st.sidebar.write("""
- Object Oriented Programming  
- Algorithms and Data Structures  
- Multithreading & Concurrency  
- Memory Management  
- Backend Development  
- Cross-Platform Development  
- Debugging and Profiling  
- Version Control (Git)  
- Game Development  
- Machine Learning  
- C++11/14/17/20  
- SDK Integrations  
- Database Management  
- Microservices & APIs  
""")

# --- Experience Section ---
st.header("Experience", anchor=False)

st.subheader("WinZO | Software Engineer", anchor=False)
st.write("**2025 - Present**")
st.write("""
- Developed and optimized games at scale.  
- Built internal SDKs and dev tools to enhance the WinZO platform.
- Worked across teams to streamline performance and integration.
""")

st.subheader("Talentica Software | Software Engineer", anchor=False)
st.write("**2024 - 2025**")
st.write("""
- Developed advanced Ad SDK for Unreal & Unity with 3D and standard ad formats.  
- Backend systems in Go and Java.  
- Integrated GenAI with LangChain & Python.  
- Created a secure key management tool using C++ (like AWS CloudHSM).
""")

st.subheader("Reliance Games | Software Engineer", anchor=False)
st.write("**2022 - 2024**")
st.write("""
- Lead programmer for WWE Mayhem.  
- Developed ML-based opponent AI.  
- Maintained and optimized game systems for smooth user experience.
""")

st.markdown("---")
# --- Education ---
st.header("Education", anchor=False)

st.subheader("Indian Institute of Technology Patna", anchor=False)
st.write("**B.Tech in Computer Science and Engineering**")
st.write("2018 - 2022")

st.markdown("---")

# --- Projects Section ---
st.header("Projects", anchor=False)

st.markdown("")
st.subheader("Vector Horizon (2025)", anchor=False)
st.write("[View on Steam](https://store.steampowered.com/app/3801540/Vector_Horizon/)")
st.write("A 3D platformer featuring a flying car, developed in Unreal Engine 5 and C++, released on Steam (PC).")
st.markdown(
    """
    <iframe width="640" height="360" src="https://www.youtube.com/embed/Q_pv6QVvIjA" 
    frameborder="0" allowfullscreen></iframe>
    """,
    unsafe_allow_html=True
)

st.markdown("")
st.markdown("")
st.markdown("")
st.subheader("Almanac (2023)", anchor=False)
st.write("[View on Google Play Store](https://play.google.com/store/apps/details?id=com.RaAten.Almanac)")
st.write("A 2D fantasy RPG built in Unity and C#, released on the Google Play Store.")
st.markdown(
    """
    <iframe width="640" height="360" src="https://www.youtube.com/embed/pW4nIEWJsmc" 
    frameborder="0" allowfullscreen></iframe>
    """,
    unsafe_allow_html=True
)

st.markdown("")
st.markdown("")
st.markdown("")
st.subheader("GunBoxing (2022)", anchor=False)
st.write("[View on Steam](https://store.steampowered.com/app/1978090/GunBoxing/)")
st.write("A first-person shooter with fighting game mechanics. Built in Unreal Engine 4 and C++, released on Steam (PC).")
st.markdown(
    """
    <iframe width="640" height="360" src="https://www.youtube.com/embed/YiDwlVA0btQ" 
    frameborder="0" allowfullscreen></iframe>
    """,
    unsafe_allow_html=True
)
st.markdown("---")
st.caption("© 2025 Suraj Bakawat")
