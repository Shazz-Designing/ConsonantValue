# ConsonantValue

A Python project for calculating the highest value of consonant substrings in a lowercase string.

## Description

This project provides a Python function, `solve`, which calculates the highest value of consonant substrings in a given lowercase string. Consonants are any letters of the alphabet except "aeiou". Each consonant is assigned a value: a = 1, b = 2, c = 3, ..., z = 26.

## Features

- Calculate the highest value of consonant substrings
- Easy-to-use Python function

## Prerequisites

1. Python (version 3.x)
2. Git (optional, for version control)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Shazz-Designing/ConsonantValue.git

2. Navigate to the project directory:

   ```bash
   cd ConsonantValue

3. Create and activate a virtual environment 

    ```bash
    python -m venv venv
    .\venv\Scripts\Activate   # On Windows

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt


## Usage

1. Import the solve function from the app module:

    ```python
    from app import solve

2. Use the function to calculate the highest value of consonant substrings:

    ```python
    result = solve("zodiacs")
    print(f"The highest value of consonant substrings is: {result}")

## Testing

Consider writing tests for your code using a testing framework like pytest. Organize your tests in a separate directory (e.g., tests/).

To run tests, use the following command:

    pytest


## Contributing

Feel free to contribute to this project. Fork the repository, make your changes, and submit a pull reques


## License
This project is licensed under the MIT License.


