from locust import HttpLocust, TaskSet


def index(l):
    response = l.client.get("/")
    print(response.status_code)
    print(response.content)


def profile(l):
    l.client.get("/butik/liste/kadin")


class UserBehavior(TaskSet):
    tasks = {index: 2, profile: 1}


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
    host = "https://www.trendyol.com"