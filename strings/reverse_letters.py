def reverse_letters(sentence: str, length: int = 0) -> str:

    return " ".join(
        "".join(word[::-1]) if len(word) > length else word for word in sentence.split()
    )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(reverse_letters("Hey wollef sroirraw"))
