# question_generator/quiz_generator.py
from nltk import word_tokenize, pos_tag
import random

class QuizGenerator:
    def __init__(self, text):
        self.text = text
        self.nouns = self.extract_nouns()

    def extract_nouns(self):
        tokens = word_tokenize(self.text)
        tagged = pos_tag(tokens)

        # Filter out words containing single quotes or hyphens
        nouns = [word for word, pos in tagged if pos in ['NN', 'NNP'] and "'" not in word and "-" not in word and "–" not in word and "’" not in word]

        return nouns

    def generate_mcq_type1(self):
        if len(self.nouns) >= 2:
            random.shuffle(self.nouns)
            question = f"What is the relationship between {self.nouns[0]} and {self.nouns[1]}?"
            answer = f"{self.nouns[0]} and {self.nouns[1]}"
            choices = [answer, f"No relationship", f"Opposite relationship", f"Unrelated"]
            random.shuffle(choices)
            return question, choices
        else:
            return "Not enough information to generate a question.", []

    def generate_mcq_type2(self):
        if len(self.nouns) >= 1:
            random.shuffle(self.nouns)
            question = f"What is the significance of {self.nouns[0]} in the context of the summary?"
            answer = f"{self.nouns[0]}"
            choices = [answer, f"Not significant", f"Negative significance", f"Unknown"]
            random.shuffle(choices)
            return question, choices
        else:
            return "Not enough information to generate a question.", []

    def generate_mcq_type3(self):
        if len(self.nouns) >= 1:
            random.shuffle(self.nouns)
            question = f"What are the key features of {self.nouns[0]} mentioned in the summary?"
            answer = f"{self.nouns[0]}"
            choices = [answer, f"No key features", f"Contradictory features", f"Miscellaneous features"]
            random.shuffle(choices)
            return question, choices
        else:
            return "Not enough information to generate a question.", []

    def generate_mcq_type4(self):
        if len(self.nouns) >= 1:
            random.shuffle(self.nouns)
            question = f"How does {self.nouns[0]} impact the overall theme of the summary?"
            answer = f"It contributes to the overall theme."
            choices = [answer, f"No impact on the theme", f"Negatively impacts the theme", f"Uncertain impact"]
            random.shuffle(choices)
            return question, choices
        else:
            return "Not enough information to generate a question.", []

    def generate_mcq_type5(self):
        if len(self.nouns) >= 2:
            random.shuffle(self.nouns)
            question = f"Compare and contrast {self.nouns[0]} and {self.nouns[1]} based on the summary."
            answer = f"{self.nouns[0]} and {self.nouns[1]} have both similarities and differences."
            choices = [answer, f"They are identical", f"They are completely different", f"Comparison not possible"]
            random.shuffle(choices)
            return question, choices
        else:
            return "Not enough information to generate a question.", []

    def generate_mcq_type6(self):
        if len(self.nouns) >= 1:
            random.shuffle(self.nouns)
            question = f"What is the role of {self.nouns[0]} in the events described in the summary?"
            answer = f"{self.nouns[0]} plays a significant role."
            choices = [answer, f"No role in the events", f"Negative role", f"Undefined role"]
            random.shuffle(choices)
            return question, choices
        else:
            return "Not enough information to generate a question.", []

    def generate_mcq_type7(self):
        if len(self.nouns) >= 1:
            random.shuffle(self.nouns)
            question = f"What is the main idea or concept associated with {self.nouns[0]} in the summary?"
            answer = f"{self.nouns[0]} represents the main idea or concept."
            choices = [answer, f"No main idea or concept", f"Contradictory ideas or concepts", f"Multiple ideas or concepts"]
            random.shuffle(choices)
            return question, choices
        else:
            return "Not enough information to generate a question.", []

    def generate_mcq_type8(self):
        if len(self.nouns) >= 1:
            random.shuffle(self.nouns)
            question = f"Explain the significance of {self.nouns[0]} based on the information in the summary."
            answer = f"{self.nouns[0]} is significant in the context of the summary."
            choices = [answer, f"Not significant", f"Negative significance", f"Unknown significance"]
            random.shuffle(choices)
            return question, choices
        else:
            return "Not enough information to generate a question.", []

    def generate_mcq_type9(self):
        if len(self.nouns) >= 1:
            random.shuffle(self.nouns)
            question = f"How does {self.nouns[0]} contribute to the central theme of the summary?"
            answer = f"{self.nouns[0]} contributes positively to the central theme."
            choices = [answer, f"No contribution to the theme", f"Negative contribution", f"Uncertain contribution"]
            random.shuffle(choices)
            return question, choices
        else:
            return "Not enough information to generate a question.", []

    def generate_mcq_type10(self):
        if len(self.nouns) >= 1:
            random.shuffle(self.nouns)
            question = f"What are some examples or instances of {self.nouns[0]} mentioned in the summary?"
            answer = f"{self.nouns[0]} is exemplified by specific instances in the summary."
            choices = [answer, f"No examples mentioned", f"Contradictory examples", f"Multiple examples"]
            random.shuffle(choices)
            return question, choices
        else:
            return "Not enough information to generate a question.", []


    def generate_all_questions(self):
        all_questions = []
        for i in range(1, 11):
            mcq_function = getattr(self, f"generate_mcq_type{i}", None)
            if mcq_function:
                question, choices = mcq_function()
                all_questions.append((question, choices))
            else:
                all_questions.append(("Invalid question type", []))
        return all_questions
