from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
contacts = []
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        contacts.append({'name': name, 'phone': phone})
        return redirect(url_for('home'))
    return render_template('home.html')
@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        contacts.append({'name': name, 'phone': phone})
        return redirect(url_for('contacts_view'))
    return render_template('add.html')

@app.route('/contacts')
def contacts_view():
    return render_template('contacts.html', contacts=contacts)

@app.route('/delete/<int:index>', methods=['POST'])
def delete_contact(index):
    if 0 <= index < len(contacts):
        contacts.pop(index)
    return redirect(url_for('contacts_view'))

if __name__ == '__main__':
    app.run(debug=True)
