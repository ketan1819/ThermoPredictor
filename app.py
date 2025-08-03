import pandas as pd

# === Load the full dataset ===
df = pd.read_csv("data.csv")  # Replace with your actual file name

# === Randomly sample 100,000 rows ===
sampled_df = df.sample(n=20000, random_state=42)

# === Save the sampled dataset ===
sampled_df.to_csv("data1.csv", index=False)

print("✅ Saved 'data_100k.csv' with 100,000 random rows.")
