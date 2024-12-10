import os
import gradio as gr
from typing import Union
from ibm_watson import SpeechToTextV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

RESULTS_FOLDER = "transcriptions"

class SpeechToText:
    def __init__(self, api_key: str = None, url: str = None):
        """Initialization for Speech-to-Text service"""
        load_dotenv()
        self.url = url or os.environ.get("WATSONX_URL", "https://us-south.ml.cloud.ibm.com")
        self.api_key = api_key or os.environ.get("WATSONX_APIKEY")
        if not self.api_key:
            raise ValueError("API Key not provided. Set WATSONX_APIKEY in .env or pass it as a parameter.")

        # Authenticate
        self.client = SpeechToTextV1(authenticator=IAMAuthenticator(self.api_key))
        self.client.set_service_url(self.url)

    def transcribe_audio(self, audio_file_path: str, output_name: str = "transcription", format: str = "json") -> str:
        """Transcribes speech from an audio file"""
        if not os.path.exists(RESULTS_FOLDER):
            os.makedirs(RESULTS_FOLDER)

        output_path = os.path.join(RESULTS_FOLDER, f"{output_name}.{format}")
        with open(audio_file_path, "rb") as audio_file:
            response = self.client.recognize(
                audio=audio_file,
                content_type="audio/wav"
            ).get_result()

            with open(output_path, "w") as f:
                f.write(response)

        return output_path

def transcribe_audio_file(audio_path: str):
    recognizer = SpeechToText()
    try:
        output_path = recognizer.transcribe_audio(audio_path, "generated_transcription")
        return f"Transcription completed! File saved at: {output_path}", output_path
    except Exception as e:
        return f"Error: {str(e)}", None

# Gradio Application
def main():
    with gr.Blocks() as app:
        gr.Markdown("""# IBM Watson Speech-to-Text Generator
        Convert your speech into text using IBM Watson Speech-to-Text API. Upload an audio file and get the transcription.
        """)

        with gr.Row():
            audio_input = gr.Audio(label="Upload Audio", type="filepath")

        output_message = gr.Textbox(label="Status", interactive=False)
        transcription_output = gr.Textbox(label="Transcription", interactive=False)

        def transcribe(audio_path):
            message, path = transcribe_audio_file(audio_path)
            if path:
                with open(path, "r") as f:
                    transcription = f.read()
                return message, transcription
            return message, None

        transcribe_button = gr.Button("Transcribe Audio")
        transcribe_button.click(
            transcribe,
            inputs=[audio_input],
            outputs=[output_message, transcription_output],
        )

    app.launch()

if __name__ == "__main__":
    main()
