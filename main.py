import requests
from bs4 import BeautifulSoup
from requests.exceptions import HTTPError, RequestException

url = input("Enter the URL of the website: ")

try:
    response = requests.get(url)
    response.raise_for_status()  # Raises an error for bad responses

    html = response.text
    print("HTML content retrieved successfully.")

    # Parsing the HTML content with BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())

    ask = input("Do you want titles too? (yes/no): ").strip().lower()
    if ask == "yes":
        titles = soup.find_all(['h1', 'h2', 'h3'])
        for title in titles:
            print(title.get_text(strip=True))
    else:
        print("Okay")

except HTTPError as http_err:
    print(f"HTTP error occurred: {http_err}")
except RequestException as req_err:
    print(f"Error: The entered URL is not valid or there was an issue retrieving the content: {req_err}")
except Exception as err:
    print(f"An unexpected error occurred: {err}")
