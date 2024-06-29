
## Search Algorithms Documentation

### Nearest Neighbor Search Algorithm

#### Interface:
- `NearestNeighborSearch(index)`
  - Parameter: `index` (index object)
- `search(vector, k=1)`
  - Parameter: `vector` (query vector), `k` (number of nearest neighbors to return)
  - Return: distance and index

#### Example:
```python
search = NearestNeighborSearch(index)
results = search.search(vector, k=5)
```
