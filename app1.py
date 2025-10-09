from flask import Flask, render_template

app = Flask(__name__)

# 主页面路由（新增）
@app.route('/')
def main_dashboard():
    # 无需传递复杂数据，仅作为入口
    return render_template('main.html')

# 以下是您已有的子页面路由（保持不变）
@app.route('/quality/')
def quality_index():
    # 您现有的quality页面逻辑
    return render_template('quality/index.html')

@app.route('/procurement/')
def procurement_index():
    # 您现有的procurement页面逻辑
    return render_template('procurement/index.html')

# 其他已有子页面路由...

if __name__ == '__main__':
    app.run(debug=True)
