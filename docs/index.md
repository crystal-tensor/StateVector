
## Indexing Algorithms Documentation

### KD Tree Index Algorithm

#### Interface:
- `KDTreeIndex(data)`
  - Parameter: `data` (dataset to build the index)
- `query(vector, k=1)`
  - Parameter: `vector` (query vector), `k` (number of nearest neighbors to return)
  - Return: distance and index

#### Example:
```python
index = KDTreeIndex(data)
distance, index = index.query(vector, k=5)
```
