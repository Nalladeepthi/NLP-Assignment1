from collections import defaultdict

# Training corpus
corpus = [
    ["<s>", "I", "love", "NLP", "</s>"],
    ["<s>", "I", "love", "deep", "learning", "</s>"],
    ["<s>", "deep", "learning", "is", "fun", "</s>"]
]

# Step 1 & 2: Compute unigram and bigram counts
unigram_counts = defaultdict(int)
bigram_counts = defaultdict(int)

for sentence in corpus:
    for i in range(len(sentence)):
        unigram_counts[sentence[i]] += 1
        if i < len(sentence) - 1:
            bigram = (sentence[i], sentence[i+1])
            bigram_counts[bigram] += 1

# Step 3: Compute bigram probabilities using MLE
bigram_probabilities = {}
for (w1, w2), count in bigram_counts.items():
    bigram_probabilities[(w1, w2)] = count / unigram_counts[w1]

# Step 4: Function to compute probability of a sentence
def sentence_probability(sentence, bigram_probs, unigram_counts):
    words = sentence.split()
    prob = 1.0
    for i in range(len(words) - 1):
        bigram = (words[i], words[i+1])
        if bigram in bigram_probs:
            prob *= bigram_probs[bigram]
        else:
            prob *= 0  # unseen bigram has probability 0 under MLE
    return prob

# Test sentences
s1 = "<s> I love NLP </s>"
s2 = "<s> I love deep learning </s>"

p1 = sentence_probability(s1, bigram_probabilities, unigram_counts)
p2 = sentence_probability(s2, bigram_probabilities, unigram_counts)

# Print results
print("Sentence 1:", s1, "Probability:", p1)
print("Sentence 2:", s2, "Probability:", p2)

if p1 > p2:
    print("Model prefers Sentence 1 because it has a higher probability.")
elif p2 > p1:
    print("Model prefers Sentence 2 because it has a higher probability.")
else:
    print("Model assigns equal probability to both sentences.")
