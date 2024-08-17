# TimeLight

TimeLight is a time management and budgeting application intended to quantify and visualize what activities a user does, their expenses, and income.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- Track daily activities and their durations
- Record expenses and income
- Visualize activities and expenses
- User authentication and profile management

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/timelight.git
    cd timelight
    ```

2. Set up the virtual environment:
    ```sh
    python3 -m venv envs
    source envs/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Set the Flask application environment variable:
    ```sh
    source scripts/set_flask_app.sh
    ```

## Usage

1. Run the Flask application:
    ```sh
    flask run
    ```

2. Open your browser and navigate to `http://127.0.0.1:5000/`

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
