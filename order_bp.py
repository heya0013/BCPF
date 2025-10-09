from flask import Blueprint, render_template
from jinja2.exceptions import TemplateNotFound

# 创建蓝图，指定蓝图名称和模板文件夹
# 模板文件夹对应 templates/order_fulfillment（与主应用的 templates 目录相对）
order_bp = Blueprint(
    'order_fulfillment',  # 蓝图名称（url_for 时需用此名称作为前缀）
    __name__,
    template_folder='templates/order_fulfillment'  # 模板路径
)

# 主页路由（对应蓝图注册时的 url_prefix + '/'）
@order_bp.route('/')
def home():
    # 蓝图模板文件夹已指定为 order_fulfillment，直接写相对路径
    return render_template('index.html')

# 订单录入路由
@order_bp.route('/Order_Entry')
def Order_Entry():
    return render_template('Order_Entry.html')

# 订单优先级路由（修复原代码中的空格错误）
@order_bp.route('/Order_Prioritization')
def Order_Prioritization():
    return render_template('Order_Prioritization.html')  # 移除文件名中的空格

# 订单 sourcing 路由
@order_bp.route('/Order_Sourcing')
def Order_Sourcing():
    return render_template('Order_Sourcing.html')

# 订单承诺路由
@order_bp.route('/Order_Promise')
def Order_Promise():
    return render_template('Order_Promise.html')

# 订单排程路由（修复原代码中的空格错误）
@order_bp.route('/Order_Scheduling')
def Order_Scheduling():
    return render_template('Order_Scheduling.html')  # 移除文件名中的空格

# 账单与支付路由
@order_bp.route('/Billing_Payment')
def Billing_Payment():
    return render_template('Billing_Payment.html')

# 客户退货路由
@order_bp.route('/Customer_Return')
def Customer_Return():
    return render_template('Customer_Return.html')

# 履约控制塔路由
@order_bp.route('/Fulfill_Control_Tower')
def Fulfill_Control_Tower():
    return render_template('Fulfill_Control_Tower.html')

# 最佳实践路由
@order_bp.route('/best-practice/<process>/<module_name>')
def best_practice(process, module_name):
    # 安全过滤流程和模块名称
    safe_process = ''.join(e for e in process if e.isalnum() or e == '_')
    safe_module = ''.join(e for e in module_name if e.isalnum() or e == '_')
    
    # 模板路径基于蓝图的 template_folder（已包含 order_fulfillment）
    template_path = f"best_practice/{safe_process}/{safe_module}.html"
    default_template = "best_practice/default.html"
    
    try:
        return render_template(
            template_path,
            process=process,
            module_name=module_name
        )
    except TemplateNotFound:
        try:
            return render_template(
                default_template,
                process=process,
                process_name=process.replace('_', ' ').title(),
                module=module_name,
                module_name=module_name.replace('_', ' ').title()
            )
        except TemplateNotFound:
            return f"""
            <h1>模板未找到</h1>
            <p>无法找到特定模板: {template_path}</p>
            <p>默认模板不存在: {default_template}</p>
            <p>请在 order_fulfillment/best_practice/ 目录下创建模板文件。</p>
            """, 404
    