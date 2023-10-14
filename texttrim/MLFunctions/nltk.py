import argparse

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from heapq import nlargest
from collections import defaultdict

def sanitize_input(data):
	replace = {
		ord('\f') : ' ',
		ord('\t') : ' ',
		ord('\n') : ' ',
		ord('\r') : None
	}
	return data.translate(replace)

def tokenize_content(content):
	stop_words = set(stopwords.words('english') + list(punctuation))
	words = word_tokenize(content.lower())
	return (sent_tokenize(content), [word for word in words if word not in stop_words])

def score_tokens(sent_tokens, word_tokens):
	word_freq = FreqDist(word_tokens)
	rank = defaultdict(int)
	for i, sent in enumerate(sent_tokens):
		for  word in word_tokenize(sent.lower()):
			if word in word_freq:
				rank[i] += word_freq[word]

	return rank

def summarize(ranks, sentences, length):

	if int(length) > len(sentences):
		print('You requested more sentences in the summary than there are in the text.')
		return ''

	else:
		indices = nlargest(int(length), ranks, key=ranks.get)
		final_summary = [sentences[j] for j in indices]
		return ' '.join(final_summary)

def main(content,lines):
	content2 = sanitize_input(content)

	sent_tokens, word_tokens = tokenize_content(content2)
	sent_ranks = score_tokens(sent_tokens, word_tokens)
	return (summarize(sent_ranks, sent_tokens, lines))
    # return (summarize(sent_ranks, sent_tokens, 3))
