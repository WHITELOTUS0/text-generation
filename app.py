from fastapi import FastAPI, HTTPException
from transformers import pipeline

# Create a new FastAPI app instance
# NOTE - we configure docs_url to serve the interactive Docs at the root path
# of the app. This way, we can use the docs as a landing page for the app on Spaces.
app = FastAPI(docs_url="/")

# Initialize the text generation pipeline
# This pipeline is able to generate text using the 
# google/flan-t5-small model.
pipe = pipeline("text2text-generation",
model="google/flan-t5-small")

# Define a function to handle the GET request at `/generate`
# This function will use the model to generate text based on the input text
# It also allows you to specify the maximum length of the generated text
@app.get("/generate")
def generate(text: str, max_length: int = 50):
    """
    Using the text2text-generation pipeline from `transformers`, generate text
    from the given input text. The model used is `google/flan-t5-small`, which
    can be found [here](<https://huggingface.co/google/flan-t5-small>).
    Args:
        text: Input text to generate from
        max_length: Maximum length of the generated output
    Returns:
        output: Json response containing the generated text
    """
    try:
         # Use the pipeline to generate text from the given input text
        output = pipe(text, max_length=max_length)
        # Return the generated text in a JSON response
        return {"output": output[0]["generated_text"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")