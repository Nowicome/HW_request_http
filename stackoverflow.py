import requests
import datetime as dt


def join_strs(strs):
    return "".join(strs)


def get_url():
    """Automatically create link for questions of last 2 days"""
    base_url = "https://api.stackexchange.com/2.3/questions?fromdate="
    to_date = int(dt.datetime.now().timestamp())
    from_date = to_date - 172800
    end_url = "&order=desc&sort=activity&tagged=python&site=stackoverflow"
    url = join_strs([base_url, str(from_date), "&todate=", str(to_date), end_url])
    return url


def get_questions():
    response = requests.get(get_url()).json()
    questions = {}
    for i in response["items"]:
        questions[i["link"]] = i["title"]
    return questions
