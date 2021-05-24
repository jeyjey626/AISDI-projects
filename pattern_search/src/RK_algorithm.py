d = 256
q = 13


def find(string, text):
    if not string:
        return []
    found_instances = []
    m = len(string)
    n = len(text)
    p = 0
    t = 0
    h = 1
    i = 0
    j = 0

    if m > n:
        return []

    for i in range(m-1):
        h = (h*d) % q

    # Calculate hash value for pattern and text
    for i in range(m):
        p = (d * p + ord(string[i])) % q
        t = (d*t + ord(text[i])) % q

    # Find the match
    for i in range(n-m+1):
        if p == t:
            for j in range(m):
                if text[i+j] != string[j]:
                    break

            j += 1
            if j == m:
                found_instances.append(i)

        if i < n-m:
            t = (d*(t-ord(text[i])*h) + ord(text[i+m])) % q

            if t < 0:
                t = t+q
    return found_instances