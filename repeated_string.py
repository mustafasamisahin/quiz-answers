def repeated_string(s, n):
    word_count = int(n / len(s))
    a_count = s.count('a')
    count = word_count * a_count + s[:n % len(s)].count('a')
    return count