from flask import Flask, render_template
from jinja2.exceptions import TemplateNotFound

app = Flask(__name__)

# 主页路由
@app.route('/')
def home():
    return render_template('supplier_collaboration/index.html')  # 更新路径

# 其他路由也需要更新模板路径
@app.route('/planning_collaboration')
def planning_collaboration():
    return render_template('supplier_collaboration/planning_collaboration.html')  # 更新路径

@app.route('/execution_collaboration')
def execution_collaboration():
    return render_template('supplier_collaboration/execution_collaboration.html')  # 更新路径

@app.route('/supply_perf_management')
def supply_perf_management():
    return render_template('supplier_collaboration/supply_perf_management.html')  # 更新路径

@app.route('/multi_tier_management_Visibility')
def multi_tier_management_Visibility():
    return render_template('supplier_collaboration/multi_tier_management_Visibilitynce.html')  # 更新路径


# 最佳实践路由 - 更新模板路径
@app.route('/best-practice/<process>/<module_name>')
def best_practice(process, module_name):
    # 安全过滤流程和模块名称（保留原有安全逻辑）
    safe_process = ''.join(e for e in process if e.isalnum() or e == '_')
    safe_module = ''.join(e for e in module_name if e.isalnum() or e == '_')
    
    # 固定指向supplier_collaboration目录（静态路径参数）
    template_path = f"supplier_collaboration/best_practice/{safe_process}/{safe_module}.html"
    default_template = "supplier_collaboration/best_practice/default.html"
    
    try:
        # 尝试渲染supplier_collaboration下的特定模板
        return render_template(template_path,
                             process=process,
                             module_name=module_name)
    except TemplateNotFound:
        try:
            # 尝试渲染supplier_collaboration下的默认模板
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
            <p>请在supplier_collaboration/best_practice/目录下创建模板文件。</p>
            """, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)