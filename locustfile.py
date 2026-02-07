from locust import HttpUser, task, between
import uuid
import random

class QuizUser(HttpUser):
    wait_time = between(1, 3)
    user_id = None
    current_question_id = None

    def on_start(self):
        self.user_id = str(uuid.uuid4())

    @task(3)
    def get_next_question(self):
        url = "/v1/quiz/next"
        if self.user_id:
            url += f"?userId={self.user_id}"
        
        with self.client.get(url, catch_response=True) as response:
            if response.status_code == 200:
                data = response.json()
                self.user_id = data["userId"]
                self.current_question_id = data["questionId"]
            else:
                response.failure(f"Failed to get question: {response.status_code}")

    @task(5)
    def submit_answer(self):
        if not self.user_id or not self.current_question_id:
            self.get_next_question()
            return
            
        # Random answer from valid choices? Logic in static list is mostly numeric or text.
        # Just sending a dummy answer to test load, keeping some correct to test scoring.
        # "4" is correct for q1.
        answers = ["4", "Paris", "100C", "WrongAnswer"]
        answer = random.choice(answers)
        
        payload = {
            "userId": self.user_id,
            "questionId": self.current_question_id,
            "answer": answer,
            "idempotencyKey": str(uuid.uuid4())
        }
        
        self.client.post("/v1/quiz/answer", json=payload)

    @task(1)
    def view_leaderboard(self):
        self.client.get("/v1/leaderboard/score")
        self.client.get("/v1/leaderboard/streak")
        
    @task(1)
    def view_metrics(self):
        if self.user_id:
            self.client.get(f"/v1/quiz/metrics/{self.user_id}")
