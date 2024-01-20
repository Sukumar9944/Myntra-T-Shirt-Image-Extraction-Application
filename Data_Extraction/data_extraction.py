from Data_Extraction.web_scraper import extract_data_by_pages
import pandas as pd


roadster_url = "https://www.myntra.com/men-tshirts?f=Brand%3ARoadster"

roadster_data = extract_data_by_pages(roadster_url, pages=4)

df = pd.DataFrame(data=roadster_data)
print(df.shape)

df.to_csv(
    r"F:\GUVI_DATA_SCIENCE\Project\Myntra-T-Shirt-Image-Extraction-Application\Datasets\roadster.csv",
    index=False,
)

"------------------------------------------------------------------------------------------------------------------------------------"

frisker_url = "https://www.myntra.com/men-tshirts?f=Brand%3AFriskers"

frisker_data = extract_data_by_pages(frisker_url, pages=4)

df = pd.DataFrame(data=frisker_data)
print(df.shape)

df.to_csv(
    r"F:\GUVI_DATA_SCIENCE\Project\Myntra-T-Shirt-Image-Extraction-Application\Datasets\frisker.csv",
    index=False,
)

"------------------------------------------------------------------------------------------------------------------------------------"

hrx_url = "https://www.myntra.com/men-tshirts?f=Brand%3AHRX%20by%20Hrithik%20Roshan"

hrx_data = extract_data_by_pages(hrx_url, pages=4)

df = pd.DataFrame(data=hrx_data)
print(df.shape)

df.to_csv(
    r"F:\GUVI_DATA_SCIENCE\Project\Myntra-T-Shirt-Image-Extraction-Application\Datasets\hrx.csv",
    index=False,
)

"------------------------------------------------------------------------------------------------------------------------------------"

wrogn_url = "https://www.myntra.com/men-tshirts?f=Brand%3AWROGN"

wrogn_data = extract_data_by_pages(wrogn_url, pages=4)

df = pd.DataFrame(data=wrogn_data)
print(df.shape)

df.to_csv(
    r"F:\GUVI_DATA_SCIENCE\Project\Myntra-T-Shirt-Image-Extraction-Application\Datasets\wrogn.csv",
    index=False,
)

"------------------------------------------------------------------------------------------------------------------------------------"

tommy_hilfiger_url = "https://www.myntra.com/men-tshirts?f=Brand%3ATommy%20Hilfiger"

tommy_hilfiger_data = extract_data_by_pages(tommy_hilfiger_url, pages=4)

df = pd.DataFrame(data=tommy_hilfiger_data)
print(df.shape)

df.to_csv(
    r"F:\GUVI_DATA_SCIENCE\Project\Myntra-T-Shirt-Image-Extraction-Application\Datasets\tommy_hilfiger.csv",
    index=False,
)

"------------------------------------------------------------------------------------------------------------------------------------"