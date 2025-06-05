from flask import Flask

app = Flask(__name__)

@app.get('/health_check')
def health_check():
    return "Successul API health check!"


if __name__ == "__main__":
    app.host("0.0.0.0", port='6060')