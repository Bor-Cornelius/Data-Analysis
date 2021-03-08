import csv

Wrong_unit_price_19th = []

with open("Mc_M01Csrp.csv", "r") as Mc_Cooking_sessions_file:
    csv_reader = csv.DictReader(Mc_Cooking_sessions_file)

    for row in csv_reader:
        Unit_price = row["UP"]
        Account = row["Customer"]
        Received_On = row["Received On"]
        # print(Unit_price, Account)
        if Unit_price != "233.00" and Unit_price != "233.01" and Account != "1111111":
            # print(Unit_price , Account ,Received_On)
            Wrong_unit_price_19th.append({
                "Accounts": row["Customer"],
                "Unit_Price": row["UP"],
                "received_on": row["Received On"]
            })
            # print(Wrong_unit_price)

with open("Wrong_unit_price.csv", "w", newline="") as \
        Cooking_sessions_report_file:
    fieldnames = ["Accounts", "Unit_Price", "received_on"]
    csv_dict_writer = csv.DictWriter(Cooking_sessions_report_file, fieldnames)
    csv_dict_writer.writeheader()

    for Unit_Prices in Wrong_unit_price_19th:
        csv_dict_writer.writerow(Unit_Prices)

     
