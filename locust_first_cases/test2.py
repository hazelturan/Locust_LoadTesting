from locust import Locust, TaskSet, task


class MyTaskSet(TaskSet):
    @task(2)
    def get_homepage(l):
        response = l.client.get("/")
        print(response.status_code)
        print(response.content)

    @task(1)
    def get_woman_tab(l):
        l.client.get("/butik/liste/kadin")


class MyLocust(Locust):
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 2000
