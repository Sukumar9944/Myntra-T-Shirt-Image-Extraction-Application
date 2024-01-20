from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

# To prevent the browser from closing automatically
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

# Define a Driver
driver = webdriver.Chrome(options=options)

# To maximize the window
driver.maximize_window()

product_data = []

def extract_data(url):
    
    driver.get(url)

    time.sleep(10)

    print('Website URL Fetched')

    # Scroll down the page  
    scroll_locater = driver.find_element(By.TAG_NAME, 'body')

    for _ in range(8):
        scroll_locater.send_keys(Keys.PAGE_DOWN)
        time.sleep(3)

    time.sleep(5)

    print('Website loaded successfully')

    product_locater = driver.find_elements(By.CLASS_NAME, 'img-responsive')

    print('Extracting Data')

    for product in product_locater[:len(product_locater):2]:
        try:
            product.click()

            new_tab = driver.window_handles[1]
            driver.switch_to.window(new_tab)

            wait_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'image-grid-image')))

            brand = driver.find_element(By.CLASS_NAME, 'pdp-title')

            description = driver.find_element(By.CLASS_NAME, 'pdp-name')


            try:
                original_price = driver.find_element(By.CLASS_NAME, 'pdp-mrp')
            except:
                original_price = driver.find_element(By.CLASS_NAME, 'pdp-price')

        
            image_url_locater = driver.find_element(By.CLASS_NAME, 'image-grid-image')
            image_src = image_url_locater.get_attribute('style')

            try:
                overall_rating = driver.find_element(By.CLASS_NAME, 'index-overallRating')
                overall_rating = overall_rating.text

            except NoSuchElementException:
                overall_rating = 'Nil'


            try:
                rating_count = driver.find_element(By.CLASS_NAME, 'index-ratingsCount')
                rating_count = rating_count.text

            except NoSuchElementException:
                rating_count = 'Nil'


            try:
                discount_price = driver.find_element(By.CLASS_NAME, 'pdp-price')
                discount_price = discount_price.text

            except NoSuchElementException:
                discount_price = 'Nil'


            try:
                offer_percentage = driver.find_element(By.CLASS_NAME, 'pdp-discount')
                offer_percentage = offer_percentage.text

            except NoSuchElementException:
                offer_percentage = 'Nil'


            data_dict = {'brand': brand.text,
                        'desc': description.text,
                        'overall_rating': overall_rating,
                        'rating_count': rating_count,
                        'original_price': original_price.text,
                        'discount_price': discount_price,
                        'offer_percentage': offer_percentage,
                        'image_url': image_src}
            
            product_data.append(data_dict)

            driver.close()

            main_tab = driver.window_handles[0]
            driver.switch_to.window(main_tab)

            wait_element_1 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'img-responsive')))
        
        except:
            print('Error Handled')
            pass

    return product_data
    


def extract_data_by_pages(url, pages):
    for i in range(pages):
        current_url = url
        extract_data(current_url)

        time.sleep(10)

        # Navigate to the next page
        next_page = driver.find_element(By.CLASS_NAME, 'pagination-next')
        next_page.click()

        url = driver.current_url

        time.sleep(5)

        print(f'Data extracted Successfully from Page : {i+1}')

    driver.close()

    return product_data