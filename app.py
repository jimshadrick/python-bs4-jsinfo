from bs4 import BeautifulSoup
import requests

url = "https://javascript.info/"
result = requests.get(url)

soup = BeautifulSoup(result.text, "html.parser")
# print(soup.prettify())

data = {}

"""
We use the .find_all() method instead of .find() to find all the <div class="list-sub__title"> elements 
within the sibling <ul>. We then iterate over each subtitle <div> and extract the text using a list comprehension.
Finally, we store the list of subtitles as the value for each title in the data dictionary.
"""
for title_div in soup.find_all("div", class_="list__title"):
    title = title_div.get_text(strip=True)
    subtitle_divs = title_div.find_next_sibling("ul").find_all(
        "div", class_="list-sub__title"
    )
    subtitles = [subtitle.get_text(strip=True) for subtitle in subtitle_divs]
    data[title] = subtitles

# print(data)

# Loop through the data and print out the topics and subtopics
for key in data:
    print(f"{key}:")
    for item in data[key]:
        print(f"- {item}")
    print()
