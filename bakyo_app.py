import streamlit as st
from bs4 import BeautifulSoup
import pandas as pd

# Streamlitアプリの設定
st.title('HTMLテキスト抽出とCSVダウンロード')

# ユーザーがHTMLコードを入力
html_code = st.text_area('HTMLコードを入力してください')

if html_code:
    # BeautifulSoupオブジェクトを作成
    soup = BeautifulSoup(html_code, 'html.parser')

    # テキストのみを抽出
    text_only = soup.get_text()

    # 文字列をスペースで分割
    elements = text_only.split()

    # ヘッダーとデータ部分に分割
    header = elements[:6]
    rows = [elements[i:i+7] for i in range(6, len(elements), 7)]

    # DataFrameを作成
    df = pd.DataFrame(rows, columns=header+ ["金額2"])

    # DataFrameを表示
    st.dataframe(df)

    # CSVファイルとしてダウンロード
    csv = df.to_csv(index=False, encoding='cp932', errors='ignore')
    st.download_button(label='CSVファイルをダウンロード', data=csv, file_name='data.csv', mime='text/csv')
