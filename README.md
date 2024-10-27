# Simple Flask Todo App with logging mechanism of RabbitMQ

This is a simple Flask Todo App using SQLAlchemy and SQLite database.

For styling, [semantic-ui](https://semantic-ui.com/) is used.

### Setup

#### Activate the Virtual Environment

On Unix-based systems:
```console
$ . venv/bin/activate
```

On Windows:
```console
$ venv\Scripts\activate
```

#### Set Environment Variables in Terminal

On Unix-based systems:
```console
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
```

On Windows:
```console
$ set FLASK_APP=app.py
$ set FLASK_ENV=development
```

#### Install Flask and Flask-SQLAlchemy

```console
$ pip install Flask
$ pip install Flask-SQLAlchemy
```

#### Install Pika

```console
$ pip install pika
```

### Step 1: Install RabbitMQ

#### Install Erlang

RabbitMQ requires Erlang to be installed. Download the Erlang installer from the [Erlang Solutions website](https://www.erlang-solutions.com/resources/download.html).
Run the installer and follow the instructions to complete the installation.

#### Install RabbitMQ

Download the RabbitMQ installer from the [RabbitMQ website](https://www.rabbitmq.com/install-windows.html).
Run the installer and follow the instructions to complete the installation.

### Step 2: Set Up RabbitMQ

#### Add RabbitMQ to the System Path

1. Open the Start Menu, search for "Environment Variables", and select "Edit the system environment variables".
2. In the System Properties window, click on the "Environment Variables" button.
3. In the Environment Variables window, find the "Path" variable in the "System variables" section and click "Edit".
4. Add the path to the RabbitMQ `sbin` directory (e.g., `C:\Program Files\RabbitMQ Server\rabbitmq_server-<version>\sbin`) to the list of paths.

#### Enable RabbitMQ Management Plugin

Open Command Prompt as Administrator and run the following command to enable the RabbitMQ management plugin:

```console
$ rabbitmq-plugins enable rabbitmq_management
```

#### Run the RabbitMQ Server

```console
$ rabbitmq-server
```

### Run the App

Activate the virtual environment and run the Flask app:

```console
$ . venv/bin/activate
$ python app.py
```

### Run the Log Consumer

Activate the virtual environment and run the log consumer script:

```console
$ . venv/bin/activate
$ python log_consumer.py
```

