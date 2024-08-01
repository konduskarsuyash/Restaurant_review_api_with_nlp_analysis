# Restaurant Review API

## Overview

This Restaurant Review API leverages NLP analysis to provide detailed insights into user reviews, offering features such as user authentication, sentiment analysis, and dynamic restaurant ratings. The project uses Django Rest Framework (DRF) and integrates advanced technologies like transformers and Redis for efficient processing.

## Features

- **User Authentication**: Secure authentication system to manage user accounts and reviews.
- **NLP Analysis**: Sentiment analysis of user comments using transformer models to determine the sentiment of each review.
- **Average Ratings**: Calculation of average ratings for each restaurant based on user reviews.
- **Top 5 Restaurants**: Dynamic display of the top 5 restaurants with the highest ratings, utilizing Redis for fast data retrieval.
- **Nearby Restaurants**: Find the nearest restaurants based on latitude and longitude coordinates.

## Tech Stack

- **Backend Framework**: Django Rest Framework (DRF)
- **NLP**: Transformers for sentiment analysis
- **Database**: PostgreSQL
- **Caching**: Redis for fast processing and data retrieval
- **Geolocation**: Integration for locating nearest restaurants

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/restaurant-review-api.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd restaurant-review-api
    ```
3. **Create a virtual environment**:
    ```bash
    python -m venv env
    ```
4. **Activate the virtual environment**:
    - On Windows:
        ```bash
        .\env\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source env/bin/activate
        ```
5. **Install the dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
6. **Apply migrations**:
    ```bash
    python manage.py migrate
    ```
7. **Run the server**:
    ```bash
    python manage.py runserver
    ```

## Usage

- **Register/Login**: Create an account or login to start reviewing restaurants.
- **Submit Reviews**: Add reviews and ratings for restaurants.
- **View Ratings**: See average ratings and top 5 restaurants based on user reviews.
- **Find Nearby Restaurants**: Enter your location to find the nearest restaurants.


## Contact

For any inquiries, please contact suyashkonduskar27@gmail.com or open an issue in the repository.

