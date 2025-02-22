from main import NLPPaperDataset

def app():
    """
    Runs the app!

    :return: None
    """
    dataset = NLPPaperDataset()
    while True:
        query = input("Enter your query. To exit, press ctrl + c.\n")
        dataset(query)

if __name__ == "__main__":
    app()
