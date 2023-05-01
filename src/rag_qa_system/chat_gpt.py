from transformers import pipeline

class ChatGPT:
    def __init__(self, model_name):
        self.model = pipeline("text-generation", model=model_name)

    def generate_answer(self, prompt, max_length=150):
        # Implement the function to generate an answer using the ChatGPT model
        pass
