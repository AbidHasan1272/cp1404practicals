"""
wiki.py
CP1404 Wikipedia Search Program
"""

import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

def main():
    while True:
        user_input = input("Enter page title: ").strip()
        if not user_input:
            print("Thank you.")
            break

        try:
            # Get the page with no autosuggest to prevent redirect surprises
            page = wikipedia.page(user_input, autosuggest=False)
            print(f"{page.title}")
            print(f"{page.summary}\n")
            print(page.url)
        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except PageError:
            print(f'Page id "{user_input}" does not match any pages. Try another id!')

if __name__ == "__main__":
    main()
