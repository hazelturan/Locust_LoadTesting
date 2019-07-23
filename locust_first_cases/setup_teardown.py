from locust import Locust, TaskSet, task


class MyTaskSet(TaskSet):

    def on_start(self):
        print("on_start blogundayım")

    def on_stop(self):
        print("on_stop blogundayım")

    @task(1)
    def my_task(self):
        print("executing my_task")

    @task(1)
    def my_other_task(self):
        print("executing my_other_task")


class MyLocust(Locust):
    task_set = MyTaskSet
    min_wait = 1000
    max_wait = 2000

    def setup(self):
        print("setup kod bloğundayım")

    def teardown(self):
        print("teardown kod bloğundayım")

# 1. Locust setup
# 2. TaskSet setup
# 3. TaskSet on_start
# 4. TaskSet tasks…
# 5. TaskSet on_stop
# 6. TaskSet teardown
# 7. Locust teardown
