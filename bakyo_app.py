import streamlit as st
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import time
import requests
from datetime import date, timedelta

# Streamlitアプリの設定
st.title('HTMLテキスト抽出とCSVダウンロード')

# ユーザーがHTMLコードを入力
html_code = st.text_area('HTMLコードを入力してください')

#@st.cache
def convert_df(df):
    # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv(index=False, header=False).encode("utf_8_sig")

dt_now_jst_aware = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))

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

    df["C1(コード)"] = df["コード"]
    df["C2"] = np.nan
    df["C3(市場)"] = "TKY"
    df["C4"] = np.nan
    df["C5"] = np.nan
    df["C6"] = np.nan
    df["C7"] = np.nan
    df["C8"] = np.nan

    df_= df[["C1(コード)","C2","C3(市場)","C4","C5","C6","C7","C8"]]
    
    # DataFrameを表示
    st.dataframe(df_)
    csv = convert_df(df_)

    st.download_button(
        label="SBIインポートリスト",
        data=csv,
        file_name=dt_now_jst_aware.strftime('%y%m%d')+'場況.csv',
        mime='text/csv',
    )
