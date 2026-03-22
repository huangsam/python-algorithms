# Python Algorithms: Agentic Heuristics

This repository is organized as a collection of "Agents" for solving computational problems. Follow these **When-Then** heuristics for deciding where to place implementations and which patterns to use.

## Agentic Decision Heuristics (Placement)

- **When** the implementation is a foundational, reusable container or data structure (e.g. `CircularBuffer`, `PieceTable`, `Graph`)  
  **Then** place it in `algorithms/collections/`.
- **When** the implementation is a standalone, core string processing algorithm (e.g. `MyersDiff`, `RegexEngine`, `Anagram`)  
  **Then** place it in `algorithms/string/`.
- **When** the implementation involves high-level system components, distribution, or architecture (e.g. `ConsistentHashing`, `ElevatorDesign`)  
  **Then** place it in `algorithms/design/`.
- **When** the implementation is an interview-style puzzle, standalone logic challenge, or platform-specific solution (e.g. `CodeSignal`, `ClimbSteps`, `Josephus`)  
  **Then** place it in `algorithms/online/`.
- **When** the implementation is a pure mathematical or recursive formula (e.g. `Fibonacci`, `Factorial`, `Primes`)  
  **Then** place it in `algorithms/math/`.

## Algorithmic Pattern Heuristics (Usage)

### Memory & State Management
- **When** you need a fixed-size sliding window to store logs or history while ensuring $O(1)$ memory recyclability  
  **Then** use the **Circular Buffer** (`circular_buffer.py`).
- **When** you need to perform high-performance, non-destructive editing (insert/delete) on massive text buffers  
  **Then** use the **Piece Table** (`piece_table.py`).
- **When** you need a probabilistic, space-efficient membership check in a massive set where occasional false positives are acceptable  
  **Then** use the **Bloom Filter** (`bloom_filter.py`).

### String & Synchronization
- **When** you need to calculate the minimal edits (insert/delete) between two data sources for human-readable updates  
  **Then** use the **Myers Diff** (`myers_diff.py`).
- **When** you need back-tracking, non-deterministic pattern matching within strings  
  **Then** use the **Regex Engine** (`regex_engine.py`).

### Distributed Systems & Design
- **When** you need to map keys to a dynamic set of nodes while minimizing the cost of adding or removing nodes  
  **Then** use the **Consistent Hashing** (`consistent_hashing.py`).
- **When** you need to handle multiple asynchronous requests (e.g., floors) with an optimized picking strategy  
  **Then** use the **Elevator Design** (`elevator.py`).

---

## Catalog of Available Agents

### Array & List
- binary_search, bst_array, check_parens, common_elements, depth_sum
- has_cycle, remove_every_other, reverse_alt_k, reverse_list, sum_lists

### Collections & Backtracking
- bloom_filter, circular_buffer, piece_table, graph, list, queue, stack, segment_tree
- get_itinerary, n_queens

### Dynamic Programming & Math
- climb_steps, edit_dist, egg_drop, knapsack, lcs
- car_cdr, count_decode, factorial, fibonacci, josephus

### Graph & Search
- count_islands, floyd_warshall, search, tsp

### String & Parsing
- anagram, autocomplete, chainable, hanoi, myers_diff, regex_engine

### Online & Specialized
- nearby_words, print_tree, word_wrap, tf_idf, sorted_squares, closest_palin, longest_subseq_diff
- **CodeSignal**: comeOnDown, findBase, isTreeSymmetric, kthLargestElement
