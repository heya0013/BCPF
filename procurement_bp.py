from flask import Blueprint, render_template
from jinja2.exceptions import TemplateNotFound

# 创建procurement模块的蓝图
# 蓝图名称为'procurement'，模板文件夹指向'templates/procurement'
procurement_bp = Blueprint(
    'procurement',
    __name__,
    template_folder='templates/procurement'  # 模板根路径，内部路径可简化
)

# 主页路由（对应访问路径：/procurement/）
@procurement_bp.route('/')
def home():
    # 模板路径简化：相对于template_folder，直接写'index.html'
    return render_template('index.html')

# 执行协作页面
@procurement_bp.route('/execution_collaboration')
def execution_collaboration():
    return render_template('execution_collaboration.html')

# 供应管理页面
@procurement_bp.route('/supply_management')
def supply_management():
    return render_template('supply_management.html')

# 付款、对账与返利页面
@procurement_bp.route('/payments_reconcile_rebate')
def payments_reconcile_rebate():
    return render_template('payments_reconcile_rebate.html')

# 采购订单、交付与零件再平衡页面
@procurement_bp.route('/po_delivery_parts_rebalance')
def po_delivery_parts_rebalance():
    return render_template('po_delivery_parts_rebalance.html')

# 采购申请与订单管理页面
@procurement_bp.route('/pr_po_management')
def pr_po_management():
    return render_template('pr_po_management.html')

# 合同管理页面
@procurement_bp.route('/contract_management')
def contract_management():
    return render_template('contract_management.html')

# 寻源到授标页面
@procurement_bp.route('/source_to_award')
def source_to_award():
    return render_template('source_to_award.html')

# 供应商管理页面
@procurement_bp.route('/supplier_management')
def supplier_management():
    return render_template('supplier_management.html')

# 成本管理页面
@procurement_bp.route('/cost_management')
def cost_management():
    return render_template('cost_management.html')

# 寻源管理页面
@procurement_bp.route('/source_management')
def source_management():
    return render_template('source_management.html')

# 新产品管理页面
@procurement_bp.route('/new_product_management')
def new_product_management():
    return render_template('new_product_management.html')

# 复杂度管理页面
@procurement_bp.route('/complexity_management')
def complexity_management():
    return render_template('complexity_management.html')

# 最佳实践路由（模板路径基于蓝图的template_folder简化）
@procurement_bp.route('/best-practice/<process>/<module_name>')
def best_practice(process, module_name):
    # 安全过滤流程和模块名称
    safe_process = ''.join(e for e in process if e.isalnum() or e == '_')
    safe_module = ''.join(e for e in module_name if e.isalnum() or e == '_')
    
    # 模板路径简化：无需再写'procurement/'前缀（已由template_folder指定）
    template_path = f"best_practice/{safe_process}/{safe_module}.html"
    
    try:
        return render_template(template_path, process=process, module_name=module_name)
    except TemplateNotFound:
        try:
            # 默认模板路径同样简化
            return render_template(
                'best_practice/default.html',
                process=process,
                process_name=process.replace('_', ' ').title(),
                module=module_name,
                module_name=module_name.replace('_', ' ').title()
            )
        except TemplateNotFound:
            return f"""
            <h1>模板未找到</h1>
            <p>无法找到模板: {template_path}</p>
            <p>默认模板也不存在: best_practice/default.html</p>
            <p>请在procurement/best_practice/目录下创建模板文件。</p>
            """, 404
