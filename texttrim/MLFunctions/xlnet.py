from summarizer import Summarizer,TransformerSummarizer

def xlnet_summary(text, lines):
 
    model = TransformerSummarizer(transformer_type='XLNet', transformer_model_key='xlnet-base-cased')
    summary = ''.join(model(text, min_length=100))
    return summary