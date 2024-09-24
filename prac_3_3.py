def tally_votes(num_entries, entries):
    vote_count = {}

    for entry in entries:
        candidate, votes = entry.split()
        votes = int(votes)

        if candidate in vote_count:
            vote_count[candidate] += votes
        else:
            vote_count[candidate] = votes

    for candidate in sorted(vote_count.keys()):
        print(f"{candidate}: {vote_count[candidate]}")

if __name__ == "__main__":
    num_entries = int(input("Введите количество записей: "))
    entries = []

    for _ in range(num_entries):
        entry = input("Введите фамилию кандидата и количество голосов: ")
        entries.append(entry)

    print("\nИтоги выборов:")
    tally_votes(num_entries, entries)
