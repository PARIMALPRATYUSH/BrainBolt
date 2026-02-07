import requests
import uuid

BASE_URL = "http://localhost:8000/v1"
USER_ID = f"acc-test-{uuid.uuid4()}"

def test_accuracy():
    print(f"Testing Accuracy Map with User: {USER_ID}")
    
    # 1. First Question: Correct (100% -> 1.0x)
    print("\n--- Step 1: 100% Accuracy ---")
    resp = requests.get(f"{BASE_URL}/quiz/next", params={"userId": USER_ID})
    q1 = resp.json()
    prompt = q1['prompt']
    
    # Simple lookup
    answers = {
        "What is 2 + 2?": "4", "Capital of France?": "Paris", 
        "Elements in water?": "Hydrogen, Oxygen", "Color of the sky on a clear day?": "Blue",
        "How many legs does a spider have?": "8"
    }
    ans = answers.get(prompt)
    if not ans:
        print(f"Skipping unknown prompt: {prompt}")
        return

    payload = {
        "userId": USER_ID, "questionId": q1['questionId'], 
        "answer": ans, "idempotencyKey": str(uuid.uuid4())
    }
    resp = requests.post(f"{BASE_URL}/quiz/answer", json=payload)
    res = resp.json()
    
    # Base=10 * Diff(1) * Streak(1) * Acc(1.0) = 10
    score = res['scoreDelta']
    print(f"Score Delta: {score}")
    assert score == 10, f"Expected 10, got {score}"

    # 2. Second Question: Wrong (50% -> irrelevant for penalty, but sets up next step)
    print("\n--- Step 2: Wrong Answer ---")
    resp = requests.get(f"{BASE_URL}/quiz/next", params={"userId": USER_ID})
    q2 = resp.json()
    payload2 = {
        "userId": USER_ID, "questionId": q2['questionId'], 
        "answer": "WRONG", "idempotencyKey": str(uuid.uuid4())
    }
    resp = requests.post(f"{BASE_URL}/quiz/answer", json=payload2)
    res2 = resp.json()
    print(f"Score Delta (Penalty): {res2['scoreDelta']}")
    # 50% accuracy -> (1 - 0.5) * 20 = 10 penalty. So scoreDelta should be -10.
    assert res2['scoreDelta'] == -10, f"Expected -10, got {res2['scoreDelta']}"

    # 3. Third Question: Correct (2/3 = 66% -> 0.9x)
    print("\n--- Step 3: 66% Accuracy (Expect 0.9x) ---")
    resp = requests.get(f"{BASE_URL}/quiz/next", params={"userId": USER_ID})
    q3 = resp.json()
    # Diff logic: 1.0 -> 2.0 -> (2.0 - 1/2.0 = 1.5). Floor(1.5)=1.
    # So Difficulty is still 1.
    
    prompt3 = q3['prompt']
    ans3 = answers.get(prompt3)
    if not ans3:
        print(f"Skipping unknown prompt: {prompt3}")
        return

    payload3 = {
        "userId": USER_ID, "questionId": q3['questionId'], 
        "answer": ans3, "idempotencyKey": str(uuid.uuid4())
    }
    resp = requests.post(f"{BASE_URL}/quiz/answer", json=payload3)
    res3 = resp.json()
    
    score3 = res3['scoreDelta']
    # Base=10 * Diff(1) * Streak(1) * Acc(0.9) = 9
    print(f"Score Delta: {score3}")
    assert score3 == 9, f"Expected 9, got {score3}"

    print("\n✅ Accuracy Verified!")

if __name__ == "__main__":
    try:
        test_accuracy()
    except Exception as e:
        print(f"❌ Error: {e}")
        exit(1)
