from config.database import db


class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(70), nullable=False)
    apellidos = db.Column(db.String(70), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    password = db.Column(db.String(250), nullable=False)
    task = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    rol = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)

    def __init__(self, nombres, apellidos, email, password, task, rol):
        self.nombres = nombres
        self.apellidos = apellidos
        self.email = email
        self.password = password
        self.task = task
        self.rol = rol

    def __repr__(self):
        return f'Usuario: {self.nombres} {self.apellidos}'

    def serialize(self):
        return {
            'id': self.id,
            'nombres': self.nombres,
            'apellidos': self.apellidos,
            'email': self.email,
            'password': self.password,
            'task': self.task,
            'rol': self.rol
        }


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(250), nullable=False)
    user = db.relationship('Usuario', backref='task', lazy=True)

    def __init__(self, task):
        self.task = task

    def __repr__(self):
        return f'Task: {self.task}'

    def serialize(self):
        return {
            'id': self.id,
            'task': self.task
        }


class Role(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(50), nullable=False)
    user = db.relationship('Usuario', backref='role', lazy=True)

    def __init__(self, role):
        self.role = role

    def __repr__(self):
        return f'Role: {self.role}'

    def serialize(self):
        return {
            'id': self.id,
            'role': self.role,
        }
