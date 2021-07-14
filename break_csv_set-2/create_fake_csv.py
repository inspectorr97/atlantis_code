import csv
from faker import Faker


fake = Faker()

def create_csv_file(RECORD_COUNT):
    with open('dummy.csv', 'w', newline='') as csvfile:
        fieldnames = ['id', 'first_name', 'last_name', 'email', 'pincode', 'timestamp']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {   
                    'id': fake.random_int(min=100, max=199),
                    'first_name': fake.name(),
                    'last_name': fake.name(),
                    'email': fake.email(),
                    'pincode' : fake.postcode(),
                    'timestamp' : fake.time()
                }
            )

if __name__ == "__main__":
    RECORD_COUNT = 100000
    create_csv_file(RECORD_COUNT)
    print("finished!")