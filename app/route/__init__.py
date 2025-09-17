from flask import Blueprint
test_bp = Blueprint('test', __name__, url_prefix='/api/v1/test')
main_bp = Blueprint('main', __name__, url_prefix='/api/v1/main')