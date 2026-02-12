from flask import Blueprint,jsonify

category_bp=Blueprint('/category',__name__)

# RF: Visualizar categoria
@category_bp.route('/category')
def get_category():
    return jsonify({'message':'Listando Categorias...'})
# RF: Verificar dados da categoria
@category_bp.route('/category/<int:category_id>')
def get_category_id(category_id):
    return jsonify({'message':f'Dados da categoria com ID {category_id}'})
# RF: Adicionar categoria
@category_bp.route('/category/',methods=['POST'])
def add_category():
    return jsonify({'message': 'adicionando uma nova categoria'})
# RF: Atualizar categoria
@category_bp.route('/category/<int:category_id>',methods=['PUT'])
def update_category(category_id):
    return jsonify({'message':f'Atualizando categoria com ID {category_id}'})
# RF: Deletar Categoria
@category_bp.route('/category/<int:category_id>',methods=['DELETE'])
def deletar_categoria(category_id):
    return jsonify({'message':f'Categoria com ID {category_id} foi deletada.'})