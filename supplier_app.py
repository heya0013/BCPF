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
    # 安全过滤流程和模块名称
    safe_process = ''.join(e for e in process if e.isalnum() or e == '_')
    safe_module = ''.join(e for e in module_name if e.isalnum() or e == '_')
    
    # 构建新的模板路径 - 添加到supplier_collaboration目录下
    template_path = f"supplier_collaboration/best_practice/{safe_process}_{safe_module}.html"
    
    try:
        # 尝试渲染特定模板
        return render_template(template_path,
                             process=process,
                             module_name=module_name)
    except TemplateNotFound:
        try:
            # 尝试渲染默认模板
            return render_template('supplier_collaboration/best_practice/default.html', 
                                  process=process,
                                  process_name=process.replace('_', ' ').title(),
                                  module=module_name,
                                  module_name=module_name.replace('_', ' ').title())
        except TemplateNotFound:
            # 如果默认模板也不存在，返回简单错误页面
            return f"""
            <h1>模板未找到</h1>
            <p>无法找到模板: {template_path}</p>
            <p>默认模板也不存在: supplier_collaboration/best_practice/default.html</p>
            <p>请创建相应的模板文件。</p>
            """, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)