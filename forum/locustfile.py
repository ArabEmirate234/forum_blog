from locust import HttpUser, task, between

class ForumUser(HttpUser):
    """
    Simulates a typical forum user behavior for load testing.
    """
    wait_time = between(1, 3)  

    def on_start(self):
        """
        Runs when a simulated user starts, simulates a login.
        """
        self.client.post("/login/", {"username": "testuser", "password": "password"})

    @task(1)
    def view_homepage(self):
        """
        Simulates viewing the homepage.
        """
        self.client.get("/")

    @task(2)
    def view_categories(self):
        """
        Simulates viewing the categories page.
        """
        self.client.get("/categories/")

    @task(3)
    def view_threads(self):
        """
        Simulates viewing threads in a category.
        """
        response = self.client.get("/threads/")
        if response.status_code == 200 and response.json():
            thread = response.json()[0]  
            self.client.get(f"/threads/{thread['id']}/")  

    @task(4)
    def like_post(self):
        """
        Simulates liking a post.
        """
        self.client.post("/posts/1/like/")  

    @task(5)
    def add_comment(self):
        """
        Simulates adding a comment to a thread.
        """
        self.client.post("/threads/1/add_comment/", {"content": "This is a test comment"}) 

    @task(2)
    def view_posts(self):
        """
        Simulates viewing the list of posts.
        """
        self.client.get("/posts/")

    @task(1)
    def logout(self):
        """
        Simulates a user logging out.
        """
        self.client.get("/logout/")
