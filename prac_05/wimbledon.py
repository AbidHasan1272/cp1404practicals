"""
CP1404/CP5632 Practical - Suggested Solution
Program: Wimbledon
Estimate: 30 minutes
Actual:   35 minutes
"""

FILENAME = "wimbledon.csv"
INDEX_0F_COUNTRY = 1
INDEX_OF_CHAMPION = 2

def main():
    """Read data file and print details."""
    records = load_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)

def process_records(records):
    """Make dictionary of champions and set of countries from records ."""
    champion_to_count = {}
    countries = set()
    for record in records:
        countries.add(record[INDEX_0F_COUNTRY])
        try:
            champion_to_count[record[INDEX_OF_CHAMPION]] += 1
        except KeyError:
            champion_to_count[record[INDEX_OF_CHAMPION]] = 1
    return champion_to_count, countries

def display_results(champion_to_count, countries):
    """Display champions and countries"""
    print("Wimbledon Champions: ")
    for name, count in champion_to_count.items():
        print(name, count)
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))

def load_records(filename):
    """Load records from file in list of lists form."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


main()