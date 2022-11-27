from flask import Blueprint, request, jsonify
from models.models import Usuario, Task, Role
from config.database import db

blue_print = Blueprint('app', __name__)


@blue_print.route('/', methods=['GET'])
def home():
    return jsonify({'message': 'Welcome to the API'})


@blue_print.route('/clasificar', methods=['POST'])
def clasificado():
    try:
        data = request.json.get('sin_clasificar')
        notdup = [x for i, x in enumerate(data) if i == data.index(x)]
        notdup.sort()
        dup = [x for i, x in enumerate(data) if i != data.index(x)]
        list_data = notdup + dup
        return jsonify({'sin_clasificar': data, 'clasificado': list_data}), 201
    except Exception as e:
        return jsonify({'message': 'Error', 'error': str(e)}), 500


@blue_print.route('/users', methods=['GET'])
def get_users():
    try:
        users = Usuario.query.all()
        return jsonify({'users': users}), 201
    except Exception as e:
        return jsonify({'message': 'Error', 'error': str(e)}), 500


@blue_print.route('/users', methods=['POST'])
def create_user():
    try:
        data = request.json
        user = Usuario(data['nombres'], data['apellidos'],
                       data['email'], data['password'], data['task'], data['rol'])
        db.session.add(user)
        db.session.commit()
        return jsonify({'user': user}), 201
    except Exception as e:
        return jsonify({'message': 'Error', 'error': str(e)}), 500


@blue_print.route('/users/<id>', methods=['GET'])
def get_user(id):
    try:
        user = Usuario.query.get(id)
        return jsonify({'user': user}), 201
    except Exception as e:
        return jsonify({'message': 'Error', 'error': str(e)}), 500


@blue_print.route('/users/<id>', methods=['PUT'])
def update_user(id):
    try:
        data = request.json
        user = Usuario.query.get(id)
        user.nombres = data['nombres']
        user.apellidos = data['apellidos']
        user.email = data['email']
        user.password = data['password']
        user.task = data['task']
        user.rol = data['rol']
        db.session.commit()
        return jsonify({'user': user}), 201
    except Exception as e:
        return jsonify({'message': 'Error', 'error': str(e)}), 500


@blue_print.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = Usuario.query.get(id)
        db.session.delete(user)
        db.session.commit()
        return jsonify({'user': user}), 201
    except Exception as e:
        return jsonify({'message': 'Error', 'error': str(e)}), 500


@blue_print.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        tasks = Task.query.all()
        return jsonify({'tasks': tasks}), 201
    except Exception as e:
        return jsonify({'message': 'Error', 'error': str(e)}), 500


@blue_print.route('/tasks', methods=['POST'])
def create_task():
    try:
        data = request.json
        task = Task(task=data['task'])
        db.session.add(task)
        db.session.commit()
        return jsonify({'message': 'Task created'}), 201
    except Exception as e:
        return jsonify({'message': 'Error', 'error': str(e)}), 500


@blue_print.route('/tasks/<id>', methods=['GET'])
def get_task(id):
    try:
        task = Task.query.get(id)
        return jsonify({'task': task}), 201
    except Exception as e:
        return jsonify({'message': 'Error', 'error': str(e)}), 500


@blue_print.route('/tasks/<id>', methods=['PUT'])
def update_task(id):
    try:
        data = request.json
        task = Task.query.get(id)
        task.task = data['task']
        db.session.commit()
        return jsonify({'message': 'Task updated'}), 201
    except Exception as e:
        return jsonify({'message': 'Error', 'error': str(e)}), 500


@blue_print.route('/tasks/<id>', methods=['DELETE'])
def delete_task(id):
    try:
        task = Task.query.get(id)
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Task deleted'}), 201
    except Exception as e:
        return jsonify({'message': 'Error', 'error': str(e)}), 500


@blue_print.route('/roles', methods=['GET'])
def get_roles():
    try:
        roles = Role.query.all()
        return jsonify({'roles': roles}), 201
    except Exception as e:
        return jsonify({'message': 'Error', 'error': str(e)}), 500


@blue_print.route('/roles', methods=['POST'])
def create_role():
    try:
        data = request.json
        role = Role(rol=data['rol'])
        db.session.add(role)
        db.session.commit()
        return jsonify({'message': 'Role created'}), 201
    except Exception as e:
        return jsonify({'message': 'Error', 'error': str(e)}), 500


@blue_print.route('/roles/<id>', methods=['GET'])
def get_role(id):
    try:
        role = Role.query.get(id)
        return jsonify({'role': role}), 201
    except Exception as e:
        return jsonify({'message': 'Error', 'error': str(e)}), 500


@blue_print.route('/roles/<id>', methods=['PUT'])
def update_role(id):
    try:
        data = request.json
        role = Role.query.get(id)
        role.rol = data['rol']
        db.session.commit()
        return jsonify({'message': 'Role updated'}), 201
    except Exception as e:
        return jsonify({'message': 'Error', 'error': str(e)}), 500


@blue_print.route('/roles/<id>', methods=['DELETE'])
def delete_role(id):
    try:
        role = Role.query.get(id)
        db.session.delete(role)
        db.session.commit()
        return jsonify({'message': 'Role deleted'}), 201
    except Exception as e:
        return jsonify({'message': 'Error', 'error': str(e)}), 500


# @blue_print.route('/uploadcsv', methods=['POST'])
# def upload_csv():
#     try:
#         file = request.files['file']
#         panda = pd.read_csv(file)
#         data = panda.to_dict('records')
#         for item in data:
            
#         return jsonify({'message': 'Users created'}), 201
#     except Exception as e:
#         return jsonify({'message': 'Error', 'error': str(e)}), 500