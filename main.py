# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# import time
# import os

# # Define Chrome options to disable notifications
# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications": 2}
# chrome_options.add_experimental_option("prefs", prefs)

# # Specify the path to the ChromeDriver
# service = Service('C:/Users/lenovo/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')

# # Initialize the ChromeDriver with the Service object
# driver = webdriver.Chrome(service=service, options=chrome_options)

# # Open Facebook
# driver.get("http://www.facebook.com")

# # Target username and password fields
# username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
# password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

# # Enter login details
# username.clear()
# username.send_keys("gphackathon")  # Replace with your username
# password.clear()
# password.send_keys("gphackathon@123")  # Replace with your password

# # Target the login button and click it
# login_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
# login_button.click()

# # Wait for login to complete
# time.sleep(5)

# # Define the hashtag you want to search
# hashtag = "tesla"  # Replace with the hashtag you want to search

# # Search for the hashtag
# search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Search Facebook']")))
# search_box.clear()
# search_box.send_keys(f"#{hashtag}")  # Enter the hashtag
# search_box.send_keys(Keys.RETURN)

# # Wait for search results to load
# time.sleep(5)

# # Navigate to the hashtag's posts
# hashtag_url = f"https://www.facebook.com/hashtag/{hashtag}"
# driver.get(hashtag_url)
# time.sleep(5)

# # Initialize lists to store post content and image URLs
# posts = []
# images = []

# # Scroll down to load more posts
# for _ in range(5):  # Adjust the range to scroll more
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(5)

# # Collect posts and images
# post_elements = driver.find_elements(By.XPATH, "//div[@data-ad-preview='message']")  # Adjusted XPath based on the Facebook structure
# for post in post_elements:
#     try:
#         content = post.text  # Get the text content of the post
#         if content:  # Only append non-empty posts
#             posts.append(content)

#             # Find images within the post
#             img_elements = post.find_elements(By.TAG_NAME, 'img')
#             for img in img_elements:
#                 img_src = img.get_attribute('src')
#                 if img_src and img_src not in images:  # Avoid duplicates
#                     images.append(img_src)

#     except Exception as e:
#         print(f"Error extracting post content or images: {e}")

# # Debug output: Print collected posts and images to console
# print(f"Collected {len(posts)} posts and {len(images)} images.")
# for i, post in enumerate(posts):
#     print(f"Post {i + 1}: {post}\n")

# for i, img in enumerate(images):
#     print(f"Image {i + 1}: {img}\n")

# # Specify the folder path to store scraped data
# folder_name = "ScrapedData"
# folder_path = os.path.join(os.getcwd(), folder_name)

# # Create the folder if it doesn't exist
# if not os.path.exists(folder_path):
#     os.makedirs(folder_path)
#     print(f'Folder {folder_name} created successfully.')
# else:
#     print(f'Folder {folder_name} already exists.')

# # Save the collected posts into a text file
# file_path = os.path.join(folder_path, f"{hashtag}_posts.txt")
# with open(file_path, 'w', encoding='utf-8') as f:
#     for i, post in enumerate(posts):
#         f.write(f"Post {i + 1}: {post}\n\n")

# print(f'Scraped data saved to {file_path}')

# # Save image URLs into a text file
# images_file_path = os.path.join(folder_path, f"{hashtag}_images.txt")
# with open(images_file_path, 'w', encoding='utf-8') as f:
#     for i, img in enumerate(images):
#         f.write(f"Image {i + 1}: {img}\n")

# print(f'Image URLs saved to {images_file_path}')

# # Close the browser
# driver.close()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os

# Define Chrome options to disable notifications
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}
chrome_options.add_experimental_option("prefs", prefs)

# Specify the path to the ChromeDriver
service = Service('C:/Users/lenovo/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe')

# Initialize the ChromeDriver with the Service object
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open Facebook
driver.get("http://www.facebook.com")

# Target username and password fields
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

# Enter login details
username.clear()
username.send_keys("gphackathon")  # Replace with your username
password.clear()
password.send_keys("gphackathon@123")  # Replace with your password

# Target the login button and click it
login_button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
login_button.click()

# Wait for login to complete
time.sleep(5)

# Define hashtags and keywords specifically for illegal content, rumors, and seditious activity
hashtags = [
    "FakeNews", "Rumors", "IllegalContent", 
    "HateSpeech", "SeditiousActivity", "Disinformation", 
    "Goa", "India", "FakeNewsGoa", "RumorsGoa"
]

# Define keywords to identify specific content types
keywords = [
    "fake", "lie", "rumor", "hateful", "violent", 
    "illegal", "scam", "propaganda", "hoax", "disinformation", 
    "deceptive", "misleading", "extremist", "radical", "incitement", 
    "Goa", "India", "hate", "conspiracy", "crime", "fraud"
]

# Initialize lists to store post content and image URLs
posts = []
images = []

# Iterate through each hashtag and search
for hashtag in hashtags:
    # Search for the hashtag
    search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Search Facebook']")))
    search_box.clear()
    search_box.send_keys(f"#{hashtag}")  # Enter the hashtag
    search_box.send_keys(Keys.RETURN)

    # Wait for search results to load
    time.sleep(5)

    # Navigate to the hashtag's posts
    hashtag_url = f"https://www.facebook.com/hashtag/{hashtag}"
    driver.get(hashtag_url)
    time.sleep(5)

    # Scroll down to load more posts
    for _ in range(10):  # Increased number of scrolls for more posts
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)  # Wait time between scrolls

    # Collect posts and images
    post_elements = driver.find_elements(By.XPATH, "//div[@data-ad-preview='message' or @data-testid='post_message']")  # Adjusted XPath based on the Facebook structure
    for post in post_elements:
        try:
            content = post.text  # Get the text content of the post
            if content:  # Only append non-empty posts
                # Check if the content contains any of the keywords
                if any(keyword.lower() in content.lower() for keyword in keywords):
                    posts.append(content)

                    # Find images within the post
                    img_elements = post.find_elements(By.TAG_NAME, 'img')
                    for img in img_elements:
                        img_src = img.get_attribute('src')
                        if img_src and img_src not in images:  # Avoid duplicates
                            images.append(img_src)

        except Exception as e:
            print(f"Error extracting post content or images: {e}")

# Debug output: Print collected posts and images to console
print(f"Collected {len(posts)} posts and {len(images)} images.")
for i, post in enumerate(posts):
    print(f"Post {i + 1}: {post}\n")

for i, img in enumerate(images):
    print(f"Image {i + 1}: {img}\n")

# Specify the folder path to store scraped data
folder_name = "ScrapedData"
folder_path = os.path.join(os.getcwd(), folder_name)

# Create the folder if it doesn't exist
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
    print(f'Folder {folder_name} created successfully.')
else:
    print(f'Folder {folder_name} already exists.')

# Save the collected posts into a text file
file_path = os.path.join(folder_path, f"illegal_content_posts.txt")
with open(file_path, 'w', encoding='utf-8') as f:
    for i, post in enumerate(posts):
        f.write(f"Post {i + 1}: {post}\n\n")

print(f'Scraped data saved to {file_path}')

# Save image URLs into a text file
images_file_path = os.path.join(folder_path, f"illegal_content_images.txt")
with open(images_file_path, 'w', encoding='utf-8') as f:
    for i, img in enumerate(images):
        f.write(f"Image {i + 1}: {img}\n")

print(f'Image URLs saved to {images_file_path}')

# Close the browser
driver.close()
