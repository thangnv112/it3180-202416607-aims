def search_by_category(items, category):
    return [dvd for dvd in items if dvd.category == category]


def search_by_title(items, title):
    return [dvd for dvd in items if title in dvd.title]
