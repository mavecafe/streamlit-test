from operator import index
from turtle import right
from winreg import ExpandEnvironmentStrings
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time



st.title('テストサイト')

st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'もうすぐ表示されます{i+1}')
    bar.progress(i+1)
    time.sleep(0.05)



if st.checkbox('Show Image'):
    img = Image.open('aaa/1015602351.jpg')
    st.image(img, caption='ぬれまん',use_column_width=True)


audio_file = open('tamco03v.ogg','rb')
audio_bytes = audio_file.read()
st.audio(audio_bytes,format='audio/ogg')

video_file = open('test.mp4','rb')
video_bytes = video_file.read()
st.video(video_bytes)


option = st.selectbox(
    'あなたの好きな数字を教えてください',
    list(range(1,11))
)
'あなたの好きな数字は',option, 'です。'

left_column,right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')



expander = st.beta_expander('問い合わせ')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')
expander.write('問い合わせ内容を書く')




#サイドバーで表示
condition = st.sidebar.slider('いまのあなたの調子は',0,50,100)
st.sidebar.write('コンディション', condition)


st.write('DataFrame')


df = pd.DataFrame({
    '都道府県':['東京都','千葉県','神奈川県','埼玉県'],
    'lat':[1,2,3,4],
    'lot':[10,20,30,40]
})

#st.write(df)


#df = pd.DataFrame(
#    '都道府県':['東京都','千葉県','神奈川県','埼玉県'],
#    'lat':[1,2,3,4],
#    'lot':[10,20,30,40]
#)

st.dataframe(df.style.highlight_max(axis=0),width=250,height=200)

st.table(df.style.highlight_max(axis=0))






df = pd.DataFrame(
    np.random.rand(20,3),
    columns=['a','b','c']  
)
st.line_chart(df)





if st.checkbox('50行20列'):
    df = pd.DataFrame(
        np.random.randn(50, 20),
        columns=('col %d' % i for i in range(20)))
    st.table(df.style.highlight_max(axis=0))
    #st.dataframe(df)  # Same as st.write(df)


if st.checkbox('マンションデータ'):
    

    mrdata = pd.read_csv('20200806mr_data1.csv')
    st.table(mrdata)
    #st.Dataframme(mrdata) これだと読み込めない

"""
# 章
## 節
### 項

```
python
import streamlit as st/
import numpy as np/
import pandas as pd/
```

"""

a = st.text_input('入力してください','ここにどうぞ')
st.write(a)





select = st.selectbox("どちらが欲しい",["bigbox","smallbox"])

if st.button('open'):
    if select == 'bigbox':
        st.write('empty')
    else:
        st.write('teresure')
    

df = pd.DataFrame({
    'lat':[35.593063,35.6297363,35.5914658],
    'lon':[139.6776223,139.6898639,139.6688982]
    
})
st.map(df)




