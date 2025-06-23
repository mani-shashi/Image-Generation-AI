from transformers import CLIPTokenizer

class TextPreprocessor:
    def __init__(self, tokenizer_name="openai/clip-vit-base-patch32"):
        self.tokenizer = CLIPTokenizer.from_pretrained(tokenizer_name)

    def preprocess_text(self, prompt: str, max_length: int = 77):
        """Tokenize and encode text prompt."""
        inputs = self.tokenizer(
            prompt, 
            padding="max_length", 
            max_length=max_length, 
            truncation=True, 
            return_tensors="pt"
        )
        return inputs.input_ids, inputs.attention_mask