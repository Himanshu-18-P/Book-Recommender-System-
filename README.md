# Book Recommender System

A Book Recommender System that utilizes Collaborative Filtering and Popularity-Based algorithms to provide personalized book recommendations.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Recommendation Strategies](#recommendation-strategies)
  - [1. Popularity-Based Recommendations](#1-popularity-based-recommendations)
  - [2. Collaborative Filtering Recommendations](#2-collaborative-filtering-recommendations)
- [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Customizing Recommendations](#customizing-recommendations)
- [Notes](#notes)
- [Acknowledgments](#acknowledgments)

## Overview

This project aims to provide users with book recommendations based on their reading preferences and popular trends. By analyzing user ratings and book data, the system suggests books that users are likely to enjoy.

## Project Structure

- **data/**: Contains datasets with information on books, user ratings, and user details.
- **recommender.ipynb**: Jupyter Notebook for Exploratory Data Analysis (EDA), data cleaning, and model preparation.
- **model.pkl**: The trained recommendation model saved after EDA and training.
- **app.py**: The main application file to run the recommender system.
- **requirements.txt**: Lists all Python dependencies required to run the project.
- **README.md**: This file, providing an overview and instructions for the project.

## Recommendation Strategies

### 1. Popularity-Based Recommendations

- **Objective**: Recommend books that are widely popular among all users.
- **Criteria**:
  - Books with a total rating count greater than **250**.
  - Books sorted by their average rating in descending order.
- **Implementation Steps**:
  1. Aggregate the total number of ratings for each book.
  2. Filter out books that do not meet the minimum rating count threshold.
  3. Compute the average rating for each remaining book.
  4. Sort the books based on average ratings.
  5. Select the top **50** books for recommendation.

### 2. Collaborative Filtering Recommendations

- **Objective**: Provide personalized recommendations based on user similarity.
- **Criteria**:
  - Include books that have received at least **50** ratings.
  - Include users who have rated at least **200** books.
- **Implementation Steps**:
  1. Create a pivot table (matrix) with users as columns and book titles as rows, filling the matrix with user ratings.
  2. Filter the matrix to include only the books and users that meet the criteria.
  3. Compute the cosine similarity between books based on user ratings.
  4. For a given book, find other books that are most similar.
  5. Recommend books that are most similar to the ones a user has rated highly.

## Installation

### Prerequisites

- **Python 3.10.8**
- **Jupyter Notebook** (optional, for running `recommender.ipynb`)

### Install Required Packages
- [pip install -r requirements.txt]
1. **Clone the repository**
- [git clone https://github.com/Himanshu-18-P/Book-Recommender-System-.git] 
2. **Navigate to the project directory**:
- [cd Book-Recommender-System-]
3. **Running the Application**:
- [python app.py]

## Acknowledgments
- Datasets: The project uses publicly available datasets for books and ratings.
- Algorithms: Leverages collaborative filtering techniques commonly used in recommendation systems.
- Community: Inspired by various open-source projects and tutorials in the data science community.