import streamlit as st
import pandas as pd
from image_processing.image_processor import view_image, download_image

# Setting Webpage Configurations
st.set_page_config(page_icon="🛒",page_title="Myntra Explorer", layout="wide")

st.title(':green[Myntra Product Explorer 🌎]')

df = pd.read_csv(r'F:\GUVI_DATA_SCIENCE\Project\Myntra-T-Shirt-Image-Extraction-Application\Datasets\myntra_processed_dataset.csv')

select_brand = st.selectbox('Select a Brand', df['brand'].unique())

brand_df = df.query(f'brand == "{select_brand}"')

col1, col2 = st.columns(2)

with col1:
    min_price = st.number_input(f'Select your minimum price range (Rs. {brand_df["original_price(Rs)"].min()})', min_value = 1)

with col2:
    max_price = st.number_input(f'Select your maximum price range (Rs. {brand_df["original_price(Rs)"].max()})', min_value = 1000 )

price_df = brand_df.query(f'`original_price(Rs)` >= {min_price} and `original_price(Rs)` <= {max_price}')

image_urls = price_df['image_url']

select_image = st.number_input('Browse Image', min_value = 1, max_value = len(image_urls))

try:
    product_image = view_image(image_urls[select_image - 1])
    st.image(product_image)

    info_df = price_df[['brand', 'description', 'overall_rating', 'rating_count', 'original_price(Rs)', 'discount_price(Rs)', 'offer_percentage(%)']]

    info_df = info_df.astype(str)

    query_info_df = info_df.loc[select_image - 1]

    st.download_button('Download_Image', data = download_image(image_urls[select_image - 1]), file_name = f'image{select_image}.jpg')

    st.dataframe(query_info_df, width = 1200)

except:
    st.warning('Please Check your Internet connection 🌐')