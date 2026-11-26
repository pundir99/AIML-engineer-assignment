import easyocr
import json
import re

reader = easyocr.Reader(['en'])

# Your answer key
answer_key = {
    "1": "Machine learning allows computers to learn from data and make predictions without being explicitly programmed."
}

# Extract text from image
result = reader.readtext('answer.jpg.jpeg')

text = "\n".join([item[1] for item in result])

# Structure answers by question number
answers = {}
current_question = None

for line in text.split("\n"):
    match = re.search(r'Q\.?\s*(\d+)', line, re.IGNORECASE)

    if match:
        current_question = match.group(1)
        answers[current_question] = line[match.end():].strip()

    elif current_question:
        answers[current_question] += " " + line.strip()

# Score answers
output = []

for q_no, answer in answers.items():
    expected = answer_key.get(q_no, "")

    if expected and answer.lower() in expected.lower():
        score = 1
        confidence = "High"
        reason = "Answer closely matches the expected answer."
    else:
        score = 0
        confidence = "Low"
        reason = "Answer requires human review."

    output.append({
        "question_no": q_no,
        "extracted_answer": answer,
        "score": score,
        "expected_answer": expected,
        "confidence": confidence,
        "reason": reason
    })

# Save output
with open("output.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=4)

print("Evaluation completed. Check output.json")