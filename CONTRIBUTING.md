# Contributing to Bedtime Story Generator

Thank you for considering contributing to **Bedtime Story Generator**! We welcome contributions of all kinds, from bug fixes and documentation to new features and ideas.

---

## Code of Conduct

This project adheres to the [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to maintain a welcoming and respectful environment for everyone.

---

## How You Can Contribute

### 1. Report Bugs

If you find a bug, please create an issue with the following details:
- A clear and descriptive title.
- Steps to reproduce the issue.
- Expected and actual results.
- Relevant logs or error messages.

### 2. Suggest Features

If you have a feature idea, create an issue titled "Feature Request:" followed by a short description. Include:
- The problem the feature solves.
- A potential implementation or example of how it could work.

### 3. Submit Code

If you're ready to write code, follow these steps:

#### Fork and Clone the Repository
1. Fork the project to your GitHub account.
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/bedtime-story-generator.git
   cd bedtime-story-generator
   ```

#### Create a Branch
Create a feature or bugfix branch:
```bash
git checkout -b your-branch-name
```

#### Make Changes
1. Write clean, well-documented code.
2. Follow the existing code style.
3. Test your changes locally.

#### Commit Changes
Write clear commit messages:
```bash
git commit -m "Add [description of your changes]"
```

#### Push Changes
Push your branch to your fork:
```bash
git push origin your-branch-name
```

#### Submit a Pull Request
1. Navigate to the original repository.
2. Click "New Pull Request".
3. Provide a clear description of your changes.

---

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/bedtime-story-generator.git
   cd bedtime-story-generator
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up environment variables in a `.env` file:
   ```env
   OPENAI_API_KEY=your_openai_api_key
   MONGO_URI=your_mongodb_connection_string
   ```
4. Run the server:
   ```bash
   uvicorn main:app --reload
   ```

---

## Coding Guidelines

### Python
- Follow **PEP 8** for Python code style.
- Use type annotations where appropriate.
- Write modular, reusable code.

### Documentation
- Add or update docstrings for all new functions or classes.
- If your feature impacts usage, update the relevant documentation files.

### Tests
- Add tests for new features or bug fixes.
- Use existing test files as references.

---

## Testing

1. Install testing dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```
2. Run tests using pytest:
   ```bash
   pytest
   ```

---

## Pull Request Process

1. Ensure all new code has tests.
2. Run all tests locally and ensure they pass.
3. Address any review feedback.
4. Once approved, your pull request will be merged by a maintainer.

---

## Acknowledgments

Thank you for your contributions!
