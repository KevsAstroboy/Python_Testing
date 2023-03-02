from locust import HttpUser, task, between


class HelloWorldUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def index(self):
        self.client.get("/")
        # self.client.get("/world")

    @task
    def showsummary_with_good_email(self):
        from_data = {'email': 'john@simplylift.co'}
        self.client.post('/showSummary', data=from_data)

    @task
    def purchase_places_when_is_empty(self):
        from_data = {'places': ''}
        self.client.post('/purchasePlaces', data=from_data)

    @task
    def purchase_places_when_is_more_than_twelve(self):
        from_data = {'places': 12}
        self.client.post('/purchasePlaces', data=from_data)

    @task
    def booking_with_good_url(self):
        self.client.get('/book/Spring Festival/Simply Lift')
