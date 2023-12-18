import streamlit as st 
from data import *
from backend import Animator
import io

# SIDEBAR
st.sidebar.header("Login")
url = st.sidebar.text_input("URL")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password")

if st.sidebar.button("Authorize"):
    st.session_state['animator'] = Animator(url, username, password)

st.markdown('---')

st.sidebar.header("Content")
text = st.sidebar.text_area("Type your text", max_chars=250)
st.sidebar.markdown("---")

st.sidebar.header("Visual")
avatar = st.sidebar.selectbox('Choose avatar', options=AVATARS)
image_url = f'{AVATAR_PREFIX}/{avatar}.png'
st.sidebar.image(image_url, width=256)
st.sidebar.markdown("---")

st.sidebar.header("Voice")
voice_source = st.sidebar.selectbox('Voice source', options = ['Maika', 'Others'])

if voice_source == 'Maika':
    tts_kwargs = INTERNAL_VOICES[voice_source]

if voice_source == 'Others':
    language = st.sidebar.selectbox('Language', LANG_MAP.keys())
    voice_gender = st.sidebar.selectbox('Voice gender', GENDERS)
    voice_name = st.sidebar.text_input(
        """Voice name (choose from [this](https://cloud.google.com/text-to-speech/docs/voices), read NOTE in the right!)""", 
    )

    
    tts_kwargs = dict(
        language = LANG_MAP[language],
        voice_gender = voice_gender,
        voice_name = voice_name
    ) 

    st.markdown(f"NOTE: Choose any voicename having **Language code** = `{LANG_MAP[language]}`, **SSML Gender** = `{voice_gender}`")
    

st.sidebar.markdown('---')
st.sidebar.header('Output options')

resize_choice = st.sidebar.radio(
    "Resize option", 
    RESIZE_CHOICES,
    1
)


if resize_choice == OPTIMAL:
    target_size = st.sidebar.number_input('Size (100 - 512)', 100, 512)
    size_kwargs = dict(
        target_size = target_size
    )

elif resize_choice == BY_WIDTH:
    target_width = st.sidebar.number_input('Width (100 - 512)', 100, 512)
    size_kwargs = dict(
        target_width = target_width,
    )

elif resize_choice == BY_HEIGHT:
    target_height = st.sidebar.number_input('Height (100 - 512)', 100, 512)
    size_kwargs = dict(
        target_height = target_height
    )

elif resize_choice == BY_WIDTH_HEIGHT:
    target_width = st.sidebar.number_input('Width (100 - 512)', 100, 512)
    target_height = st.sidebar.number_input('Height (100 - 512)', 100, 512)
    size_kwargs = dict(
        target_width = target_width,
        target_height = target_height
    )

else:
    size_kwargs = dict()

use_enhancer = st.sidebar.checkbox('Use video enhancer (x8 slower)', value=False)

if st.sidebar.button("Render!"):
    # app_state = st.experimental_get_qu/ery_params()

    if "animator" in st.session_state:
        animator = st.session_state['animator']
        args = dict(
            text=text,
            driving_style = 'default',
            image_url = image_url,
            use_enhancer = use_enhancer,
            **tts_kwargs, 
            **size_kwargs
        )
        resp = animator.run(args)

        video_data = io.BytesIO()

        for chunk in resp:
            video_data.write(chunk)
        
        st.video(video_data)

    else:
        st.markdown("Try **Authorize** again!")


# MAIN PAGE


