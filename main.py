import random
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class NLPPaper:
    def __init__(self, title, author, abstract, year, url):
        self.title = title
        self.author = author
        self.abstract = abstract
        self.year = year
        self.url = url

    def __repr__(self):
        return f"{self.title} ({self.author}, {self.year}). {self.url}."

class NLPPaperDataset:
    def __init__(self):
        self.file_path = 'anthology+abstracts.bib'
        self.papers = []
        self.parse_bibtex()
        self.selected_papers = self.get_random_papers()
        self.tfidf, self.features, self.vectorizer = self.compute_tfidf()

    def __call__(self, query):
        self.retrieve(query)

    def parse_bibtex(self):
        with open(self.file_path, "r", encoding="utf-8") as file:
            content = file.read()

        entries = content.split("@inproceedings{")[1:]

        for entry in entries:
            if entry[:2] == "in" or "abstract" not in entry:
                continue

            entry = entry.replace("and\n", "and ")

            title_match = re.search(r'title\s*=\s*[\"\{](.*)[\"\}],', entry, re.IGNORECASE)
            author_match = re.search(r'author\s*=\s*[\"\{](.*)[\"\}],', entry, re.IGNORECASE)
            abstract_match = re.search(r'abstract\s*=\s*[\"\{](.*)[\"\}]', entry, re.IGNORECASE)
            year_match = re.search(r'year\s*=\s*[\"\{](.*)[\"\}],', entry, re.IGNORECASE)
            url_match = re.search(r'url\s*=\s*[\"\{](.*)[\"\}],', entry, re.IGNORECASE)

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
        return self.papers


    def get_random_papers(self, sample_size=500, seed=42):
        random.seed(seed)
        return random.sample(self.papers, min(sample_size, len(self.papers)))

    def compute_tfidf(self):
        abstracts = [paper.abstract for paper in self.selected_papers]
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(abstracts)
        feature_names = vectorizer.get_feature_names_out()
        return tfidf_matrix, feature_names, vectorizer

    def compute_similarity(self, query):
        query_vector = self.vectorizer.transform([query])
        similarity_scores = cosine_similarity(query_vector, self.tfidf).flatten()
        return similarity_scores

    def retrieve(self, query, k=5):
        similarity_scores = self.compute_similarity(query)
        top_indices = similarity_scores.argsort()[::-1][:k]
        top_papers = [(self.selected_papers[idx], similarity_scores[idx])
                      for idx in top_indices if similarity_scores[idx] > 0.001]
        print("")
        print(f"Query: {query}")

        if top_papers:
            for idx in top_indices:
                print("")
                print(f"{self.selected_papers[idx]}. Similarity Score: {similarity_scores[idx]:.4f}")
        else:
            print("Sorry. We have no results for your query. Please try again.")


# Example usage
if __name__ == "__main__":
    dataset = NLPPaperDataset()
    dataset("Objective learning for linguistic structure representation")
