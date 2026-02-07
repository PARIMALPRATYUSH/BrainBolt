import requests
import uuid
import math

BASE_URL = "http://localhost:8000/v1"
USER_ID = f"logic-test-{uuid.uuid4()}"

def test_logic():
    print(f"Testing with User: {USER_ID}")
    
    # 1. Start - Diff should be 1.0
    print("\n--- Step 1: Initial State ---")
    resp = requests.get(f"{BASE_URL}/quiz/next", params={"userId": USER_ID})
    resp.raise_for_status()
    q_data = resp.json()
    print(f"Question Difficulty: {q_data['difficulty']}")
    assert q_data['difficulty'] == 1, f"Expected diff 1, got {q_data['difficulty']}"

    # 2. Correct Answer -> Diff should become 1.0 + (1/1.0) = 2.0
    print("\n--- Step 2: Correct Answer (Diff 1.0 -> 2.0) ---")
    question_id = q_data['questionId']
    prompt = q_data['prompt']
    
    # Lookup answer
    answers_all = {
        "What is 2 + 2?": "4",
        "Capital of France?": "Paris",
        "Elements in water?": "Hydrogen, Oxygen",
        "Color of the sky on a clear day?": "Blue",
        "How many legs does a spider have?": "8",
        # Diff 2 Qs
        "What is the boiling point of water?": "100C",
        "What is the square root of 64?": "8",
        "Highest mountain in the world?": "Everest",
        "HTTP status code for Not Found?": "404",
        "Which planet is known as the Red Planet?": "Mars"
    }
    
    ans = answers_all.get(prompt)
    if not ans:
        print(f"❌ Unknown question prompt: {prompt}")
        # Try to guess or skip? No, failure is better.
        return

    payload = {
        "userId": USER_ID,
        "questionId": question_id,
        "answer": ans,
        "idempotencyKey": str(uuid.uuid4())
    }
    resp = requests.post(f"{BASE_URL}/quiz/answer", json=payload)
    resp.raise_for_status()
    result = resp.json()
    
    new_diff = result['newDifficulty']
    print(f"New Difficulty: {new_diff}")
    
    # Expected: 1.0 + (1/1.0) = 2.0
    assert abs(new_diff - 2.0) < 0.01, f"Expected 2.0, got {new_diff}"
    
    # 3. Verify next question is from Difficulty 2 (floor(2.0) = 2)
    print("\n--- Step 3: Verify Next Question Difficulty ---")
    resp = requests.get(f"{BASE_URL}/quiz/next", params={"userId": USER_ID})
    q2_data = resp.json()
    print(f"Next Question Difficulty: {q2_data['difficulty']}")
    assert q2_data['difficulty'] == 2, f"Expected Question Diff 2, got {q2_data['difficulty']}"

    # 4. Correct Answer at Diff 2.0 -> 2.0 + (1/2.0) = 2.5
    print("\n--- Step 4: Correct Answer (Diff 2.0 -> 2.5) ---")
    prompt2 = q2_data['prompt']
    print(f"Question: {prompt2}")
    
    ans2 = answers_all.get(prompt2)
    if not ans2:
         print(f"❌ Unknown question prompt: {prompt2}")
         return

    payload2 = {
        "userId": USER_ID,
        "questionId": q2_data['questionId'],
        "answer": ans2,
        "idempotencyKey": str(uuid.uuid4())
    }
    resp = requests.post(f"{BASE_URL}/quiz/answer", json=payload2)
    result2 = resp.json()
    
    new_diff_2 = result2['newDifficulty']
    print(f"New Difficulty: {new_diff_2}")
    
    expected = 2.0 + (1.0/2.0) # 2.5
    assert abs(new_diff_2 - expected) < 0.01, f"Expected {expected}, got {new_diff_2}"

    # 5. Wrong Answer -> Decrease by 1/2.5 = 0.4 => 2.5 - 0.4 = 2.1
    print("\n--- Step 5: Wrong Answer (Diff 2.5 -> 2.1) ---")
    # Get next question (Diff 2, since floor(2.5)=2)
    resp = requests.get(f"{BASE_URL}/quiz/next", params={"userId": USER_ID})
    q3_data = resp.json()
    print(f"Next Question Difficulty: {q3_data['difficulty']}")
    assert q3_data['difficulty'] == 2, f"Expected Question Diff 2, got {q3_data['difficulty']}"
    
    # Submit wrong answer
    payload3 = {
        "userId": USER_ID,
        "questionId": q3_data['questionId'],
        "answer": "WRONG_ANSWER",
        "idempotencyKey": str(uuid.uuid4())
    }
    resp = requests.post(f"{BASE_URL}/quiz/answer", json=payload3)
    result3 = resp.json()
    
    new_diff_3 = result3['newDifficulty']
    print(f"New Difficulty: {new_diff_3}")
    
    # Expected: 2.5 - (1/floor(2.5)) = 2.5 - 0.5 = 2.0
    expected_dec = new_diff_2 - (1.0 / int(new_diff_2)) 
    assert abs(new_diff_3 - expected_dec) < 0.01, f"Expected {expected_dec}, got {new_diff_3}"
    
    print("\n✅ Logic Verified Successfully!")

if __name__ == "__main__":
    try:
        test_logic()
    except Exception as e:
        print(f"❌ Error: {e}")
        exit(1)
