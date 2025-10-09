from flask import Flask, render_template

# 导入所有模块的蓝图（确保每个蓝图对象唯一）
from logistics_bp import logistics_bp
from quality_bp import quality_bp
from procurement_bp import procurement_bp
from supplier_bp import supplier_bp
from order_bp import order_bp

# 创建Flask应用
app = Flask(__name__)

# 注册蓝图（每个模块url_prefix唯一）
app.register_blueprint(procurement_bp, url_prefix='/procurement')
app.register_blueprint(logistics_bp, url_prefix='/logistics')
app.register_blueprint(order_bp, url_prefix='/order')
app.register_blueprint(quality_bp, url_prefix='/quality')
app.register_blueprint(supplier_bp, url_prefix='/supplier')

# 主页面路由（模块卡片入口）
@app.route('/')
def main_dashboard():
    return render_template('main.html')  # 主页面模板

# 启动时打印所有路由（用于调试验证）
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006, debug=True)
    
    