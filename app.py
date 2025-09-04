from flask import Flask, render_template
from jinja2.exceptions import TemplateNotFound

app = Flask(__name__)

# 主页路由
@app.route('/')
def home():
    return render_template('index.html')

# 执行协作流程详细页面
@app.route('/execution_collaboration')
def execution_collaboration():
    return render_template('execution_collaboration.html')

# 供应管理流程详细页面
@app.route('/supply_management')
def supply_management():
    return render_template('supply_management.html')

# 付款、对账与返利流程详细页面
@app.route('/payments_reconcile_rebate')
def payments_reconcile_rebate():
    return render_template('payments_reconcile_rebate.html')

# 采购订单交付与零部件再平衡流程详细页面
@app.route('/po_delivery_parts_rebalance')
def po_delivery_parts_rebalance():
    return render_template('po_delivery_parts_rebalance.html')

# 采购申请与采购订单管理流程详细页面
@app.route('/pr_po_management')
def pr_po_management():
    return render_template('pr_po_management.html')

# 合同管理流程详细页面
@app.route('/contract_management')
def contract_management():
    return render_template('contract_management.html')

# 招投标与授标流程详细页面
@app.route('/source_to_award')
def source_to_award():
    return render_template('source_to_award.html')

# 供应商管理流程详细页面
@app.route('/supplier_management')
def supplier_management():
    return render_template('supplier_management.html')

# 成本管理流程详细页面
@app.route('/cost_management')
def cost_management():
    return render_template('cost_management.html')

# 采购来源管理流程详细页面
@app.route('/source_management')
def source_management():
    return render_template('source_management.html')

# 新产品管理流程详细页面
@app.route('/new_product_management')
def new_product_management():
    return render_template('new_product_management.html')

# 复杂性管理流程详细页面
@app.route('/complexity_management')
def complexity_management():
    return render_template('complexity_management.html')


@app.route('/best-practice/<process>/<module_name>')
def best_practice(process, module_name):
    # 安全过滤流程和模块名称
    safe_process = ''.join(e for e in process if e.isalnum() or e == '_')
    safe_module = ''.join(e for e in module_name if e.isalnum() or e == '_')
    #safe_module = ''.join(e for e in module_name if e.isalnum() or e == '_' or e == ' ')
    #safe_module = safe_module.replace(' ', '_') 
    
    # 构建模板路径
    template_path = f"best_practice/{safe_process}/{safe_module}.html"
    
    try:
        # 尝试渲染特定模板
        return render_template(template_path)
    except TemplateNotFound:
        try:
            # 尝试渲染默认模板
            return render_template('best_practice/default.html', 
                                  process=process,
                                  process_name=process.replace('_', ' ').title(),
                                  module=module_name,
                                  module_name=module_name.replace('_', ' ').title())
        except TemplateNotFound:
            # 如果默认模板也不存在，返回简单错误页面
            return f"""
            <h1>模板未找到</h1>
            <p>无法找到模板: {template_path}</p>
            <p>默认模板也不存在: best_practice/default.html</p>
            <p>请创建相应的模板文件。</p>
            """, 404
if __name__ == '__main__':
    app.run(debug=True)
