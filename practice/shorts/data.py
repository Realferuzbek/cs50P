SHOWS = [
    "david   Malan",
    "Matilda   obana",
    "Ohho  Oyy",
]


def clear():
    cleaned = []
    for show in SHOWS:
        cleaned.append(' '.join(show.title().split()))
    print(', '.join(cleaned))

clear()


# .split() .title()
