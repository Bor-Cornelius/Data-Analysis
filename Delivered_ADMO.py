import csv

Delivered_status = []

with open("Mc_Logsoutgoing.csv", "r") as Mc_delivered_status_file:
    csv_reader = csv.DictReader(Mc_delivered_status_file)

    for row in csv_reader:
        Status = row["Status"]
        Type = row["Type"]
        Meter_No = row["Meter No"]

        # print(Unit_price, Account)
        if Status == "Delivered" and Type == "ADMO":

            Delivered_status.append({
                "Status": row["Status"],
                "Type": row["Type"],
                "Delivered_On": row["Delivered On"],
                "Meter_No": row["Meter No"]
            })
            # print(Delivered_status)

with open("Meters_with_delivered_status.csv", "w", newline="") as \
        Meters_with_delivered_status_report:
    fieldnames = ["Status", "Type", "Meter_No","Delivered_On"]
    csv_dict_writer = csv.DictWriter(Meters_with_delivered_status_report, fieldnames)
    csv_dict_writer.writeheader()

    for Statuses in Delivered_status:
        csv_dict_writer.writerow(Statuses)