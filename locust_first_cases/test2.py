from locust import Locust, TaskSet, task


class MyTaskSet(TaskSet):
    @task(2)
    def my_task(self):
        self.client.get("/")

    @task(1)
    def my_other_task(self):
        self.client.get("/butik/liste/kadin")


class MyLocust(Locust):
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 2000
