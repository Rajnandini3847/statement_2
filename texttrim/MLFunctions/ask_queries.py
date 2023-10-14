from summarizer import Summarizer
from transformers import pipeline


def answer_question(context, question):
    qa_pipeline = pipeline("question-answering", model="bert-large-uncased-whole-word-masking-finetuned-squad")
    result = qa_pipeline(question=question, context=context)
    return result["answer"]