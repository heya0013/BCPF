from flask import Flask, render_template
from jinja2.exceptions import TemplateNotFound

app = Flask(__name__)

# 主页路由
@app.route('/')
def home():
    return render_template('planning/start/index.html')

# 供应计划流程详细页面
@app.route('/supply_planning')
def supply_planning():
    return render_template('planning/start/supply_planning.html')

# 智能分配流程详细页面
@app.route('/smart_allocation')
def smart_allocation():
    return render_template('planning/start/smart_allocation.html')

# 可售库存流程详细页面
@app.route('/available_to_sell')
def available_to_sell():
    return render_template('planning/start/available_to_sell.html')

# 库存计划流程详细页面
@app.route('/inventory_planning')
def inventory_planning():
    return render_template('planning/start/inventory_planning.html')

# 网络规划流程详细页面
@app.route('/network_planning')
def network_planning():
    return render_template('planning/start/network_planning.html')

# 销售与运营计划流程详细页面
@app.route('/sales_operations_planning')
def sales_operations_planning():
    return render_template('planning/start/sales_operations_planning.html')

# 需求计划流程详细页面
@app.route('/demand_planning')
def demand_planning():
    return render_template('planning/start/demand_planning.html')

# 物料需求计划流程详细页面
@app.route('/mrp')
def mrp():
    return render_template('planning/start/mrp.html')

# 工厂计划流程详细页面
@app.route('/factory_planning')
def factory_planning():
    return render_template('planning/start/factory_planning.html')

# 部件预留流程详细页面
@app.route('/parts_reservation')
def parts_reservation():
    return render_template('planning/start/parts_reservation.html')

# 过渡计划流程详细页面
@app.route('/transition_planning')
def transition_planning():
    return render_template('planning/start/transition_planning.html')

# 负债管理流程详细页面
@app.route('/liability_management')
def liability_management():
    return render_template('planning/start/liability_management.html')

# 订单承诺流程详细页面
@app.route('/order_promising')
def order_promising():
    return render_template('planning/start/order_promising.html')

# 最佳实践路由 - 更新模板路径
@app.route('/best-practice/<process>/<module_name>')
def best_practice(process, module_name):
    # 安全过滤流程和模块名称
    safe_process = ''.join(e for e in process if e.isalnum() or e == '_')
    safe_module = ''.join(e for e in module_name if e.isalnum() or e == '_')
    
    # 构建新的模板路径 - 添加到Planning目录下
    template_path = f"planning/best_practice/{safe_process}/{safe_module}.html"
    
    try:
        # 尝试渲染特定模板
        return render_template(template_path,
                             process=process,
                             module_name=module_name)
    except TemplateNotFound:
        try:
            # 尝试渲染默认模板
            return render_template('planning/best_practice/default.html', 
                                  process=process,
                                  process_name=process.replace('_', ' ').title(),
                                  module=module_name,
                                  module_name=module_name.replace('_', ' ').title())
        except TemplateNotFound:
            # 如果默认模板也不存在，返回简单错误页面
            return f"""
            <h1>模板未找到</h1>
            <p>无法找到模板: {template_path}</p>
            <p>默认模板也不存在: planning/best_practice/default.html</p>
            <p>请创建相应的模板文件。</p>
            """, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)
