import streamlit as st
import pandas as pd

st.subheader('Uploading the csv File')
csv_file = st.file_uploader('Upload the csv file:',type=['csv'])

st.subheader('Loading the csv File')
df = pd.read_csv(csv_file)
if df is not None:
 st.table(df)
else :
 st.markdown('NONE')
df = pd.read_csv('February.csv')
st.table(df)
df = pd.read_csv('April.csv')
st.table(df)

st.subheader('Uploading the excel File')
df = st.file_uploader('Upload the excel file:',type=['xlsx'])
st.subheader('Loading the excel File')
excel_file = pd.read_excel('PowerBIData.xlsx')
if excel_file is not None:
 st.table(excel_file.head())# head shows first 5 data as a demo
df = pd.read_excel('PowerBIData.xlsx')
st.table(df)#directly uploading

st.subheader("Working with Images directly")
st.image("Please stayy.jpeg")# in the path '\' is used we have to replace it with '/'

st.subheader('Working with Images while uploading')
img_file = st.file_uploader('Upload the Image file:',type=['jpg','jpeg','png'])
if img_file is not None:
 st.image(img_file)

 st.subheader('Working with Videos directly')
 st.video("zara Zara.mp4")

 st.subheader('Working with Videos while uploading')
 video_file = st.file_uploader("zara Zara.mp4",type=['mp4','mkv','hevc'])
 if video_file is not None:
  st.video(video_file,start_time=0)

st.subheader('Working with songs')
audio_file =st.file_uploader("Valam - Made in China.mp3")
if audio_file is not None:
 st.audio(audio_file.read())
