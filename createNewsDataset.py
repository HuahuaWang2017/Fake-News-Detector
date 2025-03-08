import pandas as pd

# Load the fake news dataset and assign label = 1 (Fake)
df_fake = pd.read_csv("Fake.csv")
df_fake["label"] = 1  # 1 = Fake news

# Load the real news dataset and assign label = 0 (Real)
df_true = pd.read_csv("True.csv")
df_true["label"] = 0  # 0 = Real news

# Combine both datasets
df_combined = pd.concat([df_fake, df_true], ignore_index=True)

# Shuffle the dataset to mix fake and real news
df_combined = df_combined.sample(frac=1, random_state=42).reset_index(drop=True)

df_combined.to_csv("News_Dataset.csv", index=False)
