from locust import HttpLocust, TaskSequence, seq_task, between
from locust.clients import HttpSession


def status(l):
    l.client.get("/status")


def upload(l):
    l.client.post("/data/upload", {"contentType": "image/png", "images": []})


class ScenarioTask(TaskSequence):

    @seq_task(1)
    def status(self):
        status(self)

    @seq_task(2)
    def item_list(self):
        item_list(self)

    @seq_task(2)
    def add_item(self):
        add_item(self)

class WebsiteUser(HttpLocust):
    task_set = ScenarioTask

    wait_time = between(1.0, 3.0)
