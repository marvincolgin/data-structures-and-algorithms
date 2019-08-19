from repeated_word import repeated_word

def test_sample1():
    input = "Once upon a time, there was a brave princess who..."

    expected = "a"
    actual = repeated_word(input)
    assert expected == actual


def test_sample2():
    input = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way - in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    expected = "it"
    actual = repeated_word(input)
    assert expected == actual


def test_sample3():
    input = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn't know what I was doing in New York..."
    expected = "summer"
    actual = repeated_word(input)
    assert expected == actual

