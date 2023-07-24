import requests
from bs4 import BeautifulSoup
# websites = (
#     "google.com",
#     "airbnb.com",
#     "https://twitter.com",
#     "facebook.com",
#     "https://tiktok.com"
# )
# results = {

# }

# for website in websites:
#     if not website.startswith("https://"):
#         website = f"https://{website}"
#     response = requests.get(website)
#     if response.status_code == 200:
#         results[website] = "OK"
#     else:
#         results[website] = "FAILED"

# print(results)


      

# # # string.startswith() -> boolean 값을 줌

basic_url = "https://www.youtube.com/results?search_query="
search_keyword = input("찾으려는 키워드: ")

response = requests.get(f"{basic_url}{search_keyword}")
if response.status_code != 200:
    print("Can't requests website")
else:
    print(response.text)