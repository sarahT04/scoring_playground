from difflib import SequenceMatcher

def sanitize_string(string: str) -> str:
    # Lowercase the string, replace every whitespace with nothing, 
    return string.replace(' ', '').lower()

def answer_comparisor(answer: str, real_key: str) -> int:
    # Converts the ratio to be in percentage, then round it downwards.
    return round(SequenceMatcher(None, sanitize_string(answer), sanitize_string(real_key)).ratio() * 100)

def get_scores(real_key: str, answer_list: list, start=0) -> list[dict]:
    score_list = []
    for idx, answer in enumerate(answer_list, start=start):
        score = answer_comparisor(answer, real_key)
        score_list.append({
            "id": idx, 
            "key": real_key,
            "answer": answer,
            "score": score,
        })
    return score_list

def get_score(real_key: str, answer: str) -> dict:
    return {"id": 1, "score": answer_comparisor(answer, real_key), "answer": answer, "key": real_key}

# [{
#     "id": 1, 
#     "answer": 'My answer',
#     "score": 20,
# }]
