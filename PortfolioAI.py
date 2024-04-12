import streamlit as st
import plotly.express as px
from streamlit_lottie import st_lottie
from streamlit_timeline import timeline
import streamlit.components.v1 as components
from constant import *
import requests

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)
        
# local_css("style/style.css")

# loading assets
lottie_gif = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_x17ybolp.json")
python_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
java_lottie = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_zh6xtlj9.json")
my_sql_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
git_lottie = load_lottieurl("https://assets9.lottiefiles.com/private_files/lf30_03cuemhb.json")
github_lottie = load_lottieurl("https://assets8.lottiefiles.com/packages/lf20_6HFXXE.json")
docker_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_35uv2spq.json")
figma_lottie = load_lottieurl("https://lottie.host/5b6292ef-a82f-4367-a66a-2f130beb5ee8/03Xm3bsVnM.json")
js_lottie = load_lottieurl("https://lottie.host/fc1ad1cd-012a-4da2-8a11-0f00da670fb9/GqPujskDlr.json")




# Function to create a Plotly graph for skills
def create_skills_chart(skills, levels):
    fig = px.bar(x=skills, y=levels, labels={'x': 'Skill', 'y': 'Proficiency Level'})
    return fig

# Sample data for skills (replace with actual data)
skills = ['Python', 'Data Analysis', 'Machine Learning']
levels = [90, 75, 85]

#st.title('💼 Career Showcase',align='center')

# # Create three columns
# col1, col2, col3 = st.columns([3,6,3])


# # Use the middle column to display the image
# with col2:
#     st.image('C:\\Users\\harsh\\Downloads\\38839 (1).jpg', width=150)

# Set up the Streamlit layout
st.markdown("""
    <div style='text-align: center;'>
    <br>
        <h2>💼 Career Showcase</h2>
        <br>
        <img src='https://img.freepik.com/free-photo/portrait-young-businessman-with-mustache-his-face-3d-rendering_1142-38839.jpg?t=st=1712898682~exp=1712902282~hmac=455b3b4500d8ef306cbcac2d5bbce038ae13359b16181cceee41267818b5c035&w=740' style='width: 200px;'>
        <!--<h5>Jack Codeheart</h5>-->
    </div>
""", unsafe_allow_html=True)

# ----------------- info ----------------- #
def gradient(color1, color2, color3, content1, content2):
    st.markdown(f'<h1 style="text-align:center;background-image: linear-gradient(to right,{color1}, {color2});font-size:30px;border-radius:2%;">'
                f'<span style="color:{color3};">{content1}</span><br>'
                f'<span style="color:white;font-size:10px;">{content2}</span></h1>', 
                unsafe_allow_html=True)

with st.container():
    col1,col2 = st.columns([8,3])

full_name = info['Full_Name']

gradient('#FFD4DD','#000395','e0fbfc',f"Hi, I'm {full_name}👋", info["Intro"])
#gradient('#FFD4DD','#e0fbfc','000395',f"Hi, I'm {full_name}👋", info["Intro"])
st.write("")
st.write(info['About'])
    
    
# with col2:
#      st_lottie(lottie_gif, height=100, key="data")


# Set up the Streamlit layout
#st.image('C:\\Users\\harsh\\Downloads\\38839 (1).jpg', width=150,align=center)

# # Display the skills section with a Plotly graph
# st.header('Skills')
# skills_chart = create_skills_chart(skills, levels)
# st.plotly_chart(skills_chart)


# ----------------- skillset ----------------- #
with st.container():
    st.subheader('⚒️ Skills')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st_lottie(python_lottie, height=70,width=70, key="python", speed=2.5)
    with col2:
        st_lottie(java_lottie, height=70,width=70, key="java", speed=4)
    with col3:
        st_lottie(my_sql_lottie,height=70,width=70, key="mysql", speed=2.5)
    with col4:
        st_lottie(git_lottie,height=70,width=70, key="git", speed=2.5)
    with col1:
        st_lottie(github_lottie,height=50,width=50, key="github", speed=2.5)
    with col2:
        st_lottie(docker_lottie,height=70,width=70, key="docker", speed=2.5)
    with col3:
        st_lottie(figma_lottie,height=50,width=50, key="figma", speed=2.5)
    with col4:
        st_lottie(js_lottie,height=50,width=50, key="js", speed=1)
    
# ----------------- timeline ----------------- #
with st.container():
    st.markdown("""""")
    st.subheader('📌 Career Snapshot')

    # load data
    with open('example.json', "r") as f:
        data = f.read()

    # render timeline
    timeline(data, height=400)
    
    
# # Display the achievements section
st.header('🏆 Achievements')
st.markdown("""
- Developed a machine learning model with 95% accuracy
- Published 5 research papers in top-tier journals
- Presented at international conferences
""")

#Sample data for strengths (replace with actual data)
strengths = ['Analytical', 'Communicative', 'Motivated']
values = [1, 1, 1]  # Equal values to represent each strength equally

# # Function to create a Plotly graph for strengths
# def create_strengths_chart(strengths, values):
#     fig = px.pie(names=strengths, values=values, title='')
#     fig.update_traces(textposition='inside', textinfo='label')
#     return fig




# Display the strengths section
st.header('💪 Strengths')
# st.markdown("""
# - Strong analytical and problem-solving skills
# - Excellent communication and teamwork abilities
# - Highly motivated and eager to learn new technologies
# """)

# strengths_chart = create_strengths_chart(strengths, values)
# st.plotly_chart(strengths_chart)
# Custom colors for each strength
colors = ['#FFA07A', '#87CEEB', '#FFD700']

# Function to create a Plotly graph for strengths
def create_strengths_chart(strengths, values, colors):
    fig = px.pie(names=strengths, values=values, title='')
    fig.update_traces(textposition='inside', textinfo='label', marker=dict(colors=colors))
    return fig

# Display the chart
st.plotly_chart(create_strengths_chart(strengths, values, colors))
        
import plotly.graph_objs as go
import numpy as np

# Sample data: random scores for 5 days
np.random.seed(42)  # For reproducible results
days = ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5']
scores = np.random.randint(1, 11, size=5)  # Random scores out of 10

# Function to create a Plotly graph for quiz scores with color fill
def create_scores_chart(days, scores):
    fig = px.line(
        x=days, y=scores, 
        title='',
        markers=True,
        labels={'x': 'Day', 'y': 'Score'}
    )
    fig.update_traces(line=dict(width=3), fill='tozeroy')  # Fill color under the line
    fig.update_layout(
        autosize=True,  # This will make the plot size responsive
        margin=dict(l=0, r=0, t=0, b=0),  # This will remove unnecessary margins
        plot_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=False, range=[0, 10]),
        template='plotly_white'  # Light theme for better color visibility
    )
    # Set a gradient color fill for visual appeal
    fig['data'][0]['fillcolor'] = 'rgba(135, 206, 235, 0.4)'  # Adjust the RGBA values as needed
    return fig



# Display the quiz scores section with a Plotly graph
st.header('🎯 Quiz Scores')
scores_chart = create_scores_chart(days, scores)
st.plotly_chart(scores_chart)       

# # -----------------  contact  ----------------- #
# st.header("📨 Contact Me")

# # with col2:
# #         col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
# contact_form = f"""
#         <form action="https://formsubmit.co/["Email"]" method="POST">
#             <input type="hidden" name="_captcha value="false">
#             <input type="text" name="name" placeholder="Your name" required>
#             <input type="email" name="email" placeholder="Your email" required>
#             <textarea name="message" placeholder="Your message here" required></textarea>
#             <button type="submit">Send</button>
#         </form>
#         """
# st.markdown(contact_form, unsafe_allow_html=True)

# -----------------  endorsement  ----------------- #
with st.container():
    # Divide the container into three columns
    col1,col2 = st.columns([2, 2])
    # In the first column (col1)        
    with col1:
        # Add a subheader to introduce the coworker endorsement slideshow
        st.subheader("🗣️ Coworker Endorsements")
        # Embed an HTML component to display the slideshow
        components.html(
        f"""
        <!DOCTYPE html>
        <html>
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- Styles for the slideshow -->
        <style>
            * {{box-sizing: border-box;}}
            .mySlides {{display: none;}}
            img {{vertical-align: middle;}}

            /* Slideshow container */
            .slideshow-container {{
            position: relative;
            margin: auto;
            width: 100%;
            }}

            /* The dots/bullets/indicators */
            .dot {{
            height: 15px;
            width: 15px;
            margin: 0 2px;
            background-color: #eaeaea;
            border-radius: 50%;
            display: inline-block;
            transition: background-color 0.6s ease;
            }}

            .active {{
            background-color: #6F6F6F;
            }}

            /* Fading animation */
            .fade {{
            animation-name: fade;
            animation-duration: 1s;
            }}

            @keyframes fade {{
            from {{opacity: .4}} 
            to {{opacity: 1}}
            }}

            /* On smaller screens, decrease text size */
            @media only screen and (max-width: 300px) {{
            .text {{font-size: 11px}}
            }}
            </style>
        </head>
        <body>
            <!-- Slideshow container -->
            <div class="slideshow-container">
                <div class="mySlides fade">
                <img src={endorsements["img1"]} style="width:100%">
                </div>

                <div class="mySlides fade">
                <img src={endorsements["img2"]} style="width:100%">
                </div>

                <div class="mySlides fade">
                <img src={endorsements["img3"]} style="width:100%">
                </div>

            </div>
            <br>
            <!-- Navigation dots -->
            <div style="text-align:center">
                <span class="dot"></span> 
                <span class="dot"></span> 
                <span class="dot"></span> 
            </div>

            <script>
            let slideIndex = 0;
            showSlides();

            function showSlides() {{
            let i;
            let slides = document.getElementsByClassName("mySlides");
            let dots = document.getElementsByClassName("dot");
            for (i = 0; i < slides.length; i++) {{
                slides[i].style.display = "none";  
            }}
            slideIndex++;
            if (slideIndex > slides.length) {{slideIndex = 1}}    
            for (i = 0; i < dots.length; i++) {{
                dots[i].className = dots[i].className.replace("active", "");
            }}
            slides[slideIndex-1].style.display = "block";  
            dots[slideIndex-1].className += " active";
            }}

            var interval = setInterval(showSlides, 2500); // Change image every 2.5 seconds

            function pauseSlides(event)
            {{
                clearInterval(interval); // Clear the interval we set earlier
            }}
            function resumeSlides(event)
            {{
                interval = setInterval(showSlides, 2500);
            }}
            // Set up event listeners for the mySlides
            var mySlides = document.getElementsByClassName("mySlides");
            for (i = 0; i < mySlides.length; i++) {{
            mySlides[i].onmouseover = pauseSlides;
            mySlides[i].onmouseout = resumeSlides;
            }}
            </script>

            </body>
            </html> 

            """,
                height=270,
    )  

# -----------------  contact  ----------------- #
    with col2:
        st.subheader("📨 Contact Me")
        contact_form = f"""
        <form action="https://formsubmit.co/{info["Email"]}" method="POST">
            <input type="hidden" name="_captcha value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        st.markdown(contact_form, unsafe_allow_html=True)

        
# # Run the Streamlit app
# if __name__ == '__main__':
