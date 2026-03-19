# 🎯 Smart Rexommendation: Book & Movie Explorer

An interactive Command Line Interface (CLI) tool that bridges the gap between literature and cinema. This project allows users to instantly retrieve detailed metadata, ratings, and plot summaries for millions of titles by connecting to real-world global databases.

---

## 🚀 Why this is "Intermediate" Level
Moving beyond basic Python scripts, this project demonstrates several core software development concepts:



* **External API Integration:** Consuming data from two different REST APIs (Google Books & OMDb).
* **Complex JSON Parsing:** Navigating nested dictionary structures to extract specific information.
* **Dynamic Data Handling:** Managing real-time user queries and providing formatted feedback.
* **Robust Logic Flow:** Implementing a continuous loop with exit conditions and input validation.

---

## 🛠️ Technical Stack
* **Language:** Python 3.x
* **Libraries:** `requests` (for HTTP calls), `json` (for data processing)
* **Data Sources:** * [Google Books API](https://developers.google.com/books)
    * [OMDb API (Open Movie Database)](http://www.omdbapi.com/)

---

## 📋 Features
* **Book Search:** Get author names, publication dates, genres, page counts, and full descriptions.
* **Movie Search:** Get release dates, runtime, IMDB ratings, and plot summaries.
* **Smart Navigation:** A simple menu system to switch between searching books or movies.
* **Detailed View:** Cleanly formatted console output for easy reading.

---

## 🔧 How to Run
1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/portfolio-projects.git](https://github.com/YOUR_USERNAME/portfolio-projects.git)
    cd python/intermediate-projects/smart-rex
    ```
2.  **Install Dependencies:**
    ```bash
    pip install requests
    ```
3.  **API Key Setup:**
    * Go to [OMDb API](http://www.omdbapi.com/apikey.aspx) and get a free API key.
    * Open the script and replace the `apikey` value with your actual key.
4.  **Launch:**
    ```bash
    python main.py
    ```


---

### 🌟 Future Roadmap
- [ ] Add a "Save to Favorites" feature using a CSV or SQL database.
- [ ] Refactor the code into modular functions for better maintainability.
- [ ] Implement `colorama` for a more colorful and modern CLI experience.
