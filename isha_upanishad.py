import json
import faiss
import numpy as np
from tqdm import tqdm
from sentence_transformers import SentenceTransformer

# Load JSON
with open("isha_upanishad.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Extract texts to train on
texts = []
verses = {}

for i, verse in enumerate(tqdm(data, desc="Extracting Verses", unit="verse")):
    verse_num = f"Verse {verse['verse']}:"
    sanskrit = verse['sanskrit']
    translation = verse['translations'].get('swami_vivekananda', '')
    commentary = verse['commentary'].get('adi_shankaracharya', '')

    combined_text = f"{verse_num}\n{sanskrit}\nTranslation: {translation}\nCommentary: {commentary}"
    
    texts.append(combined_text)
    verses[len(texts) - 1] = combined_text  # Store verse index

# Load transformer model
print("\nLoading sentence transformer model...")
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Encode text with progress tracking
print("\nEncoding verses into embeddings...")
embeddings = np.zeros((len(texts), model.get_sentence_embedding_dimension()))  # Pre-allocate array

for i in tqdm(range(len(texts)), desc="Embedding Progress", unit="verse"):
    embeddings[i] = model.encode(texts[i], convert_to_numpy=True)

# Create FAISS Index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

print("\n✅ Training completed! Chatbot is ready.")

# Chatbot function (retrieves trained data)
def chatbot(query):
    query_embedding = model.encode([query], convert_to_numpy=True)
    D, I = index.search(query_embedding, 1)  # Retrieve best match
    return verses[I[0][0]]

# Chatbot loop
print("\nUpanishad Chatbot Ready! Ask anything about the Isha Upanishad:")
while True:
    user_input = input("\nYou: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break
    response = chatbot(user_input)
    print(f"Bot:\n{response}")
