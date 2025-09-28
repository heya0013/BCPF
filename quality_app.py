from flask import Flask, render_template
from jinja2.exceptions import TemplateNotFound

app = Flask(__name__)

# 主页路由
@app.route('/')
def home():
    return render_template('quality/index.html')  # 更新路径

# 其他路由也需要更新模板路径
@app.route('/Supply_Chain_Quality_Management')
def Supply_Chain_Quality_Management():
    return render_template('quality/Supply_Chain_Quality_Management.html')  # 更新路径

@app.route('/Product_Lifecycle_Management')
def Product_Lifecycle_Management():
    return render_template('quality/Product_Lifecycle_Management.html')  # 更新路径

@app.route('/Customer_Experience_Management')
def Customer_Experience_Management():
    return render_template('quality/Customer_Experience_Management.html')  # 更新路径

@app.route('/Foundation_Process')
def Foundation_Process():
    return render_template('quality/Foundation_Process.html')  # 更新路径


# 最佳实践路由 - 更新模板路径
@app.route('/best-practice/<process>/<module_name>')
def best_practice(process, module_name):
    # 安全过滤流程和模块名称（保留原有安全逻辑）
    safe_process = ''.join(e for e in process if e.isalnum() or e == '_')
    safe_module = ''.join(e for e in module_name if e.isalnum() or e == '_')
    
    # 固定指向quality目录（静态路径参数）
    template_path = f"quality/best_practice/{safe_process}/{safe_module}.html"
    default_template = "quality/best_practice/default.html"
    
    try:
        # 尝试渲染quality下的特定模板
        return render_template(template_path,
                             process=process,
                             module_name=module_name)
    except TemplateNotFound:
        try:
            # 尝试渲染quality下的默认模板
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
            <p>请在quality/best_practice/目录下创建模板文件。</p>
            """, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004, debug=True)