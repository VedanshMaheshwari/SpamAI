# SpamAI

A machine learning project to classify email PDFs as SPAM or Non-SPAM using a trained model and a web interface.

## Project Structure

- `app/` — FastAPI backend for PDF upload and prediction
- `frontend/` — React frontend for user interaction
- `model/` — Saved model and vectorizer
- `data/` — Processed dataset (not included in repo)
- `train_model.ipynb` — Jupyter notebook for model training

## Setup Instructions

### 1. Clone the Repository
```sh
git clone <your-repo-url>
cd SpamAI
```

### 2. Backend Setup (FastAPI)
1. Create a virtual environment and activate it:
   ```sh
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On Mac/Linux:
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```sh
   pip install -r app/requirements.txt
   ```
3. Train the model (optional, if you want to retrain):
   - Open `train_model.ipynb` in Jupyter and run all cells.
4. Start the backend server:
   ```sh
   .venv\Scripts\uvicorn.exe app.main:app --reload
   ```
   The API will be available at `http://127.0.0.1:8000/` (see `/docs` for API docs).

### 3. Frontend Setup (React)
1. Open a new terminal and navigate to the `frontend` folder:
   ```sh
   cd frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the frontend development server:
   ```sh
   npm run dev
   ```
   The app will be available at `http://localhost:5173/` (or as shown in the terminal).

### 4. Usage
- Open the frontend in your browser.
- Upload a PDF email file to classify as SPAM or Non-SPAM.

### 5. Notes
- The backend expects the model files in `model/` and the processed data in `data/`.
- If you retrain, make sure to update the model files in `model/`.
- For production, configure CORS and environment variables as needed.

---

**Made for CyberML Project.**
