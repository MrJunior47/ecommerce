from pathlib import Path 
import os

import streamlit as st # pip install streamlit
from PIL import Image # pip install pillow

# --- PATH SETTINGS ---
THIS_DIR = os.getcwd()
ASSETS_DIR = THIS_DIR / assets
STYLES_DIR = THIS_DIR / styles
CSS_FILE = STYLES_DIR / main.css

# --- GENERAL SETTINGS ---
STRIPE_CHECKOUT = "https://buy.stripe.com/muss ich noch machen"
CONTACT_EMAIL = "YOUREMAIL@EMAIL.COM"
DEMO_VIDEO = "https://www.youtube.com/watch?v=DUqqPCPll_g"
PRODUCT_NAME = "Excel Add-in: MyToolBelt"
PRODUCT_TAGLINE = "Ready To Become an Office Superhero"
PRODUCT_DESCRIPTION = """
MyToolBelt saves every smart office worker time and effort 
when it dcomes to analysis with a unique set od tools you won't find anywhere else:

- Generate flawless Python code
- Call Python scripts 
- Create Junyper Notebooks from Excel
- Add tickmarks to cells and highlight key areas
- Create an informative table of content with ease
- ...and many more powerful features
**This is your new superpower; why go to work without it ?
"""

def load_css_file(css_file_path):
    with open(css_file_path)as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- PAGE CONFIG ---
st.set_page_config(
    page_title = PRODUCT_NAME ,
    page_icon = ":star:",
    layout = "centered",
    initial_sidebar_state = "collapsed",
)
load_css_file(CSS_FILE)
# --- MAIN SECTION ---

st.header(PRODUCT_NAME)
st.subheader(PRODUCT_TAGLINE)
left_col , right_col = st.columns((2,1))
with left_col:
    st.text("")
    st.write(PRODUCT_DESCRIPTION)
    st.markdown(
        f'<a href={STRIPE_CHECKOUT} class="button"> Get the add-in</a>',
        unsafe_allow_html=True,
    )
with right_col:
    product_image = Image.open(ASSETS_DIR / "IMG_4018.jpg")
    st.image(product_image, width=450)

# --- FEATURES ---
st.write("")
st.write("---")
st.write(":rocket: Features")
features = {
    "IMG_4018.jpg" : [
        "Run Python Files From Excel",
        "After blah balh some info with long text that sounds very convincing to buy my product"
    ],
    "IMG_4016.jpg" : [
        "Create Pandas Dataframes",
        "Much more info about every little convincing thing that will make you give me your money and run away with it"
        "And then last foto"
    ],
    "IMG_4024.jpg" : [
        "Create Jupyter Notebooks",
        "Last picture, idk how didnt spell anything wrong for now, but here you go more info",
        "Nevermind just pay me and you'll get my great product which im trying to convince to for so much time and effort"
        "Python is fun"
    ]
}

for image, description in features.items():
    image = Image.open(ASSETS_DIR / image)
    st.write("")
    left_col, right_col = st.columns(2)
    left_col.image(image, use_column_width=True)
    right_col.write(f"**{description[0]}**")
    right_col.write(description[1])

# --- DEMO ---
st.write("")
st.write("---")
st.subheader(":tv: Demo")
st.video(DEMO_VIDEO, format="video/mp4", start_time=0)

# --- FAQ ---
st.write("")
st.write("---")
st.subheader(":raising_hand: FAQ")
faq = {
    "Question 1" : "Some very smart answer that convice you to buy more of my product",
    "Question 2" : "Some very smart answer that convice you to buy more of my product",
    "Question 3" : "Some very smart answer that convice you to buy more of my product",
    "Question 4" : "Some very smart answer that convice you to buy more of my product",
    "Question 5" : "Some very smart answer that convice you to buy more of my product",
}

for question, answer in faq.items():
    with st.expander(question):
        st.write(answer)

# --- CONTACT FORM ---
st.write("")
st.write("---")
st.subheader(":mailbox: Have a quesiton? Ask Away!")
contact_form = f"""
<form action="https://formsubmit.co/{CONTACT_EMAIL} method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Your name" required>
    <input type="email" name="email" placeholder="Your email" required>
    <textarea name="message" placeholder="Your message here"></textarea>
    <button type="submit" class="button">Send email</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)
