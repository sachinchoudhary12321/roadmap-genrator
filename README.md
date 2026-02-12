# roadmap-genrator
AI Roadmap Generator  An AI-powered web application that generates structured and personalized learning roadmaps based on user skill, level, and career goal.
🚀 AI Roadmap Generator

An AI-powered web application that generates personalized learning roadmaps based on your skill, current level, and career goal.

This project uses Streamlit for frontend UI and Gemini 2.5 Flash API for intelligent roadmap generation.

📌 Problem Statement

Many learners struggle with:

What to learn first

How long to spend on each topic

Which projects to build

How to prepare for interviews

This AI tool acts as a career mentorship assistant and provides a structured roadmap in seconds.

✨ Features

🎯 Skill-based roadmap generation

📊 Beginner / Intermediate / Advanced levels

🗺 Timeline-based structured plan

💼 Project recommendations

🛠 Tools and technologies guidance

📚 Free learning resources

🎤 Interview preparation steps

📥 Download roadmap as text file

🛠 Tech Stack

Python

Streamlit

Gemini 2.5 Flash API

OpenAI-compatible SDK

dotenv (Environment variables)

⚙️ How It Works

User enters:

Skill

Current Level

Career Goal

A structured prompt is generated dynamically.

The prompt is sent to Gemini API.

AI returns a formatted learning roadmap.

The roadmap is displayed and can be downloaded.

🧠 Prompt Strategy

The model is instructed to generate:

Timeline (weeks/months)

Step-by-step topics

Projects

Tools

Free resources

Interview preparation plan

Low temperature (0.2) ensures:

Structured output

Less randomness

More reliable planning

🚀 Future Improvements

PDF export option

User authentication

Progress tracking dashboard

Skill-based leaderboard

AI-based roadmap refinement

College-level analytics dashboard

📂 Project Structure
├── app.py
├── roadmap_generator.py
├── .env
├── requirements.txt

🔐 Setup Instructions

Clone the repository

Install dependencies

Add your API key in .env file

Run:

streamlit run app.py
