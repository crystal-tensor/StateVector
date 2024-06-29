
## Vector Representation Algorithms Documentation

### Text Vectorization

#### Model:
- Word2Vec

#### Interface:
- `TextVectorizer(model_path)`
  - Parameter: `model_path` (path to the model)
- `vectorize(text)`
  - Parameter: `text` (text to be vectorized)
  - Return: vector representation of the text

#### Example:
```python
vectorizer = TextVectorizer('model/word2vec_model.bin')
vector = vectorizer.vectorize("example text")
```
