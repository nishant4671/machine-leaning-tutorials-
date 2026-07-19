Tokenisation in Artificial Intelligence (NLP / LLMs)
In AI, tokenisation is the process of breaking down human-readable text into smaller, machine-readable pieces called tokens. These are the fundamental units that an AI model (like ChatGPT) processes. A token is not always a whole word; it can be a subword, a character, or a punctuation mark.

Related Terms:

Token: The smallest unit of text the model understands. (e.g., The word "unhappiness" might be tokenized as [un, happi, ness]).

Vocabulary: The complete, predefined list of all possible tokens that a specific AI model knows.

Subword Tokenisation: The most common modern approach. It splits rare words into frequent fragments (e.g., "tokenization" -> [token, ization]) so the model doesn't get confused by words it hasn't seen before.

BPE (Byte-Pair Encoding): A popular algorithm (used by GPT models) that iteratively merges the most frequently occurring pairs of bytes/characters to build the vocabulary.

WordPiece: Google’s algorithm (used in BERT) similar to BPE, but it merges based on likelihood rather than frequency.

SentencePiece: A system used by models like Llama that treats the input as a raw stream of Unicode characters, allowing it to tokenize any language without needing spaces.

Token Limit / Context Window: The maximum number of tokens the AI can process in a single prompt+response. (e.g., GPT-4 has a 128k token limit).

Embedding: The numerical vector (list of numbers) that the model assigns to a token after tokenisation, so it can do math with it.