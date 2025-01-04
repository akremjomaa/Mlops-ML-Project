# Full-Stack Dockerized ML Project

This project demonstrates a full-stack machine learning application, fully containerized with Docker. The project includes:

- **Frontend**: A user-friendly Streamlit interface to interact with the ML model.
- **Backend**: A FastAPI-based API serving a classification model using the Iris dataset.

---

## Features
- Predict Iris species using ML model.
- Interactive user interface for model testing.
- API documentation via Swagger.

---

## Prerequisites
To run this project, ensure you have:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: [Install Docker Compose](https://docs.docker.com/compose/install/)

---

## Quick Start
Follow these steps to launch the project:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/akremjomaa/Mlops-ML-Project.git
   cd Mlops-ML-Project
   ```

2. **Build and start the services**:
   ```bash
   docker compose up --build
   ```

3. **Access the services**:
   - **API Swagger documentation**: [http://localhost:8000/docs](http://localhost:8000/docs)
   - **Streamlit App**: [http://localhost:8501](http://localhost:8501)

---

## Project Structure
- **Streamlit App**: Provides a simple UI for predictions.
- **FastAPI Backend**: Handles requests and predictions using the trained model.
- **Docker Compose**: Manages the project's containers for seamless deployment.

---

## Notes
- Ensure ports 8000 and 8501 are available on your machine.
- To stop the services, use:
   ```bash
   docker compose down
   ```
- To rebuild after updates, run:
   ```bash
   docker compose up --build
   ```

---

## About
This project was created as part of learning Docker and its integration with machine learning workflows. For questions or contributions, feel free to contact [Akrem Jomaa](https://github.com/akremjomaa).

---

**Happy Dockerizing!**
