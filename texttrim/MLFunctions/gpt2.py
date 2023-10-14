from summarizer import Summarizer,TransformerSummarizer


def gpt2_summary(text,lines):
    model = TransformerSummarizer(transformer_type="GPT2",transformer_model_key="gpt2-medium")
    result = model(text, min_length=int(lines))
    full = ''.join(result)
    return full