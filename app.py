from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'hair cut',
    'location': 'Bengaluru, India',
    'price': 'Rs. 100'
  },
  {
    'id': 2,
    'title': 'spa',
    'location': 'Bengaluru, India',
    'price': 'Rs. 200'
  },
{
  'id': 3,
  'title': 'shavingt',
  'location': 'Bengaluru, India',
  'price': 'Rs. 80'
}
]

@app.route("/")
def hello_world():
    return render_template('Home.html',jobs=JOBS,company_name='STYLESENSE')

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
