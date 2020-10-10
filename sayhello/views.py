from flask import flash, redirect, url_for, render_template
from sayhello import app, db
from sayhello.forms import HelloForm
from sayhello.models import Message


@app.route('/', methods=['GET', 'POST'])
def index():
    form = HelloForm()
    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data
        message = Message(name=name, body=body)
        db.session.add(message)
        db.session.commit()
        flash('Your message have been sent to the world!')
        ### url_for 重定向指定的函数，例如下面的index()
        return redirect(url_for('index'))
    ### 对结果以时间信息进行排序
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    return render_template('index.html',form=form,messages=messages)
