# AIML Engineer Assignment

## Project Overview
This project evaluates handwritten answer sheets using OCR and a basic answer-scoring pipeline.

## Technologies Used
- Python
- EasyOCR
- Regular Expressions
- JSON

## Pipeline
1. Extract text from answer sheet images.
2. Identify and structure answers by question number.
3. Compare extracted answers with an answer key.
4. Generate scores and confidence labels.
5. Save evaluation results in JSON format.

## How to Run
Install EasyOCR:

```bash
pip install easyocr
```

Run the program:

```bash
python main.py
```

## Output
The program generates `output.json` containing question numbers, extracted answers, expected answers, scores, confidence levels and reasons.

## Limitations
The current scoring method uses basic text matching. It may not evaluate semantically correct answers written differently. OCR accuracy may also vary with handwriting and image quality.

## Future Improvements
- Semantic answer scoring
- Better multi-page answer handling
- Improved handwriting recognition
- Confidence calibration and human review