# import libraries
import spacy

# load spacy
nlp = spacy.load('en_core_web_md')

# words to compare similarities
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# display similarities
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print()

# I initially thought the similarity between 'monkey' and 'banana' would be higher than the similarity between 'monkey' and 'cat'.
# However, it is very cool to see how the spacy classifies words 
# One thing I didn't see until it was pointed out in the task was that there are no transitive relationships taken into account for the similarity calculations

# own example
word_1 = nlp("traffic")
word_2 = nlp("work")
word_3 = nlp("cars")

print(word_1.similarity(word_2))  # 0.2500449776662009
print(word_1.similarity(word_3))  # 0.41640239871305745
print()

# compare each word against every word provided (including itself)
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
    print()


sentence_to_compare = "Why is my cat on the car"

# sentences for comparisons
sentences = ["where did my dog go",
            "Hello, there is my car",
            "I\'ve lost my car in my car",
            "I\'d like my boat back",
            "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

# compare sentences
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


# Running file with the simpler language model 'en_core_web_sm':
# The model does not allow for effective similarity calculations for associativity.
# The similarities between words are significantly higher than the similarities between sentences.
# This could imply the model does not have the capability of adequately calculating similarities between sentences.
# The model returns similarities that don't make sense (e.g. cat apple 0.7018378973007202, monkey apple 0.7389943599700928, etc.)