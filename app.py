from flask import Flask, request, jsonify
from transformers import T5ForConditionalGeneration, T5Tokenizer
import torch
import os
import re

app = Flask(__name__)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
checkpoint_path = os.path.join(BASE_DIR, "checkpoint")
tokenizer_path = os.path.join(BASE_DIR, "et5_model")


model = T5ForConditionalGeneration.from_pretrained(checkpoint_path)
tokenizer = T5Tokenizer.from_pretrained(tokenizer_path)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)


def split_sentences(text):
    return re.findall(r'[^.!?]+[.!?]?', text)

@app.route("/api/v1/recruit/wordcorrect", methods=["POST"])
def correct_text():
    data = request.get_json()
    input_text = data.get("text", "")

    if not input_text.strip():
        return jsonify({"error": "No text provided."}), 400

    
    sentences = split_sentences(input_text)

    corrected_sentences = []
    for sentence in sentences:
        sentence = sentence.strip()
        if sentence:
            input_ids = tokenizer.encode(sentence, return_tensors="pt").to(device)
            output_ids = model.generate(input_ids, max_length=128)
            corrected = tokenizer.decode(output_ids[0], skip_special_tokens=True)
            corrected_sentences.append(corrected)

    
    final_text = " ".join(corrected_sentences)

    return jsonify({
        "corrected_text": final_text,
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

