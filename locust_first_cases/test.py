from locust import HttpLocust, TaskSet


def get_homepage(l):
    response = l.client.get("/")
    print(response.status_code)
    print(response.content)


def get_woman_tab(l):
    l.client.get("/butik/liste/kadin")


class UserBehavior(TaskSet):
    tasks = {get_homepage: 2, get_woman_tab: 1}


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
    host = "https://www.trendyol.com"
