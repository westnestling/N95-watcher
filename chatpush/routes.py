from flask import Blueprint
from flask import render_template

route_bp = Blueprint('route', __name__)


@route_bp.route('/')
def index():
    # 显示登陆状态
    # return 'Hello, World!'
    return render_template('index.html')

# 发送消息
@route_bp.route('/send', methods=['POST'])
def send_msg():
    pass
