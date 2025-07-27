import json
from datetime import datetime

def save_feedback(rule, comment):
    feedback_entry = {
        "rule": rule,
        "comment": comment,
        "timestamp": datetime.now().isoformat()
    }
    with open("outputs/feedback.json", "a") as f:
        f.write(json.dumps(feedback_entry) + "\n")
