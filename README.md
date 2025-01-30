# She-Talks-Tech
AI Driven Internships and Placements Recommendation System
# Internship-and-Placement
AI Driven Internships and Placements Recommendation System

## 🌟 Features
- **AI Recommendations**: Content-based filtering using skills/GPA
- **Resume Analyzer**: ATS compatibility checker with NLP
- **Web Scraping**: Real-time internship/placement data aggregation
- **Collaboration Hub**: Real-time chat & discussion forums
- **Placement Analytics**: Interactive dashboards with Chart.js
- **Responsive Design**: Optimized for mobile & desktop

## 🛠️ Tech Stack
**Frontend**  
`React.js` `Tailwind CSS` `Chart.js` `Socket.io`

**Backend**  
`Node.js` `Express.js` `Python` `Flask`

**AI/ML**  
`scikit-learn` `spaCy` `NLTK` `TensorFlow`

**Database**  
`PostgreSQL` (Placements)  
`MongoDB` (User Data)

**DevOps**  
`Docker` `AWS EC2` `Heroku` `GitHub Actions`

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 18.x
- PostgreSQL & MongoDB

### Installation
```bash
# Clone repository
git clone https://github.com/yourusername/she-talks-tech.git
cd she-talks-tech

# Frontend setup
cd frontend
npm install
npm start

# Backend setup (new terminal)
cd ../backend
pip install -r requirements.txt
python app.py

🔍 How It Works

1. Data Collection: Web scraping of job portals

2. Resume Parsing: PDF/text analysis with NLP

3. AI Matching:

# Content-based filtering example

def calculate_similarity(user_skills, job_requirements):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([user_skills, job_requirements])
    return cosine_similarity(vectors[0], vectors[1])[0][0]
    
4. Dashboard: Interactive visualization of placement trends

PROJECT STRUCTURE 

she-talks-tech/

├── frontend/          # React application

├── backend/           # Node.js & Python API

├── ml_models/         # Recommendation algorithms

├── database/          # SQL schemas & migrations

├── docs/              # Documentation & screenshots

└── Dockerfile         # Container configuration

🤝 Contributing

- Fork the repository

- Create your feature branch (git checkout -b feature/amazing-feature)

- Commit changes (git commit -m 'Add amazing feature')

- Push to branch (git push origin feature/amazing-feature)

- Open a Pull Request
