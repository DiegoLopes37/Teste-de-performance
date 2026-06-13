from locust import HttpUser, task, between

class OrangeHRMUser(HttpUser):

    wait_time = between(1, 3)

    def on_start(self):
        self.login()

    def login(self):

        payload = {
            "username": "Admin",
            "password": "admin123"
        }

        self.client.post(
            "/web/index.php/auth/validate",
            data=payload,
            name="POST Login"
        )

    @task(5)
    def dashboard(self):

        self.client.get(
            "/web/index.php/dashboard/index",
            name="GET Dashboard"
        )

    @task(4)
    def employee_list(self):

        self.client.get(
            "/web/index.php/pim/viewEmployeeList",
            name="GET Employee List"
        )

    @task(3)
    def directory(self):

        self.client.get(
            "/web/index.php/directory/viewDirectory",
            name="GET Directory"
        )

    @task(2)
    def search_employee(self):

        payload = {
            "employee_name": "a"
        }

        self.client.post(
            "/web/index.php/pim/searchEmployee",
            data=payload,
            name="POST Search Employee"
        )

    @task(1)
    def update_employee(self):

        payload = {
            "firstName": "Teste"
        }

        self.client.post(
            "/web/index.php/pim/saveEmployee",
            data=payload,
            name="POST Update Employee"
        )