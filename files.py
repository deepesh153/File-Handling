import streamlit as st
import pandas as pd

st.subheader('Uploading the csv File')
df = st.file_uploader('Upload the csv file:',type=['csv','xlsx'])

st.subheader('Loading the csv File')
df = pd.read_csv('February.csv')
st.table(df)
df = pd.read_csv('April.csv')
st.table(df)
df = pd.read_excel('PowerBIData.xlsx')
if df is not None:
 st.table(df.head())# head shows first 5 data as a demo
# df = pd.read_excel('PowerBIData.xlsx')
# st.table(df)#directly uploading

st.subheader("Working with Images directly")
st.image("C:/Users/ACT/Desktop/juypter/Streamlit/Please stayy.jpeg")# in the path '\' is used we have to replace it with '/'

st.subheader('Working with Images while uploading')
img_file = st.file_uploader('Upload the Image file:',type=['jpg','jpeg','png'])
if img_file is not None:
 st.image(img_file)

 st.subheader('Working with Videos directly')
 st.video("C:/Users/ACT/Desktop/juypter/Streamlit/zara Zara.mp4")

 st.subheader('Working with Videos while uploading')
 video_file = st.file_uploader("C:/Users/ACT/Desktop/juypter/Streamlit/zara Zara.mp4",type=['mp4','mkv','hevc'])
 if video_file is not None:
  st.video(video_file,start_time=0)

st.subheader('Working with songs')
audio_file =st.file_uploader("C:/Users/ACT/Desktop/juypter/Streamlit/Valam - Made in China.mp3")
if audio_file is not None:
 st.audio(audio_file.read())