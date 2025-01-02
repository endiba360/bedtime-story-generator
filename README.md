# 🎨 Bedtime Story Generator

An open-source project that generates engaging short stories for bedtime using Python as the backend and OpenAI's ChatGPT for storytelling. This tool is perfect for creating personalized, age-appropriate tales to share with loved ones or enjoy on your own.

---

## 🔬 Features

- **🎨 Story Customization**:
  - Choose themes, characters, and story length.
  - Specify age groups and moral lessons.
- **🎧 Text-to-Speech Integration**:
  - Listen to your stories with natural-sounding audio.
- **📚 Save and Share**:
  - Save generated stories or share them with others.
- **🔄 Open Source**:
  - Built with extensibility and community contributions in mind.

---

## 🛠️ Tech Stack

- **Backend**: FastAPI
- **AI Integration**: OpenAI's GPT model
- **Database**: MongoDB
- **Frontend**: React/Vue.js
- **Text-to-Speech**: gTTS/pyttsx3
- **Deployment**: Docker, AWS/Heroku

---

## 🌐 Getting Started

### Prerequisites

1. **Python 3.9+** installed.
2. API key from [OpenAI](https://platform.openai.com/signup).
3. (Optional) MongoDB for storing user data and stories.
4. Docker (if you prefer containerized deployment).

### Setup

1. **🔧 Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/bedtime-story-generator.git
   cd bedtime-story-generator
   ```

2. **🔢 Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **🔐 Set Up Environment Variables**:
   Create a `.env` file with the following:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   MONGO_URI=your_mongodb_connection_string
   ```

4. **🚀 Run the Backend**:
   ```bash
   uvicorn main:app --reload
   ```

5. **🌐 Access the API**:
   Open `http://127.0.0.1:8000/docs` in your browser for API documentation.

---

## ✍️ Contributing

We welcome contributions! To get started:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes and push:
   ```bash
   git commit -m "Add feature description"
   git push origin feature-name
   ```
4. Submit a pull request.

Check out our [CONTRIBUTING.md](CONTRIBUTING.md) for more details.

---

## 🔒 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🔎 Roadmap

1. MVP: Basic story generation via API.
2. Add user profiles and saved stories feature.
3. Integrate text-to-speech functionality.
4. Build a frontend web app.
5. Open plugin system for new story genres.

---

## 📢 Contact

Have questions? Reach out via GitHub issues or email me at `endiba360@gmail.com`.
