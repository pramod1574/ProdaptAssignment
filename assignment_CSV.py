import csv

dataset = {}


def process_csv(*args):
    key = 0
    for file in args:

        with open(file, 'r') as fh:
            csv_reader = csv.DictReader(fh)

            for lines in csv_reader:
                key += 1
                dataset[key] = lines
    # print(dataset)

    if not dataset:
        return "Files are empty or no input files provided"

    # Processing values from dataset and segregate them properly
    colnames = ['timestamp', 'type', 'amount', 'euro', 'cents', 'from', 'to']
    final_lis = []
    for row in dataset.values():
        rows = dict(row)

        if rows.get('timestamp'):
            timestamp = rows['timestamp']
        elif rows.get('date_readable'):
            timestamp = rows['date_readable']
        elif rows.get('date'):
            timestamp = rows['date']
        else:
            timestamp = None

        if rows.get('type'):
            type = rows['type']
        elif rows.get('transaction'):
            type = rows['transaction']
        else:
            type = None

        if rows.get('amounts'):
            amount = rows['amounts']
        elif rows.get('amount'):
            amount = rows['amount']
        else:
            amount = None

        if rows.get('from'):
            fro = rows['from']
        else:
            fro = None

        if rows.get('to'):
            to = rows['to']
        else:
            to = None

        if rows.get('euro'):
            euro = rows['euro']
        else:
            euro = None

        if rows.get('cents'):
            cents = rows['cents']
        else:
            cents = None

        rowlist = [timestamp, type, amount, euro, cents, fro, to]
        final_lis.append(rowlist)

    # Writing to a final csv file
    combined_csv = "combined.csv"

    with open(combined_csv, 'w', newline='') as fw:
        csv_writer = csv.writer(fw)
        csv_writer.writerow(colnames)
        csv_writer.writerows(final_lis)
    return "success"

# process_csv('bank1.csv', 'bank2.csv', 'bank3.csv')
