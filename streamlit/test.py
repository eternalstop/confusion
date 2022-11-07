"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import pandas as pd
df = pd.DataFrame({
  '云厂商': ["腾讯云", "阿里云", "金山云", "华为云"],
  '账号业务名称': ["腾讯云大陆账号", "阿里云大陆账号", "金山云大陆账号", "华为云大陆账号"],
  '账号名': ["game-cloud@komoelive.com", "bilicloud@bilibili.com", "2597674310@qq.com", "bilicloud"],
  '账号ID': ["2597674310", "1946641698389315", "2000060040", "a20d492ef25141a0874edadc7d5fb5e9"],
  '账号主体': ["BILIBILI", "BILIBILI", "BILIBILI", "BILIBILI"],
  '覆盖区域': ["中国大陆", "中国大陆", "中国大陆", "中国大陆"]
})

st.table(df)
# st.dataframe(df, 900, 300)