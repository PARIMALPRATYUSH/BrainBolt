import requests
import uuid

BASE_URL = "http://localhost:8000/v1"
USER_ID = "integrity-test-user"

def test_integrity_error():
    print(f"1. Getting question for {USER_ID}...")
    resp = requests.get(f"{BASE_URL}/quiz/next", params={"userId": USER_ID})
    assert resp.status_code == 200, f"Failed to get question: {resp.text}"
    data = resp.json()
    question_id = data['questionId']
    print(f"   Got Question: {question_id}")

    print("2. Submitting answer (First time)...")
    payload = {
        "userId": USER_ID,
        "questionId": question_id,
        "answer": "Answer",
        "idempotencyKey": str(uuid.uuid4())
    }
    resp = requests.post(f"{BASE_URL}/quiz/answer", json=payload)
    if resp.status_code != 200:
        print(f"   Warning: First submission failed: {resp.status_code} {resp.text}")
        # It might fail if I already ran this test manually. 
        # But let's assume it succeeds or fails with 400 (Question already answered).
    else:
        print("   Success.")

    print("3. Submitting answer (Duplicate)...")
    # Use different idempotency key to bypass redis check and hit DB
    payload["idempotencyKey"] = str(uuid.uuid4())
    resp = requests.post(f"{BASE_URL}/quiz/answer", json=payload)
    
    print(f"   Status Code: {resp.status_code}")
    print(f"   Response: {resp.text}")
    
    if resp.status_code == 400 and "Question already answered" in resp.text:
        print("✅ SUCCESS: Caught IntegrityError and returned 400.")
    elif resp.status_code == 500:
        print("❌ FAILED: Internal Server Error (Likely NameError).")
        exit(1)
    else:
        print(f"❌ UNEXPECTED: {resp.status_code}")
        exit(1)

if __name__ == "__main__":
    try:
        test_integrity_error()
    except Exception as e:
        print(f"❌ Error: {e}")
        exit(1)
