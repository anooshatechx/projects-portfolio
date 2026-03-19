# 🌍 Bilingual Translator: English to Urdu/Roman Urdu

A smart translation tool that bridges the gap between English and Urdu. This project not only translates text using the **MyMemory API** but also provides a **Roman Urdu** option for users who can speak the language but may not read the script fluently.

---

## 🚀 Intermediate Skills Demonstrated
* **API Interaction:** Fetching real-time translations via REST API.
* **Data Processing:** Using the `urdu_roman` library to convert script into phonetic Romanized text.
* **User Interaction Logic:** Implementing a dynamic menu for output customization.

---

## 🛠️ Tech Stack
* **Language:** Python 3.x
* **Libraries:** `requests` (API calls), `urdu_roman` (Text romanization)
* **API:** [MyMemory Translation Service](https://mymemory.translated.net/doc/spec.php)

---

## 📋 Features
* **Real-time Translation:** Instantly converts English sentences to Urdu.
* **Dual Output Mode:**
    * **Simple Urdu:** Standard Urdu script.
    * **Roman Urdu:** Phonetic English-alphabet Urdu.
* **Looping Interface:** Perform multiple translations without restarting the script.

---

## 🔧 How to Run
1. **Install Dependencies:**
   ```bash
   pip install requests urdu-roman
