from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import spacy

nlp = spacy.load("en_core_web_lg")

def analyze_resume(resume_text):
    """Enhanced resume analysis with spaCy"""
    doc = nlp(resume_text)
    return {
        "skills": [ent.text for ent in doc.ents if ent.label_ == "SKILL"],
        "summary": " ".join([sent.text for sent in doc.sents][:3])
    }

def get_recommendations(job_descriptions, resume_data):
    """Hybrid recommendation system"""
    tfidf = TfidfVectorizer(stop_words='english')
    
    # Combine all text data
    corpus = [jd['description'] for jd in job_descriptions]
    corpus.append(f"{resume_data['skills']} {resume_data['summary']}")
    
    # Create vectors
    tfidf_matrix = tfidf.fit_transform(corpus)
    
    # Calculate similarity
    cosine_sim = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    return sorted(zip(range(len(job_descriptions)), cosine_sim[0]), 
                key=lambda x: x[1], reverse=True)[:5]