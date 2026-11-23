import csv

valid_rows = []
skipped_rows = []
rows_attempted = 0

try:
    with open("../data/messy_data.csv", "r") as file:
        reader = csv.DictReader(file)

        for row_num, row in enumerate(reader, start=2):
            rows_attempted += 1

            try:
                if None in row:
                    skipped_rows.append(
                        f"Row {row_num}: extra column detected — skipped"
                    )
                    continue

                name = row["name"]
                category = row["category"]
                amount = float(row["amount"])

                valid_rows.append({
                    "name": name,
                    "category": category,
                    "amount": amount
                })

            except ValueError:
                skipped_rows.append(
                    f"Row {row_num}: ValueError — could not convert '{row['amount']}' to float"
                )

            except KeyError:
                skipped_rows.append(
                    f"Row {row_num}: KeyError — missing expected column"
                )

except FileNotFoundError:
    print("Error: ../data/messy_data.csv was not found.")
    exit()

print("=== CSV Report ===")
print(f"Rows attempted: {rows_attempted}")
print(f"Rows parsed:    {len(valid_rows)}")
print(f"Rows skipped:   {len(skipped_rows)}")

print("\nSkipped rows:")
for message in skipped_rows:
    print(" ", message)

print("\nClean data:")
for row in valid_rows:
    print(
        f"  {row['name']} | {row['category']} | ${row['amount']:.2f}"
    )