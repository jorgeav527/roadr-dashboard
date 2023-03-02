from bs4 import BeautifulSoup
import requests


def get_instagram_followers():
    url_ins = "https://www.instagram.com/roadr/"
    response_ins = requests.get(url_ins)

    soup_ins = BeautifulSoup(response_ins.content, "html.parser")

    followers_count_ins = soup_ins.find("meta", attrs={"name": "description"}).get(
        "content"
    )
    _followers_count_ins = followers_count_ins.split("-")[0].strip()
    # followers = re.findall(r"\d+(?= Followers)", followers_count)[0]
    # following = re.findall(r"\d+(?= Following)", text)[0]
    # posts = re.findall(r"\d+(?= Posts)", text)[0]
    followers = int(_followers_count_ins.split()[0].replace(",", ""))
    return followers
