import base64
from locust import HttpLocust, TaskSequence, seq_task, between
from locust.clients import HttpSession


def create_imageb64():
    with open("test.png", "rb") as image_binary:
        return base64.b64encode(image_binary.read()).decode("utf-8")


def status(l):
    l.client.get("/status")


def upload(l, image):
    print(image)
    response = l.client.post("/data/upload", {"contentType": "image/png", "images": [image]})
    print(response.text)

def convert(l, image):
    l.client.post("/convert/pdf")


class ScenarioTask(TaskSequence):

    def on_start(self):
        self.image = create_imageb64()

    @seq_task(1)
    def status(self):
        status(self)

    @seq_task(2)
    def upload(self):
        upload(self, self.image)


class WebsiteUser(HttpLocust):
    task_set = ScenarioTask

    wait_time = between(1.0, 3.0)
