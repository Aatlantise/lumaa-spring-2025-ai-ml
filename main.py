import random
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class NLPPaper:
    """
    Class whose instance represents a single ACL Anthology Paper. Attributes include title, author, abstract, year,
    and url.
    """
    def __init__(self, title, author, abstract, year, url):
        self.title = title
        self.author = author
        self.abstract = abstract
        self.year = year
        self.url = url

    def __repr__(self):
        return f"{self.title} ({self.author}, {self.year}). {self.url}."

class NLPPaperDataset:
    """
    A dataset of NLPPaper class instances.
    """
    def __init__(self):
        self.file_path = 'anthology+abstracts.bib'
        self.papers = []
        self.parse_bibtex()

        self.selected_papers = []
        self.get_random_papers()

        self.tfidf, self.features, self.vectorizer = None, None, None
        self.compute_tfidf()

    def __call__(self, query):
        """
        "Retrives" papers relevant to the query.

        :param query: User's input query
        :return: None. Results are printed in self.retrieve().
        """
        self.retrieve(query)

    def parse_bibtex(self):
        """
        Parses bibtex file. Generates a list of NLPPaper instances, which is stored in self.papers
        """
        with open(self.file_path, "r", encoding="utf-8") as file:
            content = file.read()

        entries = content.split("@inproceedings{")[1:]

        for entry in entries:
            if "abstract" not in entry:
                continue

            entry = entry.replace("and\n", "and ")

            title_match = re.search(r'title\s*=\s*[\"\{](.*)[\"\}],', entry, re.IGNORECASE)
            author_match = re.search(r'author\s*=\s*[\"\{](.*)[\"\}],', entry, re.IGNORECASE)
            abstract_match = re.search(r'abstract\s*=\s*[\"\{](.*)[\"\}]', entry, re.IGNORECASE)
            year_match = re.search(r'year\s*=\s*[\"\{](.*)[\"\}],', entry, re.IGNORECASE)
            url_match = re.search(r'url\s*=\s*[\"\{](.*)[\"\}],', entry, re.IGNORECASE)

            # Only add to self.papers if there is no missing fields
            if all([title_match, author_match, abstract_match, year_match, url_match]):
                title = title_match.group(1)
                author = author_match.group(1)
                author = re.sub(r'[\s]+', ' ', author)
                abstract = abstract_match.group(1)
                year = year_match.group(1)
                url = url_match.group(1)
            else:
                continue
            paper = NLPPaper(title, author, abstract, year, url)
            self.papers.append(paper)


    def get_random_papers(self, sample_size=500, seed=42):
        """
        Select 500 random papers from our corpus. Saves results in self.selected_papers.

        :param sample_size: Upper bound for the recommended dataset size
        :param seed: Answer to life
        """
        random.seed(seed)
        self.selected_papers = random.sample(self.papers, min(sample_size, len(self.papers)))

    def compute_tfidf(self):
        """
        Computes tf-idf vectorizer, matrix, and feature list using paper abstracts.
        """
        abstracts = [paper.abstract for paper in self.selected_papers]
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf = self.vectorizer.fit_transform(abstracts)
        self.features = self.vectorizer.get_feature_names_out()

    def compute_similarity(self, query):
        """
        Computes cosine similarity between user query and abstracts.

        :param query: User query
        :return: A list of similarity scores between query and abstract for each abstract
        """
        query_vector = self.vectorizer.transform([query])
        similarity_scores = cosine_similarity(query_vector, self.tfidf).flatten()
        return similarity_scores

    def retrieve(self, query, k=5):
        """
        Computes similarity scores, prints up to k most relevant papers based on their abstracts.

        :param query: User query
        :param k: Maximum number of papers to retrieve
        :return: None
        """
        similarity_scores = self.compute_similarity(query)
        top_indices = similarity_scores.argsort()[::-1][:k]
        top_papers = [(self.selected_papers[idx], similarity_scores[idx])
                      for idx in top_indices if similarity_scores[idx] > 0.001]
        print("")
        print(f"Query: {query}")

        if top_papers:
            for idx in top_indices:
                print("")
                print(f"{self.selected_papers[idx]} Similarity Score: {similarity_scores[idx]:.4f}")
        else:
            print("Sorry. We have no results for your query. Please try again.")


# Example usage
if __name__ == "__main__":
    dataset = NLPPaperDataset()
    dataset("Objective learning for linguistic structure representation")
