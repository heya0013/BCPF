from flask import Flask, render_template
from jinja2.exceptions import TemplateNotFound

app = Flask(__name__)

# 主页路由
@app.route('/')
def home():
    return render_template('procurement/index.html')  # 更新路径

# 其他路由也需要更新模板路径
@app.route('/execution_collaboration')
def execution_collaboration():
    return render_template('procurement/execution_collaboration.html')  # 更新路径

@app.route('/supply_management')
def supply_management():
    return render_template('procurement/supply_management.html')  # 更新路径

@app.route('/payments_reconcile_rebate')
def payments_reconcile_rebate():
    return render_template('procurement/payments_reconcile_rebate.html')  # 更新路径

@app.route('/po_delivery_parts_rebalance')
def po_delivery_parts_rebalance():
    return render_template('procurement/po_delivery_parts_rebalance.html')  # 更新路径

@app.route('/pr_po_management')
def pr_po_management():
    return render_template('procurement/pr_po_management.html')  # 更新路径

@app.route('/contract_management')
def contract_management():
    return render_template('procurement/contract_management.html')  # 更新路径

@app.route('/source_to_award')
def source_to_award():
    return render_template('procurement/source_to_award.html')  # 更新路径

@app.route('/supplier_management')
def supplier_management():
    return render_template('procurement/supplier_management.html')  # 更新路径

@app.route('/cost_management')
def cost_management():
    return render_template('procurement/cost_management.html')  # 更新路径

@app.route('/source_management')
def source_management():
    return render_template('procurement/source_management.html')  # 更新路径

@app.route('/new_product_management')
def new_product_management():
    return render_template('procurement/new_product_management.html')  # 更新路径

@app.route('/complexity_management')
def complexity_management():
    return render_template('procurement/complexity_management.html')  # 更新路径

# 最佳实践路由 - 更新模板路径
@app.route('/best-practice/<process>/<module_name>')
def best_practice(process, module_name):
    # 安全过滤流程和模块名称
    safe_process = ''.join(e for e in process if e.isalnum() or e == '_')
    safe_module = ''.join(e for e in module_name if e.isalnum() or e == '_')
    
    # 构建新的模板路径 - 添加到procurement目录下
    template_path = f"procurement/best_practice/{safe_process}_{safe_module}.html"
    
    try:
        # 尝试渲染特定模板
        return render_template(template_path,
                             process=process,
                             module_name=module_name)
    except TemplateNotFound:
        try:
            # 尝试渲染默认模板
            return render_template('procurement/best_practice/default.html', 
                                  process=process,
                                  process_name=process.replace('_', ' ').title(),
                                  module=module_name,
                                  module_name=module_name.replace('_', ' ').title())
        except TemplateNotFound:
            # 如果默认模板也不存在，返回简单错误页面
            return f"""
            <h1>模板未找到</h1>
            <p>无法找到模板: {template_path}</p>
            <p>默认模板也不存在: procurement/best_practice/default.html</p>
            <p>请创建相应的模板文件。</p>
            """, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
