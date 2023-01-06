from init_app import app
import models



# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     description = db.Column(db.String, nullable=False)
#     status = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)
#
#     def serialize(self):
#         return {
#             'id': self.id,
#             'description': self.description,
#             'status': self.status
#         }
#
#
# class Status(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String, nullable=False)
#
#     def serialize(self):
#         return {
#             'id': self.id,
#             'name': self.name
#         }


if __name__ == '__main__':
    with app.app_context():
        models.db.drop_all()
        models.db.create_all()

        for name in ['new', 'done', 'in_work']:
            status = models.Status(
                name=name,
            )
            models.db.session.add(status)
            models.db.session.commit()

    print('All tables have been created')
