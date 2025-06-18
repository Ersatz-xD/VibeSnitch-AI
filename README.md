# Vibe Snitch — Personality Prediction Desktop App

---

## 🧠 What Is Vibe Snitch?

Vibe Snitch is a modern **desktop application** that predicts a user’s **MBTI personality type** based on five short text inputs (e.g., social media posts). It combines a trained machine learning model with Gemini AI to deliver rich personality insights, including top traits, confidence levels, and relationship behaviors.

Built with **Python** and **PyQt** for the GUI, and **MySQL** for persistent data storage.

---

## 🚀 Features

| Feature                   | Description                                      |
| ------------------------- | ------------------------------------------------ |
| **User Authentication**   | Login and signup with secure MySQL backend       |
| **Input Window**          | Enter name and five posts to analyze              |
| **Prediction Window**     | Displays MBTI result, personality summary, traits, confidence, and relationship insights |
| **Saved Results**         | View previously saved personality predictions    |
| **ML Model Integration**  | Predict MBTI type using a pre-trained pipeline   |
| **Gemini AI Integration** | Generates detailed personality analysis          |
| **Modern UI**             | Sleek, intuitive PyQt interface with dark theme  |

---

## 🗂 Project Structure Overview

- **MainShell.py** — Hosts all windows inside a `QStackedWidget`, manages navigation and user context.
- **InputWindow.py** — Collects user input: name and posts.
- **PredictionWindow.py** — Shows MBTI prediction and detailed Gemini report.
- **SavedResultsWindow.py** — Dynamically displays saved prediction cards.
- **db_manager.py** — Handles all MySQL database connections and queries.
- **models/** — Contains saved ML pipeline model (`personality_pipeline_lr.pkl`).
- **ui_files/** — Qt Designer `.ui` files.
- **ai/** — Contains files to interact with gemini and clean texts before sending to AI model.

---

## 🔧 Setup & Installation

### Requirements

- Python 3.8+
- PyQt5
- MySQL server
- Required Python packages (install via pip):

```bash
pip install -r requirements.txt
````

### Environment Variables Setup

Create a .env file in the project root with the following variables to configure your database and Gemini API access:

```env
DB_HOST=your_database_host
DB_USER=your_database_username
DB_PASSWORD=your_database_password
DB_NAME=your_database_name

GEMINI_API_KEY=your_gemini_api_key
````
Make sure to replace the placeholders with your actual credentials

### Database Setup

Create the MySQL database and tables:

```sql
CREATE DATABASE vibe_snitch;

USE vibe_snitch;

CREATE TABLE users (
  user_id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(50) UNIQUE NOT NULL,
  password VARCHAR(255) NOT NULL
);

CREATE TABLE results (
  result_id INT PRIMARY KEY AUTO_INCREMENT,
  user_id INT NOT NULL,
  personality_type VARCHAR(10) NOT NULL,
  confidence_level VARCHAR(20) NOT NULL,
  top_traits VARCHAR(255) NOT NULL,
  relationship_behavior TEXT NOT NULL,
  saved_on TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Run the App

1. Clone this repository.
2. Configure credentials in `.env`.
3. Launch the Vbe Snitch:

```bash
python VibeSnitch.py
```

---

## 🧠 How It Works

1. User logs in or signs up.
2. User inputs their name and five short posts.
3. App combines posts and sends text to the ML pipeline to predict MBTI type.
4. The predicted MBTI type and posts are sent to Gemini AI for a detailed personality report.
5. The app displays results including:

   * MBTI type label
   * Personality summary
   * Confidence level (High/Medium/Low)
   * Top personality traits
   * Relationship behavior paragraph
   * Compatible personality types
     
6. Results are saved automatically to MySQL.
7. User can view saved results in a dedicated window.

---

## 🛠 Technology Stack

| Component            | Technology            |
| -------------------- | --------------------- |
| Frontend GUI         | Python + PyQt5        |
| Machine Learning     | Scikit-learn pipeline |
| Personality Analysis | Gemini AI API         |
| Database             | MySQL                 |
| Model Persistence    | Pickle files          |


---

## 📬 Contact

For questions or contributions, please contact: [My LinkedIn](https://linkedin.com/in/ayaan-ahmed-khan-448600351).

---

Thank you for trying out **Vibe Snitch** — uncover your vibe, one post at a time! 🚀

