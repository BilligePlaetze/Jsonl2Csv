
from datetime import datetime
import csv,  json, sys

def get_isodate(msg):
    date = msg.get("date", None)

    if not date:
        return "unknown"

    return datetime.fromtimestamp(date).isoformat()

def main():
    if len(sys.argv) != 3:
        if len(sys.argv) > 2:
             sys.exit("No json and and csv file given")
        elif len(sys.argv) >= 2:
            sys.exit("No csv file given")

    jsonpath = sys.argv[1]
    csvpath = sys.argv[2]

    with open(jsonpath, "r") as jsonfile:
        with open(csvpath, "w", newline='') as csvfile:
            csvwriter = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            csvwriter.writerow(["from", "to", "date", "text"])
            for item in jsonfile:
                msg = json.loads(item, 'cp1250')

                csvwriter.writerow([
                    msg["from"].get("print_name", "unknown"),
                    msg["to"].get("print_name", "unknown"),
                    get_isodate(msg),
                    msg.get("text", "no text")
                ])

if __name__ == "__main__":
    main()