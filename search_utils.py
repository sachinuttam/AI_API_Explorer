"""
search_utils.py
-----------------
Lightweight keyword-based search engine used to rank the APIs in
data/apis_data.py against whatever a user types in the search bar.

No heavy ML dependencies needed — just weighted keyword matching, which
is fast, transparent, and works instantly with zero training time.
"""

import re
from difflib import SequenceMatcher

from data.apis_data import APIS


def _tokenize(text: str):
    return re.findall(r"[a-z0-9]+", text.lower())


def _similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a, b).ratio()


def score_api(query_tokens, api: dict) -> float:
    """Weighted score: name matches count most, then category, then tags,
    then description. Adds a small fuzzy-similarity bonus so close
    misspellings still surface reasonable results."""
    name = api["name"].lower()
    category = api["category"].lower()
    tags = [t.lower() for t in api["tags"]]
    description = api["description"].lower()

    score = 0.0
    for token in query_tokens:
        if token in name:
            score += 5
        if token in category:
            score += 4
        if any(token in tag or tag in token for tag in tags):
            score += 3
        if token in description:
            score += 1

        # fuzzy bonus in case of typos / partial words
        best_fuzzy = max(
            [_similarity(token, tag) for tag in tags] +
            [_similarity(token, w) for w in _tokenize(category)],
            default=0,
        )
        if best_fuzzy > 0.8:
            score += 1.5

    return score


def search_apis(query: str, top_n: int = 5):
    """Return the top_n APIs best matching the query.
    Falls back to an empty list if the query is blank."""
    query = (query or "").strip()
    if not query:
        return []

    tokens = _tokenize(query)
    if not tokens:
        return []

    scored = [(score_api(tokens, api), api) for api in APIS]
    scored = [(s, api) for s, api in scored if s > 0]
    scored.sort(key=lambda pair: pair[0], reverse=True)

    return [api for _, api in scored[:top_n]]


def get_featured_apis():
    """A fixed set of 5 popular/diverse APIs shown by default before the
    user searches for anything."""
    featured_names = [
        "OpenWeatherMap API",
        "Alpha Vantage",
        "NewsAPI",
        "OpenAI API",
        "Google Maps Platform",
    ]
    lookup = {api["name"]: api for api in APIS}
    return [lookup[name] for name in featured_names if name in lookup]


def get_all_categories():
    return sorted({api["category"] for api in APIS})
