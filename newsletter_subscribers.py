import csv

newsletter_subscribers_above_30 = []

with open("newsletter_subscribers.csv", "r") as newsletter_subscribers_file:
    csv_dict_reader = csv.DictReader(newsletter_subscribers_file)

    for row in csv_dict_reader:
        age = int(row["age"])
        referred_by = row["referred_by"]
        if age >= 30 and referred_by == "google":
            newsletter_subscribers_above_30.append({
                "name": row["name"],
                "email": row["email"]
            })
            print(newsletter_subscribers_above_30)
with open("newsletter_subscribers_above_30.csv", "w", newline="") as\
        newsletter_subscribers_above_30_file:
    fieldnames = ["name","email"]
    csv_dict_writer = csv.DictWriter(
        newsletter_subscribers_above_30_file,fieldnames=fieldnames)
    csv_dict_writer.writeheader()

    for subscribe in newsletter_subscribers_above_30:
        csv_dict_writer.writerow(subscribe)
