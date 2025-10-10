# logistics_bp.py
from flask import Blueprint, render_template
from jinja2.exceptions import TemplateNotFound

# 创建蓝图，指定模块名称和模板文件夹（已默认对应templates/logistics）
logistics_bp = Blueprint(
    'logistics',  # 蓝图名称
    __name__,
    template_folder='templates/logistics'  # 模板路径（相对于主app的templates）
)

# 主页路由（对应原/logistics/）
@logistics_bp.route('/')
def home():
    return render_template('logi/index.html')  # 实际路径：templates/logistics/index.html

# 其他路由（无需再写"logistics/"前缀，蓝图会自动添加）
@logistics_bp.route('/warehouse_management')
def warehouse_management():
    return render_template('warehouse_management.html')  # 实际路径：templates/logistics/warehouse_management.html

@logistics_bp.route('/transportation_management')
def transportation_management():
    return render_template('transportation_management.html')

@logistics_bp.route('/MFG')
def MFG():
    return render_template('MFG.html')

@logistics_bp.route('/logistics_Operation_Center')
def logistics_Operation_Center():
    return render_template('logistics_Operation_Center.html')

@logistics_bp.route('/Import_Export')
def Import_Export():
    return render_template('Import_Export.html')

@logistics_bp.route('/Global_Trade_Compliance')
def Global_Trade_Compliance():
    return render_template('Global_Trade_Compliance.html')

# 最佳实践路由
@logistics_bp.route('/best-practice/<process>/<module_name>')
def best_practice(process, module_name):
    # 保留原安全过滤逻辑
    safe_process = ''.join(e for e in process if e.isalnum() or e == '_')
    safe_module = ''.join(e for e in module_name if e.isalnum() or e == '_')
    
    # 模板路径已基于蓝图的template_folder，无需再写"logistics/"
    template_path = f"best_practice/{safe_process}/{safe_module}.html"
    default_template = "best_practice/default.html"
    
    try:
        return render_template(template_path, process=process, module_name=module_name)
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
            <p>请在logistics/best_practice/目录下创建模板文件。</p>
            """, 404