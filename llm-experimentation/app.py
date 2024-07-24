import torch
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
from flask import Flask, request, render_template

app = Flask(__name__)

model_name = "bert-large-uncased-whole-word-masking-finetuned-squad"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForQuestionAnswering.from_pretrained(model_name)

def get_answer(question, text):

    inputs = tokenizer(question, text, return_tensors="pt")
    input_ids = inputs["input_ids"].tolist()[0]

    outputs = model(**inputs)
    start_scores = outputs.start_logits
    end_scores = outputs.end_logits

    answer_start = torch.argmax(start_scores)
    answer_end = torch.argmax(end_scores) + 1

    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(input_ids[answer_start:answer_end]))
    return answer

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/answer', methods=['POST'])
def answer():
    question = request.form['question']
    text = request.form['text']
    answer = get_answer(question, text)
    return render_template('index.html', question=question, text=text, answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
