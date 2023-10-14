from nltk import word_tokenize, pos_tag,sent_tokenize
import random

class QuestionGenerator:
    def __init__(self, text):
        self.text = text
        self.nouns = self.extract_nouns()

    def extract_nouns(self):
        tokens = word_tokenize(self.text)
        tagged = pos_tag(tokens)

        # Filter out words containing single quotes or hyphens
        nouns = [word for word, pos in tagged if pos in ['NN', 'NNP'] and "'" not in word and "-" not in word and "–" not in word and "’" not in word]

        return nouns

    def generate_question_type1(self):
        if len(self.nouns) >= 2:
            random.shuffle(self.nouns)
            question = f"What is the relationship between {self.nouns[0]} and {self.nouns[1]}?"
            return question
        else:
            return "Not enough information to generate a question."

    def generate_question_type2(self):
        if len(self.nouns) >= 1:
            random.shuffle(self.nouns)
            question = f"What is the significance of {self.nouns[0]} in the context of the summary?"
            return question
        else:
            return "Not enough information to generate a question."

    def generate_question_type3(self):
        if len(self.nouns) >= 1:
            random.shuffle(self.nouns)
            question = f"What are the key features of {self.nouns[0]} mentioned in the summary?"
            return question
        else:
            return "Not enough information to generate a question."

    def generate_question_type4(self):
        if len(self.nouns) >= 1:
            random.shuffle(self.nouns)
            question = f"How does {self.nouns[0]} impact the overall theme of the summary?"
            return question
        else:
            return "Not enough information to generate a question."

    def generate_question_type5(self):
        if len(self.nouns) >= 2:
            random.shuffle(self.nouns)
            question = f"Compare and contrast {self.nouns[0]} and {self.nouns[1]} based on the summary."
            return question
        else:
            return "Not enough information to generate a question."

    def generate_question_type6(self):
        if len(self.nouns) >= 1:
            random.shuffle(self.nouns)
            question = f"What is the role of {self.nouns[0]} in the events described in the summary?"
            return question
        else:
            return "Not enough information to generate a question."

    def generate_question_type7(self):
        if len(self.nouns) >= 1:
            random.shuffle(self.nouns)
            question = f"What is the main idea or concept associated with {self.nouns[0]} in the summary?"
            return question
        else:
            return "Not enough information to generate a question."

    def generate_question_type8(self):
        if len(self.nouns) >= 1:
            random.shuffle(self.nouns)
            question = f"Explain the significance of {self.nouns[0]} based on the information in the summary."
            return question
        else:
            return "Not enough information to generate a question."

    def generate_question_type9(self):
        if len(self.nouns) >= 1:
            random.shuffle(self.nouns)
            question = f"How does {self.nouns[0]} contribute to the central theme of the summary?"
            return question
        else:
            return "Not enough information to generate a question."

    def generate_question_type10(self):
        if len(self.nouns) >= 1:
            random.shuffle(self.nouns)
            question = f"What are some examples or instances of {self.nouns[0]} mentioned in the summary?"
            return question
        else:
            return "Not enough information to generate a question."

    def generate_all_questions(self):
        all_questions = []
        for i in range(1, 11):
            question_function = getattr(self, f"generate_question_type{i}", None)
            if question_function:
                question = question_function()
                all_questions.append(f"Question {i}: {question}")
            else:
                all_questions.append(f"Invalid question type: {i}")
        return all_questions


