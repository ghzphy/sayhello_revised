import click

from sayhello import app, db
from sayhello.models import Message

@app.cli.command()
@click.option('--drop',is_flag=True,help='Create after drop.')
def initdb(drop):
    if drop:
        click.confirm('This operation will delete the database, do you want to continue?',abort=True)
        db.drop_all()
        click.echo('Drop tables.')
    db.create_all()
    click.echo('Initialized database.')

@app.cli.command()
@click.option('--count',default=20,help='Quantity of messages, the default is 20.')
def forge(count):
    from faker import Faker    
    db.drop_all()
    db.create_all()
    ### Faker()默认为英文，Faker('zh-CN')为中文
    fake = Faker('zh-CN')
    click.echo('Working...')
    
    for i in range(count):
        message = Message(
            name=fake.name(),
            body=fake.sentence(),
            timestamp=fake.date_time_this_year()
        )
        db.session.add(message)
    db.session.commit()
    click.echo('Created %d fake messages. ' % count)


