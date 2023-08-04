from locust import HttpUser, task

class ListWorkspace(HttpUser):
    @task
    def post_detail(self):
        headers = {
        "accept": "application/json",
        "X-CSRFToken": "8oIHbFfZ0RBDafR2u23cYFcxQQG3f3tnpVm0O7JBwn8oNOkW39v83Ds4JRxIYq8Z"
        }
        self.client.get(url="workflow/workspace", headers=headers)