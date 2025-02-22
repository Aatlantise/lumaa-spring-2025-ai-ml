# Junghyun Min's solution to Lumaa's AI/ML coding challenge
---

## Overview

This repository implements a simple, tf-idf-based NLP paper recommendation system.  

### Example Use Case

- The user inputs a query:  
  *"Data augmentation for robust language learning"*  
- The system processes this description (query) and compares it to a dataset of randomly selected 500 articles from ACL Anthology.  
- The system returns up to 5 relevant articles, along with their urls and similarity scores.
```angular2html
Query: data augmentation for robust language learning

Tailoring Domain Adaptation for Machine Translation Quality Estimation (Sharami, Javad Pourmostafa Roshan and Shterionov, Dimitar and Blain, Fr{\'e}d{\'e}ric and Vanmassenhove, Eva and Sisto, Mirella De and Emmery, Chris and Spronck, Pieter, 2023). https://aclanthology.org/2023.eamt-1.2/. Similarity Score: 0.2113

{UU}-Tax at {S}em{E}val-2022 Task 3: Improving the generalizability of language models for taxonomy classification through data augmentation (Sarhan, Injy and Mosteiro, Pablo and Spruit, Marco, 2022). https://aclanthology.org/2022.semeval-1.35/. Similarity Score: 0.1842

On the Impact of Temporal Concept Drift on Model Explanations (Zhao, Zhixue and Chrysostomou, George and Bontcheva, Kalina and Aletras, Nikolaos, 2022). https://aclanthology.org/2022.findings-emnlp.298/. Similarity Score: 0.1423

Generative Cross-Domain Data Augmentation for Aspect and Opinion Co-Extraction (Li, Junjie and Yu, Jianfei and Xia, Rui, 2022). https://aclanthology.org/2022.naacl-main.312/. Similarity Score: 0.1246

Sartipi-Sedighin at {S}em{E}val-2023 Task 2: Fine-grained Named Entity Recognition with Pre-trained Contextual Language Models and Data Augmentation from {W}ikipedia (Sartipi, Amir and Sedighin, Amirreza and Fatemi, Afsaneh and Baradaran Kashani, Hamidreza, 2023). https://aclanthology.org/2023.semeval-1.78/. Similarity Score: 0.1246

```

---

## Setup and launch

To perform setup the launch the app, simply run the following:
```angular2html
bash get-data.sh
pip install -r requirements.txt
python3 app.py
```

It will prompt your query:
```angular2html
Enter your query. To exit, press ctrl + c.
```

Enter your query,
```angular2html
Enter your query. To exit, press ctrl + c.
Data augmentation for robust language learning
```

And enjoy your recommended list of articles!
If you wish to receive another set of articles, simply input your new query right away.
```angular2html

Query: Data augmentation for robust language learning

Tailoring Domain Adaptation for Machine Translation Quality Estimation (Sharami, Javad Pourmostafa Roshan and Shterionov, Dimitar and Blain, Fr{\'e}d{\'e}ric and Vanmassenhove, Eva and Sisto, Mirella De and Emmery, Chris and Spronck, Pieter, 2023). https://aclanthology.org/2023.eamt-1.2/. Similarity Score: 0.2113

{UU}-Tax at {S}em{E}val-2022 Task 3: Improving the generalizability of language models for taxonomy classification through data augmentation (Sarhan, Injy and Mosteiro, Pablo and Spruit, Marco, 2022). https://aclanthology.org/2022.semeval-1.35/. Similarity Score: 0.1842

On the Impact of Temporal Concept Drift on Model Explanations (Zhao, Zhixue and Chrysostomou, George and Bontcheva, Kalina and Aletras, Nikolaos, 2022). https://aclanthology.org/2022.findings-emnlp.298/. Similarity Score: 0.1423

Generative Cross-Domain Data Augmentation for Aspect and Opinion Co-Extraction (Li, Junjie and Yu, Jianfei and Xia, Rui, 2022). https://aclanthology.org/2022.naacl-main.312/. Similarity Score: 0.1246

Sartipi-Sedighin at {S}em{E}val-2023 Task 2: Fine-grained Named Entity Recognition with Pre-trained Contextual Language Models and Data Augmentation from {W}ikipedia (Sartipi, Amir and Sedighin, Amirreza and Fatemi, Afsaneh and Baradaran Kashani, Hamidreza, 2023). https://aclanthology.org/2023.semeval-1.78/. Similarity Score: 0.1246
Enter your query. To exit, press ctrl + c.
```

---

## Demo Video
[Placeholder link]()

---

### Monthly salary expectations
My salary expectations are flexible, depending on the nature of work.
In a full-time role requiring my level of expertise and experience, my monthly salary expectations are $6-10k.
