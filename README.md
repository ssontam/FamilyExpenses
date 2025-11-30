# Flask + HTMX Application Starter

This is a simple starter application using Flask (Python backend) and HTMX (Frontend interactivity). It is designed to be a clean starting point for building web applications with a separation of concerns.

## Architecture Flow

1.  **User Request**: The user visits a URL (e.g., `/`).
2.  **Flask Route**: The request is handled by a route in `app/routes/`.
3.  **Template Rendering**: Flask renders an HTML template from `app/templates/`.
4.  **HTMX Interactivity**: The HTML contains HTMX attributes (like `hx-get`). When a user interacts (e.g., clicks a button), HTMX sends a background request to the server.
5.  **Partial Update**: The server responds with a snippet of HTML, and HTMX swaps it into the page without a full reload.

## Project Structure

-   `app/`: Contains the application code.
    -   `__init__.py`: The Application Factory. Initializes the app and DB.
    -   `models/`: Database models (SQLAlchemy).
    -   `routes/`: Route definitions (Blueprints).
    -   `templates/`: HTML templates.
    -   `static/`: CSS, JS, images.
-   `config.py`: Configuration settings (Database URL, Secret Key).
-   `run.py`: The entry point to run the application.
-   `requirements.txt`: List of Python dependencies.

## Setup & Running

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Application**:
    ```bash
    python run.py
    ```

3.  **View in Browser**:
    Open `http://localhost:5000`

## Database Setup (Future)

The application is configured to use SQLAlchemy.
-   Currently, it defaults to SQLite for simplicity.
-   To use MySQL, update `SQLALCHEMY_DATABASE_URI` in `config.py` with your MySQL connection string:
    `mysql+pymysql://username:password@localhost/db_name`
