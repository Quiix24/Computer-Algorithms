# KMP String Search Algorithm Implementation

A complete implementation of the Knuth-Morris-Pratt (KMP) string searching algorithm in Python, featuring an efficient O(n+m) time complexity solution with bilingual documentation.

## 🚀 Features

- **Efficient Search**: O(n+m) time complexity where n is text length and m is pattern length
- **LPS Array**: Optimized Longest Prefix Suffix preprocessing for skip-ahead functionality
- **Interactive Interface**: User-friendly command-line interface with Arabic/English support
- **Visual Output**: Clear visualization of pattern matches with position indicators
- **Comprehensive Documentation**: Includes both code comments and PDF guide

## 📋 Algorithm Overview

The KMP algorithm improves upon naive string matching by using a preprocessed "failure function" (LPS array) to avoid redundant character comparisons. When a mismatch occurs, instead of starting over from the next character, the algorithm uses the LPS array to determine how many characters can be safely skipped.

### Key Components:

1. **LPS Array Computation**: Preprocesses the pattern to create a lookup table
2. **Pattern Matching**: Uses the LPS array to efficiently search through the text
3. **Result Collection**: Returns all occurrence positions of the pattern

## 🛠️ Installation & Usage

### Prerequisites
- Python 3.6 or higher
- No external dependencies required

### Running the Program

1. Clone this repository:
```bash
git clone https://github.com/yourusername/kmp-algorithm.git
cd kmp-algorithm
```

2. Run the program:
```bash
python kmp_search.py
```

3. Follow the prompts:
   - Enter the text you want to search in
   - Enter the pattern you want to find
   - View the results with position indicators

### Example Usage

```
Ed5al el text elli 3ayez tedawwar fih: ABABCABABA
Ed5al el pattern elli 3ayez tedawwar 3aleih: ABA

El pattern mawgood 3and el indices: [0, 2, 7]

Shakl el pattern fel text:
ABABCABABA
^^^^ ^ ^^^

Kol el matches:
- Fel position 0: 'ABA'
- Fel position 2: 'ABA'  
- Fel position 7: 'ABA'
```

## 📁 Project Structure

```
├── kmp_search.py                                    # Main implementation
├── Complete KMP Algorithm Implementation Guide.pdf  # Detailed documentation
├── Screenshot 2025-05-23 124310.png               # Example output 1
├── Screenshot 2025-05-23 124318.png               # Example output 2
└── README.md                                       # This file
```

## 🧮 Algorithm Complexity

- **Time Complexity**: O(n + m)
  - LPS array computation: O(m)
  - Pattern searching: O(n)
- **Space Complexity**: O(m) for the LPS array

Where `n` is the length of the text and `m` is the length of the pattern.

## 🔍 How It Works

### 1. LPS Array Construction
The `compute_lps()` function creates an array where `lps[i]` represents the length of the longest proper prefix of `pattern[0..i]` which is also a suffix of `pattern[0..i]`.

### 2. Pattern Matching
The `kmp_search()` function uses the LPS array to avoid unnecessary character comparisons by skipping positions that are guaranteed not to match.

### 3. Result Visualization
The program provides:
- List of all match positions
- Visual representation with caret (^) symbols
- Individual match details

## 🤝 Contributing

Feel free to fork this project and submit pull requests for any improvements:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 📚 References

- Knuth, Donald; Morris, James H.; Pratt, Vaughan (1977). "Fast pattern matching in strings"
- [KMP Algorithm - GeeksforGeeks](https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/)

## 👨‍💻 Author

**Ahmed Mohamed**
- GitHub: [@Quiix24](https://github.com/Quiix24)
- LinkedIn: [Ahmed Mohamed](https://www.linkedin.com/in/ahmed-said-youssif)

---

*This implementation demonstrates understanding of advanced string algorithms and efficient algorithm design principles.*
