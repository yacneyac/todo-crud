import models

from init_app import app, db


if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()

        for name in ['new', 'done', 'in_work']:
            status = models.Status(
                name=name,
            )
            db.session.add(status)
            db.session.commit()

    print('All tables have been created')
