import chromadb

# Connect to the persistent vector DB
chroma_client = chromadb.PersistentClient(path=".chroma")

# 🔥 Drop the collection completely
chroma_client.delete_collection("street_fairy_kb")

print("✅ 'street_fairy_kb' collection deleted.")