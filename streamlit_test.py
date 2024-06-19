import streamlit as st
from PIL import Image

st.title('Hi')
st.header('My love')
st.sidebar.header('Log in')
user_id = st.sidebar.text_input('아이디 입력', value='', max_chars=15)
user_password = st.sidebar.text_input('패스워드 입력', value='', type='password')

if user_id == 'violetta' and user_password == '1234':
    st.sidebar.header('그림 목록')
    options = ['', '진주 귀걸이를 한 소녀', '별이 빛나는 밤', '절규', '생명의 나무', '월하정인']
    user_opt = st.sidebar.selectbox('좋아하는 작품은?', options, index=0)
    st.sidebar.write('**선택한 그림은', user_opt)

    # 메인 화면
    st.subheader('How are you?')
    image_files = ['0.png', 'b.png', 'c.png', 'e.png', 'a.jpg', 'd.png']
    sel_index = options.index(user_opt)
    
    # Ensure a valid image file is selected
    if sel_index > 0:  # Skip the first empty option
        img_file = image_files[sel_index]
        try:
            image_local = Image.open(f'{img_file}')
            st.image(image_local, caption=user_opt)
        except FileNotFoundError:
            st.error(f'Image file {img_file} not found.')
else:
    st.error('Invalid user ID or password.')
