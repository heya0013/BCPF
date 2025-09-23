from flask import Flask, render_template
from jinja2.exceptions import TemplateNotFound

app = Flask(__name__)

# 主页路由
@app.route('/')
def home():
    return render_template('logistics/index.html')  # 更新路径

# 其他路由也需要更新模板路径
@app.route('/warehouse_management')
def warehouse_management():
    return render_template('logistics/warehouse_management.html')  # 更新路径

@app.route('/transportation_management')
def transportation_management():
    return render_template('logistics/transportation_management.html')  # 更新路径

@app.route('/MFG')
def MFG():
    return render_template('logistics/MFG.html')  # 更新路径

@app.route('/logistics_Operation_Center')
def logistics_Operation_Center():
    return render_template('logistics/logistics_Operation_Center.html')  # 更新路径

@app.route('/Import_Export')
def Import_Export():
    return render_template('logistics/Import_Export') 

@app.route('/Global_Trade_Compliance')
def Global_Trade_Compliance():
    return render_template('logistics/Global_Trade_Compliance') 

# 最佳实践路由 - 更新模板路径
@app.route('/best-practice/<process>/<module_name>')
def best_practice(process, module_name):
    # 安全过滤流程和模块名称（保留原有安全逻辑）
    safe_process = ''.join(e for e in process if e.isalnum() or e == '_')
    safe_module = ''.join(e for e in module_name if e.isalnum() or e == '_')
    
    # 固定指向logistics目录（静态路径参数）
    template_path = f"logistics/best_practice/{safe_process}/{safe_module}.html"
    default_template = "logistics/best_practice/default.html"
    
    try:
        # 尝试渲染logistics下的特定模板
        return render_template(template_path,
                             process=process,
                             module_name=module_name)
    except TemplateNotFound:
        try:
            # 尝试渲染logistics下的默认模板
            return render_template(default_template,
                                  process=process,
                                  process_name=process.replace('_', ' ').title(),
                                  module=module_name,
                                  module_name=module_name.replace('_', ' ').title())
        except TemplateNotFound:
            # 模板不存在时返回错误（明确指向supplier目录）
            return f"""
            <h1>模板未找到</h1>
            <p>无法找到特定模板: {template_path}</p>
            <p>supplier默认模板不存在: {default_template}</p>
            <p>请在logistics/best_practice/目录下创建模板文件。</p>
            """, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)