from locust import HttpLocust, TaskSet, task
    class AdminLoadTest(TaskSet):
        def login(self):
            self.client.post("http://localhost:8088/users/login/",{"user_account": "admin", "password": "123456"})
　　    def logout(self):
        self.client.get("http://localhost:8088/users/logout/")
　　    def on_start(self):
            self.login()
　　    def on_stop(self):
            self.logout()
　　  @task
　　    def admin_index(self):
        self.client.get("http://localhost:8088/admin/")
    class RunLoadTests(HttpLocust):
　　  task_set = AdminLoadTest