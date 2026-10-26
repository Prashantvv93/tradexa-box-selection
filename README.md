# AI-Assisted Shipping Box Selection System

## About the Project

This project helps an e-commerce warehouse select a suitable shipping box for a product.

The user provides the product's length, width, height, and weight. The system checks the available boxes and recommends the cheapest box that can fit the product.

If no box is suitable, the system returns a message saying that no suitable box was found.

## Technologies Used

- Python
- Django
- Django REST Framework
- SQLite
- Git and GitHub

## Features

- Store shipping box details.
- Check product dimensions and weight.
- Allow products to fit in different box orientations.
- Recommend the cheapest suitable box.
- Validate product input.
- Return a clear message if no box is suitable.
- Test the system using automated tests.

## How to Run the Project

### 1. Download or clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL
cd tradexa-box-selection

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create and activate a virtual environment

On Windows:

python -m venv venv
.\venv\Scripts\Activate.ps1

### 3. Install the required packages

python -m pip install -r requirements.txt


### 4. Apply database migrations

python manage.py migrate

### 5. Start the development server

python manage.py runserver

The server will run at:

http://127.0.0.1:8000/

## API Details

**Endpoint:** `POST /api/recommend/`

The API accepts product dimensions and weight as JSON.

### Example input

{
  "length": 25,
  "width": 15,
  "height": 10,
  "weight": 1
}

Dimensions are in centimetres, and weight is in kilograms.

### Example output

{
  "message": "Suitable shipping box found.",
  "box": {
    "name": "Medium",
    "length": "30.00",
    "width": "20.00",
    "height": "15.00",
    "max_weight": "5.00",
    "cost": "15.00"
  }
}

The exact decimal formatting in the response may vary depending on the current implementation.

## How to Run Tests

Run this command:

python manage.py test boxes


The current test suite contains six tests covering box selection, product rotation, weight limits, dimension limits, invalid input, and equal-cost box selection.

## Assumptions

- Box and product dimensions use centimetres.
- Product and box weights use kilograms.
- A product can be rotated to fit a box.
- The cheapest suitable box is selected.
- If two suitable boxes have the same cost, the box with the smaller volume is selected.

## Limitations

- The project currently provides a backend API, not a separate frontend.
- Shipping boxes must be added to the database before they can be recommended.
- The project uses SQLite for development.

## AI Usage

ChatGPT was used as a helper during development. Details about how AI was used are documented in `AI_USAGE.md`.
