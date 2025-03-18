# Upanishad Chatbot – Isha Upanishad Search  
This repository contains a chatbot that allows users to ask questions about the **Isha Upanishad**. The chatbot retrieves relevant verses, translations, and commentaries based on user queries using **FAISS** for similarity search and **Sentence Transformers** for embeddings.

---

## 🚀 Features
- Parses **Isha Upanishad** JSON file with Sanskrit verses, translations, and commentaries.
- Uses **Sentence Transformers** (`all-MiniLM-L6-v2`) to generate semantic embeddings.
- Implements **FAISS (Facebook AI Similarity Search)** for efficient nearest-neighbor search.
- Provides **instant answers** based on the closest matching verse.
- **Interactive CLI chatbot** for querying the Upanishad.

---

## 📂 Dataset
The chatbot reads data from `isha_upanishad.json`, which contains:
- **Verse numbers**  
- **Sanskrit text**  
- **Swami Vivekananda’s translation**  
- **Adi Shankaracharya’s commentary**  

---

## 🛠 Installation & Setup
1. **Clone this repository:**
   ```sh
   git clone https://github.com/yourusername/upanishad-chatbot.git
   cd upanishad-chatbot
   ```

2. **Install dependencies:**
   ```sh
   pip install faiss-cpu numpy tqdm sentence-transformers
   ```

3. **Download the Isha Upanishad JSON dataset**  
   Ensure that `isha_upanishad.json` is placed in the same directory.

4. **Run the chatbot:**
   ```sh
   python chatbot.py
   ```

---

## 🧠 How It Works
1. **Extracts verses** from `isha_upanishad.json` and formats them with translations & commentaries.
2. **Encodes verses** into **vector embeddings** using `all-MiniLM-L6-v2`.
3. **Indexes embeddings** with **FAISS** for fast retrieval.
4. **Processes user queries**, finds the closest matching verse, and returns it.

---

## 📝 Example Usage
```
You: What is the essence of the Isha Upanishad?
Bot:
Verse 1:
ॐ ईशा वास्यमिदं सर्वं यत्किञ्च जगत्यां जगत्।
तेन त्यक्तेन भुञ्जीथा मा गृधः कस्यस्विद्धनम्॥

Translation: This entire universe is pervaded by the Lord. Enjoy by renunciation and do not covet anyone's wealth.

Commentary: Adi Shankaracharya explains that true renunciation leads to liberation...
```

---

## 🔥 Future Improvements
- Add **multiple translations** from different scholars.
- Implement **web or mobile UI** for better accessibility.
- Extend to **other Upanishads** and Vedic texts.

---

## 📜 License
This project is open-source under the **MIT License**.

---

## 👨‍💻 Author
**[Your Name]**  
📧 sahilsinghrangra96@gmail.com  
🔗 [GitHub Profile](https://github.com/sahilrangra)  

🙏 Inspired by the wisdom of the Upanishads. 🚀
