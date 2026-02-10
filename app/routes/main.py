from flask import Blueprint,jsonify

main_bp=Blueprint('main_bp',__name__)


# RF: O sistema deve permitir que um usuário se autentique para obter um token
@main_bp.route('/login',methods=['POST'])
def login():
    return jsonify({'message':'Rota de Login!'})

# RF: O sistema deve permitir listagem de todos os produtos
@main_bp.route('/products')
def get_products():
    return jsonify({"message":"Esta é a rota de listagem dos produtos"})

# RF: O sistema deve permitir a criacao de um novo produto
@main_bp.route('/products',methods=['POST'])
def create_product():
    return jsonify({"message":"Criando um novo produto"})

# RF: O sistema deve permitir a visualização dos detalhes de um unico produto
@main_bp.route('/product/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    return jsonify({'message':f'Vendo os detalhes de um único Produto {product_id}'})
# RF: O sistema deve permitir a atualização de um unico produto existente
@main_bp.route('/product/<int:product_id>',methods=['PUT'])
def put_product(product_id):
    return jsonify({'message':f'Rota de atualização de um produto com o ID{product_id}'})
# RF: O sistema deve permitir a deleção de um único produto e produto existente
@main_bp.route('/products/<int:product_id>',methods=['DELETE'])
def delete_product(product_id):
    return jsonify({'message':f'Deleta o produto com o ID {product_id}'})
# RF: O sistema deve permitir a importacao de vendas através de um arquivo
@main_bp.route('/sales/upload',methods=['POST'])
def upload_sales():
    return jsonify({'message':'upload de arquivos de vendas'})


@main_bp.route('/')
def index():
    return jsonify({"message":"Bem vindo ao StyleSync!"})


