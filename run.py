from app import app
from config import Config


if __name__ == '__main__':
    app.run(debug=True, port=Config.PORT, host='0.0.0.0')