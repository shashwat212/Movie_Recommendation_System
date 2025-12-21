# 🎬 MyDailyWork_Task3_Movie_Recommendation_System

A **content-based movie recommendation system** built using **Python** that suggests similar movies based on genre, actors, directors, and awards.

---

## 📌 Project Description

This project demonstrates a **movie recommendation system** that interacts with users and provides personalized movie suggestions based on their selected movie.
It uses **content-based filtering** to compare multiple attributes and recommend movies with similar characteristics.

The project focuses on understanding the basics of **recommendation systems, similarity scoring, and user interaction handling**.

---

## ✨ Features

* 👋 Displays a welcome message when the program starts
* 📽️ Shows a list of available movies with details
* 🎯 Recommends the **top 10 most similar movies**
* 🎭 Uses multiple similarity factors:

  * Genre
  * Actor
  * Director
  * Awards
* ❌ Politely handles cases when a movie is not found
* 🔁 Allows multiple searches without restarting the program
* 👋 Exits safely with a friendly goodbye message

---

## 🛠️ Technologies Used

* **Python**
* **Content-Based Filtering**

---

## ▶️ How to Run the Project

1. **Clone the repository**

   ```bash
   git clone <your-repo-link>
   ```

2. **Navigate to the project folder**

   ```bash
   cd MyDailyWork_Task3_Movie_Recommendation_System
   ```

3. **Run the recommender system**

   ```bash
   python movie_recommender.py
   ```

---

## 📂 Project Structure

```
MyDailyWork_Task3_Movie_Recommendation_System/
│── movie_recommender.py   # Main recommendation logic
│── README.md              # Project documentation
```

---

## ✅ Example Interaction

```
👉 Enter movie name: Inception

🎯 Top Movie Recommendations for 'Inception':

1. 🎬 Interstellar
   Genre   : Sci-Fi, Drama
   Actor   : Matthew McConaughey
   Director: Christopher Nolan
   Awards  : Oscar Winner
----------------------------------------

2. 🎬 The Dark Knight
   Genre   : Action, Drama
   Actor   : Christian Bale
   Director: Christopher Nolan
   Awards  : Oscar Winner
----------------------------------------

3. 🎬 Dune
   Genre   : Sci-Fi, Adventure
   Actor   : Timothée Chalamet
   Director: Denis Villeneuve
   Awards  : Oscar Winner
----------------------------------------
