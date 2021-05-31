from flask.cli import FlaskGroup
from sqlalchemy import exc
from project import (
    app,
    db,
    database_of_frame_information,
)  

cli = FlaskGroup(app)

@cli.command("create_and_init_db")
def create_and_init_db():
    db.create_all()

    if_database_work = "now build the database and it can work"

    add_database_of_frame_information = database_of_frame_information(
        if_database_work
    )
    try:
        db.session.add(add_database_of_frame_information)
        db.session.commit()
        print( "add the reuslt in database")
    except exc.SQLAlchemyError as e:
        print(str(e))
        db.session.rollback()
        return "there was an issue in licenses_passwords when adding your datebase."

if __name__ == "__main__":
    cli()
