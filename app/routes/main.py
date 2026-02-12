from flask import Blueprint,jsonify, request
from app.models.user import LoginPayload
from pydantic import ValidationError
from app import db
from bson import ObjectId
from app.models.products import *

main_bp=Blueprint('main_bp',__name__)


# RF: O sistema deve permitir que um usuário se autentique para obter um token
@main_bp.route('/login',methods=['POST'])
def login():
    try:
        dados_body=request.get_json()
        user_data=LoginPayload(username=dados_body['username'],
                               password=dados_body['password'])
    except ValidationError as e:
        return jsonify({'error':e.errors()}),400
    except Exception as exp:
        return jsonify({'error':f'Erro[{exp.__class__}]'}),500
    
    if user_data.username == 'admin' and user_data.password == 'admin':
        return jsonify({'message':f'Logado com sucesso!'}),200

    return jsonify({'error':'credenciais incorretas'})
    


# RF: O sistema deve permitir listagem de todos os produtos
@main_bp.route('/products')
def get_products():
    products_cursor=db.products.find({})
    products_list=[ProductDBModel(**product).model_dump(by_alias=True,exclude_none=True) for product in products_cursor]
    return jsonify(products_list)

# RF: O sistema deve permitir a criacao de um novo produto
@main_bp.route('/products',methods=['POST'])
def create_product():
    return jsonify({"message":"Criando um novo produto"})

# RF: O sistema deve permitir a visualização dos detalhes de um unico produto
@main_bp.route('/product/<string:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    try:
        id=ObjectId(product_id)
    except Exception as e:
        return jsonify({'erro':f'erro ao transformar o id em ObjectId{product_id}: {e}'})

    product_get_id=db.products.find_one({'_id':id})
    
    if product_get_id:
        product_model=[ProductDBModel(**product_get_id).model_dump(by_alias=True,exclude_none=True)]
        return jsonify(product_model)
    return jsonify({'error':f'Produto {product_id} Não encontrado'})
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


