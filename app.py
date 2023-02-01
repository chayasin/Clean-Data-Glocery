from re import search
import streamlit as st
import pandas as pd
import openpyxl

# Setpu stremlit
st.set_page_config(layout="wide")

# Import data, Clean Data
fk_dat = pd.read_excel('Freshket_complete.xlsx')
mk_dat = pd.read_csv('Makroclick_complete.csv')

fk_dat = fk_dat[['ProductName', 'Volumn', 'FullPrice','CurrentPrice']]
mk_dat = mk_dat[['ITEMNAME','FULLPRICE','DISCOUNT', 'UNITPRICE']]
mk_dat.columns = ['ProductName', 'FullPrice', 'CurrentPrice', 'UnitPrice']
mk_dat = mk_dat[mk_dat['ProductName'].notna()]

# App
st.header("Items")

# cat_list = ('เนื้อสัตว์','ผักผลไม้')
# cat = st.selectbox(label="Category",)

keyword = st.text_input(label="ชื่อสินค้า")

search_string = r"^"
for word in keyword.split(' '):
    search_string = search_string + r'(?=.*' + word + r')'

print(search_string)
keyword = search_string
# keyword = keyword.replace(' ','|')

fk_ = fk_dat[fk_dat['ProductName'].str.contains(keyword)]
mk_ = mk_dat[mk_dat['ProductName'].str.contains(keyword)]

# volumn = st.text_input(label="ปริมาณ")
# fk_ = fk_[fk_['Volumn'].str.contains(volumn)]
# mk_ = mk_[mk_['ProductName'].str.contains(volumn)]

col1, col2 = st.columns(2)

with col1:
    st.header("Freshket")
    st.dataframe(fk_)
    
with col2:
    st.header("Makroclick")
    st.dataframe(mk_)
    