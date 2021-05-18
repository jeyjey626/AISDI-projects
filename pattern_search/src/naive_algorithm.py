# Naive pattern searching algorithm

def find(string, text):
        """
        Parameters:string (str): szukany napis
        text (str): przeszukiwany tekst
        Returns:(list): lista pozycji w 'text' (w kolejności rosnącej), od których zaczyna się 'string'
        """
        if not string:
            return []

        pattern_len = len(string)
        list = []
        for i in range(len(text)-pattern_len+1):
            if text[i:pattern_len + i] == string:
                list.append(i)
        return list


if __name__ == '__main__':
    string = ''
    text = 'aaaaaaaaaa'
    list = find(string, text)
    print(list)