# Knuth-Morris-Pratt pattern searching algorithm

def kmp_table(string):
    kmp_table = [-1, 0]
    i = 2
    j = 0
    while i < len(string):
        if string[i -1] == string[j]:
            kmp_table.append(j + 1)
            i += 1
            j += 1
        else:
            if j > 0:
                j = kmp_table[j]
            else:
                kmp_table.append(0)
                i += 1
    return kmp_table


def find(string, text):
    """
    Parameters:string (str): szukany napis
    text (str): przeszukiwany tekst
    Returns:(list): lista pozycji w 'text' (w kolejności rosnącej), od których zaczyna się 'string'
    """
    if not string:
        return []
    list = []
    table = kmp_table(string)
    string_idx = 0
    text_idx = 0
    while text_idx + string_idx < len(text):
        if string[string_idx] == text[string_idx + text_idx]:
            string_idx += 1
            if string_idx == len(string):
                list.append(text_idx)
                string_idx = 0
                text_idx += 1
        else:
            text_idx = text_idx + string_idx - table[string_idx]
            if string_idx > 0:
                string_idx = table[string_idx]
    return list


if __name__ == '__main__':
    string = ''
    text = 'ababa'
    list = find(string, text)
    print(list)