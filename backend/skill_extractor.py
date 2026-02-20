import json
import spacy
import re
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

with open("skills_db.json", "r") as f:
    SKILLS_DB = json.load(f)

matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

# normalize function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9+# ]', ' ', text)  # remove special chars
    text = text.replace("problem solving", "problem-solving")
    return text

# build patterns
for category in SKILLS_DB:
    for skill in SKILLS_DB[category]:
        matcher.add(skill, [nlp.make_doc(skill)])


def extract_skills(text):
    text = clean_text(text)
    doc = nlp(text)

    matches = matcher(doc)

    found_skills = set()

    for match_id, start, end in matches:
        found_skills.add(doc[start:end].text.lower())

    return sorted(list(found_skills))