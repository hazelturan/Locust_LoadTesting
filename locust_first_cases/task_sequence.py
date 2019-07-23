from locust import Locust, TaskSet, seq_task, TaskSequence


class MyTaskSequence(TaskSequence):
    @seq_task(1)
    def first_task(self):
        print("first")

    @seq_task(2)
    def second_task(self):
        print("second")

    @seq_task(3)
    def third_task(self):
        print("third")


class MyLocust(Locust):
    task_set = MyTaskSequence
    min_wait = 1000
    max_wait = 2000
