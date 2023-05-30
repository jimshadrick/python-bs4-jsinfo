from bs4 import BeautifulSoup

html = """
<div class="list__item">
    <div class="list__title">
        <a class="list__link" href="/generators-iterators">
            Generators, advanced iteration
        </a>
    </div>
    <ul class="list-sub">
        <li class="list-sub__item">
            <div class="list-sub__title">
                <a class="list-sub__link" href="/generators">
                    Generators
                </a>
            </div>
        </li>
        <li class="list-sub__item">
            <div class="list-sub__title">
                <a class="list-sub__link" href="/async-iterators-generators">
                    Async iteration and generators
                </a>
            </div>
        </li>
    </ul>
</div>
"""

soup = BeautifulSoup(html, "html.parser")

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

print(data)

""" Results:
{
    'Generators, advanced iteration': ['Generators', 'Async iteration and generators']
}
"""

# Loop through the data and print out the topics and subtopics
for key in data:
    print(f"{key}:")
    for item in data[key]:
        print(f"- {item}")
    print()

""" Results:
Generators, advanced iteration:
- Generators
- Async iteration and generators
"""
