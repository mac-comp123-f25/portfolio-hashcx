import string


def compute_frequencies(fn: str) -> dict[str, int]:
    fn_obj = open(fn)
    words: list[str] = fn_obj.read().split()
    words_clean: list[str] = []
    for word in words:
        words_clean.append(word.strip(string.punctuation))

    freq: dict[str, int] = {}
    for word in words_clean:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


def print_most_freq(freq: dict[str, int], n: int = None) -> None:
    lst = sorted(list(freq.items()), key=lambda elem: elem[1], reverse=True)

    if n == None:
        n = len(freq)

    lst_print = lst[0:n]

    # find length of longest word
    max_len = len(sorted(lst_print, key=lambda elem: len(elem[0]), reverse=True)[0][0])

    for elem in lst_print:
        print(f"{elem[0].ljust(max_len + 3, '.')}{elem[1]}")

freq: dict[str, int] = compute_frequencies("../TextFiles/mobydick.txt")
print_most_freq(freq, n = None)
