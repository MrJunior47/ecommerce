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
        f'<a href={STRIPE_CHECKOUT} class="button">:money_with_wings: Дари Пари</a>',
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
        "Супер стрaшна снимка :anger:",
        "Логото е направено за канала ни в ТикТок. Щяхме да правим жидеа с BeyBlade-ove, ама те са оказаха боклуци..."
    ],
    "IMG_4016.jpg" : [
        "Още една снимка на логото ни",
        "Яки са а? "
        "Дейба и тъпите китайци, ама нищо."
    ],
    "IMG_4024.jpg" : [
        "Това е последното лого",
        "Малко е клише. Има много женски цветове, ама не е зле. ",
        "Вие какво мислите? "
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
st.subheader(":tv: Demo-Демек някво клипче за да ва забавлвам малко")
st.video(DEMO_VIDEO, format="video/mp4", start_time=0)

# --- FAQ ---
st.write("")
st.write("---")
st.subheader(":raising_hand: Въпроси и отговори")
faq = {
    ":small_blue_diamond: Защо може да ми трябват пари? :arrow_down_small: " : "За фризьор, на примерно. :scissors: Или пък да излезна с Паулина на вън. :wine_glass: ",
    ":small_blue_diamond: Как може да ми преведете пари? :arrow_down_small: " : "Цъкате на големия бутон с надпис \"Дари пари\" и си избирате метод за плащане. :currency_exchange: ",
    ":small_blue_diamond: Какви методи за плащане има? :arrow_down_small: " : "Може с крадитна карта. :credit_card: Може да ми пишете email и да ми ги дадете на ръка. :e-mail: Може с PayPal. Може и по банкков път. :inbox_tray: ",
    ":small_blue_diamond: Димитър ще вземе ли пари от тая работа? :arrow_down_small: " : ":shit: Може да му се иска, ама няма. :no_pedestrians: Аз сам съм си потрудих за този website и си е всичко за мен. :shark: ",
    ":small_blue_diamond: Защо не работи в момента? :arrow_down_small: " : "Ще го направя на български език. :new: Чакам да ми стане PayPal-a и трябва да си направя линк за плащане. :new: В краткото бъдеще ще може да ми пращате пари. :new: ",
}

for question, answer in faq.items():
    with st.expander(question):
        st.write(answer)

# --- CONTACT FORM ---
st.write("")
st.write("---")
st.subheader(":mailbox: Имате някакъв друг въпрос? Попитайте тук с емайл!")
contact_form = f"""
<form action="https://formsubmit.co/{CONTACT_EMAIL} method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder="Името тук" required>
    <input type="email" name="email" placeholder="Еmailа тук" required>
    <textarea name="message" placeholder="Напишете някакво съобщение"></textarea>
    <button type="submit" class="button" method="POST">Send email</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)
