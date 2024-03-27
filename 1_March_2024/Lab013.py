import csv

test_data = [
    ["name", "age", "city"],
    ["alice", 25, "canada"],
    ["laila", 22, "newyork"]
]

try:
    with open ("data1.csv", "w") as file:
        writer = csv.writer(file)
        for data in test_data:
            writer.writerow(data)
except Exception as e:
    print(e)
finally:
    print("close file")