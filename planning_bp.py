from flask import Blueprint, render_template
from jinja2.exceptions import TemplateNotFound

# 创建蓝图对象，指定模板文件夹为"Planning"
planning_bp = Blueprint(
    'planning',  # 蓝图名称
    __name__,
    template_folder="templates/planning"  # 保持原有的模板文件夹配置
)

# 主页路由
@planning_bp.route('/')
def home():
    return render_template('start/index.html')

# 供应计划流程详细页面
@planning_bp.route('/supply_planning')
def supply_planning():
    return render_template('start/supply_planning.html')

# 智能分配流程详细页面
@planning_bp.route('/smart_allocation')
def smart_allocation():
    return render_template('start/smart_allocation.html')

# 可售库存流程详细页面
@planning_bp.route('/available_to_sell')
def available_to_sell():
    return render_template('start/available_to_sell.html')

# 库存计划流程详细页面
@planning_bp.route('/inventory_planning')
def inventory_planning():
    return render_template('start/inventory_planning.html')

# 网络规划流程详细页面
@planning_bp.route('/network_planning')
def network_planning():
    return render_template('start/network_planning.html')

# 销售与运营计划流程详细页面
@planning_bp.route('/sales_operations_planning')
def sales_operations_planning():
    return render_template('start/sales_operations_planning.html')

# 需求计划流程详细页面
@planning_bp.route('/demand_planning')
def demand_planning():
    return render_template('start/demand_planning.html')

# 物料需求计划流程详细页面
@planning_bp.route('/mrp')
def mrp():
    return render_template('start/mrp.html')

# 工厂计划流程详细页面
@planning_bp.route('/factory_planning')
def factory_planning():
    return render_template('start/factory_planning.html')

# 部件预留流程详细页面
@planning_bp.route('/parts_reservation')
def parts_reservation():
    return render_template('start/parts_reservation.html')

# 过渡计划流程详细页面
@planning_bp.route('/transition_planning')
def transition_planning():
    return render_template('start/transition_planning.html')

# 负债管理流程详细页面
@planning_bp.route('/liability_management')
def liability_management():
    return render_template('start/liability_management.html')

# 订单承诺流程详细页面
@planning_bp.route('/order_promising')
def order_promising():
    return render_template('start/order_promising.html')


# 最佳实践路由 - 保持原逻辑但适配蓝图
@planning_bp.route('/best-practice/<process>/<module_name>')
def best_practice(process, module_name):
    # 安全过滤流程和模块名称
    safe_process = ''.join(e for e in process if e.isalnum() or e == '_')
    safe_module = ''.join(e for e in module_name if e.isalnum() or e == '_')
    
    # 构建模板路径（相对于蓝图的template_folder="Planning"）
    template_path = f"best_practice/{safe_process}/{safe_module}.html"
    
    try:
        # 尝试渲染特定模板
        return render_template(template_path,
                             process=process,
                             module_name=module_name)
    except TemplateNotFound:
        try:
            # 尝试渲染默认模板（修正路径，相对于Planning文件夹）
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
    
