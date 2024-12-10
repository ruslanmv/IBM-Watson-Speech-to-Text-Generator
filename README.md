# IBM Watson Speech-to-Text Generator

This project is a Gradio-based application that utilizes IBM Watson's Speech-to-Text API to convert audio files into text transcriptions. Users can upload an audio file, and the application will process and display the transcription.

## Features
- Converts speech from audio files into text using IBM Watson's Speech-to-Text API.
- Provides a user-friendly interface built with Gradio.
- Supports audio file upload and transcription.
- Saves transcriptions in a local folder for later use.

## Requirements
- Python 3.8+
- IBM Cloud account with access to the Speech-to-Text service.
- `.env` file with the following keys:
  ```env
  WATSONX_APIKEY=your_ibm_cloud_api_key
  WATSONX_URL=https://us-south.ml.cloud.ibm.com
  ```

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Set Up a Virtual Environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the Environment**:
   Create a `.env` file in the root directory and add your IBM Watson API credentials:
   ```env
   WATSONX_APIKEY=your_ibm_cloud_api_key
   WATSONX_URL=https://us-south.ml.cloud.ibm.com
   ```

## Running the Application

1. **Start the Application**:
   ```bash
   python3 main.py
   ```

2. **Access the Interface**:
   Open your browser and go to:
   ```
   http://127.0.0.1:7860
   ```

3. **Transcribe Audio**:
   - Upload an audio file in WAV format.
   - Click "Transcribe Audio" to generate and view the transcription.

## Folder Structure
- `transcriptions/`: Stores the generated transcription files.
- `.env`: Contains your API credentials.
- `main.py`: The main Python script for running the application.

## Example Usage
After starting the application:
1. Upload an audio file (e.g., `sample_audio.wav`).
2. Click "Transcribe Audio."
3. View the transcription in the output textbox or access the saved transcription file in the `transcriptions/` folder.

## Notes
- Ensure you have an active IBM Cloud account and a valid API key.
- The `transcriptions/` folder will be created automatically if it doesn't exist.
- The application currently supports WAV audio files.

## Dependencies
- `gradio`
- `ibm-watson`
- `python-dotenv`

Install them with:
```bash
pip install gradio ibm-watson python-dotenv
```



## Contributing
Feel free to submit issues and pull requests for improvements or new features.


