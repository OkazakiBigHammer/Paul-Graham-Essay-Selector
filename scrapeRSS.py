from bs4 import BeautifulSoup
import requests
from feedgen.feed import FeedGenerator

# Step 1: Download the page
url = 'http://example.com'
response = requests.get(url)
html = response.text

# Step 2: Parse the page with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Step 3: Extract the information you're interested in
# This will depend on the structure of the website you're scraping
# For this example, we'll assume that each post is in a div with the class "post",
# and that the title and content of the post are in tags with the classes "title" and "content"
posts = soup.find_all('div', class_='post')

# Step 4: Create the RSS feed
fg = FeedGenerator()
fg.title('My RSS Feed')
fg.link(href='http://example.com', rel='alternate')
fg.description('An RSS feed of posts from example.com')

for post in posts:
    title = post.find('div', class_='title').text
    content = post.find('div', class_='content').text

    fe = fg.add_entry()
    fe.title(title)
    fe.content(content)

# Step 5: Write the RSS feed to a file
with open('feed.rss', 'w') as f:
    print(fg.rss_str(pretty=True).decode(), file=f)
