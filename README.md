# LeetRec  

*A LeetCode problem recommender using custom data structures.*  

## Overview  
LeetRec suggests **LeetCode problems** based on your chosen topic (e.g., *Arrays & Strings*) and difficulty level (*Easy*, *Medium*, *Hard*). It demonstrates the practical use of **hash maps** and **linked lists** to organize and retrieve problems efficiently.  

---

## Data Structures Implemented  
- **`LinkedList`**  
  - Stores problems as nodes with `add_node` and traversal support.  
- **`HashMap`**  
  - Maps topics to nested hashmaps of difficulties (e.g., `subject → difficulty → problem_list`).  
  - Handles collisions via **linear probing**.  

*(See [`datastructures.py`](./datastructures.py) for details.)*  

---

## How to Run  
1. Clone the repo:  
   ```bash
   git clone https://github.com/your-username/leetrec.git
   cd leetrec
   ```
2. Execute:
    ```bash
    python3 main.py
    ```

## Project Structure

| File | Description |
| :---:| :----------:|
| datastructures.py | Custom datastructures |
| problemset.py | Predefined topics/problems database|
| main.py | CLI interface and problem retrieval. | 