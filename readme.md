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
git clone <your-repo>
cd smart-task-recommender
pip install -r requirements.txt

uvicorn app.main:app --reload
