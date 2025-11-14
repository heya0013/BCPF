from flask import Blueprint, render_template
from jinja2.exceptions import TemplateNotFound

# 创建蓝图，指定模块名称和模板文件夹（已默认对应templates/esg）
esg_bp = Blueprint(
    'esg',  # 蓝图名称
    __name__,
    template_folder='templates/esg'  # 模板路径（相对于主app的templates）
)

# 主页路由（对应原/esg/）
@esg_bp.route('/')
def home():
    return render_template('Esg/index.html')  # 实际路径：templates/esg/index.html

# 其他路由（无需再写"esg/"前缀，蓝图会自动添加）
@esg_bp.route('/sustainable_products')
def sustainable_products():
    return render_template('sustainable_products.html')  # 实际路径：templates/esg/Sustainable Products.html

@esg_bp.route('/Sustainable_Value_Chain')
def Sustainable_Value_Chain():
    return render_template('Sustainable_Value_Chain.html')

@esg_bp.route('/Decarbonization')
def Decarbonization():
    return render_template('Decarbonization.html')

@esg_bp.route('/ESG_E2E_Management')
def ESG_E2E_Management():
    return render_template('ESG_E2E_Management.html')

# 最佳实践路由
@esg_bp.route('/best-practice/<process>/<module_name>')
def best_practice(process, module_name):
    # 保留原安全过滤逻辑
    safe_process = ''.join(e for e in process if e.isalnum() or e == '_')
    safe_module = ''.join(e for e in module_name if e.isalnum() or e == '_')
    
    # 模板路径已基于蓝图的template_folder，无需再写"esg/"
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
            <p>请在esg/best_practice/目录下创建模板文件。</p>
            """, 404