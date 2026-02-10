from flask import Blueprint,jsonify

main_bp=Blueprint('main_bp',__name__)

@main_bp.route('/')
def index():
    return jsonify({"message":"Bem vindo ao StyleSync!"})

@main_bp.route('/products')
def get_products():
    return jsonify({"message":"Esta é a rota de listagem dos produtos"})

@main_bp.route('/login',methods=['POST'])
def login():
    return jsonify({'message':'Rota de Login!'})