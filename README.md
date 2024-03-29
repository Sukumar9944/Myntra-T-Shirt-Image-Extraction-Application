# Myntra Image Extraction Application

## Overview

This Streamlit application allows users to  extract and explore images of T-shirts from Myntra. The process involves scraping data from the Myntra website using Selenium, followed by preprocessing the data and creating an interactive application with Streamlit. Users can browse through the images, view additional information, and download the images directly from the application.

## Features

- **Data Scraping**: The application uses Selenium for data scraping from the Myntra website to gather information about T-shirts, including brand, description, ratings, original price, discount price, and offer percentage.

- **Data Preprocessing**: The scraped data is preprocessed to create a clean dataset, which is then used to power the Streamlit application.

- **Interactive Image Viewer**: Users can select a brand, set a price range, and browse through the extracted images. The selected image is displayed in the app along with relevant information.

- **Download Image**: Users can download the currently displayed image with a single click using the "Download Image" button.

![Untitledvideo-MadewithClipchamp5-ezgif com-video-to-gif-converter (2)](https://github.com/Sukumar9944/Myntra-T-Shirt-Image-Extraction-Application/assets/132226144/4b9d9b0d-74f0-4bc3-9a6a-0441f93433cc)

## Prerequisites

- Install required Python packages using `pip install -r requirements.txt`

## How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/myntra-image-extraction.git
   ```

2. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

3. Open your browser and navigate to http://localhost:8501 to access the application.

## Usage
- Select a brand from the dropdown menu.
- Set your preferred price range using the number input fields.
- Browse through the images using the number input for image selection.
- View detailed information about the selected image.
- Download the displayed image with the "Download Image" button.

## Note
Ensure that you have a stable internet connection during the usage of the application

## License
This project is licensed under the MIT License - see the LICENSE file for details.

