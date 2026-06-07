#!/usr/bin/env python3

import click
from app import app, db
from app import config

@click.group()
def cli():
    pass

@cli.command()
def install():
    with app.app_context():
        db.create_all()
    click.echo("install OK")

@cli.command()
def run():
    app.run()

@cli.command()
def start():
    app.run(debug=True)

@cli.command()
@click.argument('start', required=False)
@click.argument('end', required=False)
def donations(start, end):
    import worker_donations
    worker_donations.run(start, end)
    click.echo("donations OK")

@cli.command()
def testmail():
    from flask_mail import Message
    from app import mail
    msg = Message("Hello",
                  sender=config.mail_from,
                  recipients=config.admins)
    mail.send(msg)
    click.echo("testmail sent")

if __name__ == '__main__':
    cli()