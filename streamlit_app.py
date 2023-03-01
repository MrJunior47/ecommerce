from pathlib import Path 
import os

import streamlit as st # pip install streamlit
from PIL import Image # pip install pillow

# --- PATH SETTINGS ---
THIS_DIR = os.getcwd()
ASSETS_DIR = f"{THIS_DIR}/Assets"
STYLES_DIR = f"{THIS_DIR}/Styles"
CSS_FILE = f"{STYLES_DIR}/main.css"

# --- GENERAL SETTINGS ---
STRIPE_CHECKOUT = "https://buy.stripe.com/muss ich noch machen"
CONTACT_EMAIL = "venidavchev@gmail.com"
DEMO_VIDEO = "https://www.youtube.com/watch?v=DUqqPCPll_g"
PRODUCT_NAME = "Websait-a нa Venelin "
PRODUCT_TAGLINE = "Допълнителни доходи :money_mouth_face: "
PRODUCT_DESCRIPTION = """
Този сайт е специално за наще.
Това е кратко описание:

-  Можете да ми преведете пари супер лесно. :white_check_mark: 
-  Нямате нужда от IBAN или BIC, всичко е улеснено. :martial_arts_uniform: 
-  Няма нужда да търсите някакви стотинки и да пълните джобовете ми. :moneybag:
-  Ще пиша на кирилица, когато подновя сайта. :bookmark_tabs: 
-  Това е само пробно. Можете да ми изпращате имейлил
-  ...в бъдеще всичко ще бъде по-лесно
- Това е новият ви супергерой! :hero:
- Защо са ви QR-Cod-oвe или IBAN-и :question:
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
        f'<a href={STRIPE_CHECKOUT} class="button">:money_with_wings: Darenie</a>',
        unsafe_allow_html=True,
    )
with right_col:
    product_image = Image.open("/app/ecommerce/Assets/IMG_4018.jpg")
    st.image(product_image, width=150)

# --- FEATURES ---
st.write("")
st.write("---")
st.write(":rocket: Features")
features = {
    "IMG_4018.jpg" : [
        "Super strashna snimka :anger:",
        "Logoto e napraveno za kanala ni v TikTok. Shtqhme da pravim videa s BeyBlade-ove, ama te sa okazaha bokluci..."
    ],
    "IMG_4016.jpg" : [
        "Oshte edna snimka da logoto ni",
        "Qki sa a? "
        " Deiba i tupite kitaici, ama nishto."
    ],
    "IMG_4024.jpg" : [
        "Tva e po svetloto logo",
        "Malko e klische. Ima mnogo jenski cvetove, ama ne e zle. ",
        "Vie kakvo mislite? "
    ]
}

for image, description in features.items():
    image = Image.open(f"/app/ecommerce/Assets/{image}")
    st.write("")
    left_col, right_col = st.columns(2)
    left_col.image(image, use_column_width=True)
    right_col.write(f"**{description[0]}**")
    right_col.write(description[1])

# --- DEMO ---
st.write("")
st.write("---")
st.subheader(":tv: Demo-Demek nqkvo klip4e da va zabavlqva malko")
st.video(DEMO_VIDEO, format="video/mp4", start_time=0)

# --- FAQ ---
st.write("")
st.write("---")
st.subheader(":raising_hand: FAQ")
faq = {
    ":small_blue_diamond: Zashto moje da mi trqbvat pari? :arrow_down_small: " : "Za Frizior, na primerno. :scissors:  Ili puk da izlezna s Paulina na vun. :wine_glass: ",
    ":small_blue_diamond: Kak moje da mi prevedete pari? :arrow_down_small: " : "Cukate na golemiq buton s nadpis \"Darenie\" i si izbirate metod za plashtane. :currency_exchange: ",
    ":small_blue_diamond: Kakvi metodi ima za plashtane? :arrow_down_small: " : "Moje s kreditna karta. :credit_card: Moje da mi pishete email i da mi gi dadete na ruka. :e-mail: Moje s PayPal. Moje i po bankov put. :inbox_tray: ",
    ":small_blue_diamond: Dimitar shte vzeme li pari ot taq rabota? :arrow_down_small: " : ":shit: Moje da mu sa iska mnogo, ama nqma. :no_pedestrians:  Az sam si sa potrudih za tozi website i si e vsi4ko za men. :shark: ",
    ":small_blue_diamond: Zashto v momenta ne raboti? :arrow_down_small: " : "Shte go napravq na bulgarski ezik :new: 4akam da mi stane PayPal-a i trqbva da si napravq link za plashtane. :new:  V kratkoto budeshte shte mojete da mi prashtate pari. :new: ",
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
