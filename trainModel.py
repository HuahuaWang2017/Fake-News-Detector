import torch
from transformers import BertForSequenceClassification, BertTokenizer
from datasets import load_dataset

# Load dataset (Kaggle’s Fake News dataset)
dataset = load_dataset("csv", data_files="News_Dataset.csv")

# Load pre-trained BERT tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Tokenization function
def tokenize_function(examples):
    return tokenizer(examples["text"], padding="max_length", truncation=True)

# Apply tokenization to the entire dataset
tokenized_datasets = dataset.map(tokenize_function, batched=True)

# Load pre-trained BERT model
model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

# Define optimizer and loss function
optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)
loss_fn = torch.nn.CrossEntropyLoss()

# Training loop
epochs = 3
for epoch in range(epochs):
    for batch in tokenized_datasets["train"]:
        inputs = tokenizer(batch["text"], return_tensors="pt", padding=True, truncation=True)
        labels = torch.tensor(batch["label"]).unsqueeze(0)

        optimizer.zero_grad()
        outputs = model(**inputs)
        loss = loss_fn(outputs.logits, labels)
        loss.backward()
        optimizer.step()

# Save the trained model
model.save_pretrained("fake_news_model")
tokenizer.save_pretrained("fake_news_model")
print("Model training complete and saved!")
