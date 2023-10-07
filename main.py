from fastapi import FastAPI
import spacy

app = FastAPI()

# Load the spaCy NER model
nlp_ner = spacy.load("model-best")

@app.post("/extract")
async def extract_categories(text: str):
    # Process the user input text
    doc = nlp_ner(text)

    # Initialize variables to store extracted data
    name = None
    cost = None
    sku = None
    size_quantity = []

    # Iterate through the entities and their labels
    for ent in doc.ents:
        if ent.label_ == "NAME":
            name = ent.text
        elif ent.label_ == "COST":
            cost = ent.text
        elif ent.label_ == "SKU":
            sku = ent.text
        elif ent.label_ == "SIZE X QUANTITY":
            size_quantity.append(ent.text)

    # Create a response dictionary
    response_data = {
        "name": name,
        "cost": cost,
        "sku": sku,
        "size_quantity": size_quantity
    }

    return response_data
