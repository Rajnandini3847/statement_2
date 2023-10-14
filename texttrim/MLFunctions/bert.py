from summarizer import Summarizer,TransformerSummarizer


def bert_summary(text,lines):
    min_length = int(lines*10)
    bert_model = Summarizer()
    summary = ''.join(bert_model(text, min_length=100))
    return summary