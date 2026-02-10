def compute_lps(pattern):
    """
    Bne7seb el Longest Prefix Suffix (LPS) array lel pattern.
    LPS[i] = a6wal prefix mn pattern[0..i] elli heya suffix bardu.
    Da bysa3edna ne skip el comparisons elli msh darooriya lamma yeb2a fe mismatch.
    """
    lps = [0] * len(pattern)
    length = 0  # tool el prefix suffix el sabek
    i = 1
    
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                # Hena msh bnzawed el i, bas bnraga3 el length
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps

def kmp_search(text, pattern):
    """
    Knuth-Morris-Pratt (KMP) algorithm el asli lel string matching.
    A7san mn el naive search - el time complexity beta3o O(n+m).
    """
    if not pattern:
        return []
    
    lps = compute_lps(pattern)
    result = []
    i = 0  # el index beta3 el text
    j = 0  # el index beta3 el pattern
    
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == len(pattern):
                # La2ina match kamla!
                result.append(i - j)
                j = lps[j - 1]  # Ngahaz lel match elli ba3daha
        else:
            if j != 0:
                j = lps[j - 1]  # Nesta3mel el LPS 3ashan neskip 7agat
            else:
                i += 1  # Mafish match, fa nro7 lel character elli ba3daha
    return result

# Ed5al el text wel pattern mn el user
text = input("Ed5al el text elli 3ayez tedawwar fih: ")
pattern = input("Ed5al el pattern elli 3ayez tedawwar 3aleih: ")

# Ne3red el natiga
result = kmp_search(text, pattern)
if result:
    print("El pattern mawgood 3and el indices:", result)
    
    # Nezhar makanet el pattern fel text
    print("\nShakl el pattern fel text:")
    print(text)
    
    # Ne3mel indicator ta7t kol match
    indicators = [" " for _ in range(len(text))]
    for pos in result:
        for i in range(pos, min(pos + len(pattern), len(text))):
            indicators[i] = "^"
    print("".join(indicators))
    
    # Ne3red kol match 3ala 7eda
    print("\nKol el matches:")
    for pos in result:
        match_end = min(pos + len(pattern), len(text))
        print(f"- Fel position {pos}: '{text[pos:match_end]}'")
else:
    print("El pattern mesh mawgood fel text")