# Smart Task Recommender 🚀

**Recommend the perfect task based on your current mood, energy, stress, and available time.**

Tired but have 30 mins? → Light reading  
Pumped with 90 mins free? → Deep work session  

Built with FastAPI for speed and simplicity.

## Live Demo / Screenshots
## 📄 Project Demo (PDF)

👉 [View API Demo (PDF)](docs/api-demo.pdf)


## How It Works
- You input: mood (1-5), energy (1-5), stress (1-5), available_time (minutes)
- Smart scoring: `score = (energy × 2) + mood - (stress × 1.5)`
- Recommends one of 4 task types with reasoning

## Quick Start
```bash
# Clone the repository
git clone https://github.com/BezaleelPaul/Smart-Task-Recommender.git

# Move into the project directory
cd Smart-Task-Recommender

# Install dependencies
pip install -r requirements.txt

# Run the FastAPI server
uvicorn app.main:app --reload


