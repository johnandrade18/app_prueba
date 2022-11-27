from flask_marshmallow import Marshmallow

ma = Marshmallow()

# Schema for the table User


class UsuarioSchema(ma.Schema):
    class Meta:
        fields = ('id', 'nombres', 'apellidos', 'email', 'password', 'task', 'rol')


class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'task')


class RoleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'role')
