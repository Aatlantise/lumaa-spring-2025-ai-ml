from main import NLPPaperDataset

def main():
    dataset = NLPPaperDataset()
    while True:
        query = input("Enter your query. To exit, press ctrl + c.")
        dataset(query)

if __name__ == "__main__":
    main()
