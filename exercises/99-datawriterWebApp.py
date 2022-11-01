#create a program that asks user to add text from web app
from flask import Flask, render_template_string, request
app = Flask(__name__)

html = """
  		      <div class="form">
              <form action="{{url_for('sent')}}" method="POST">
  			        <input title="Your email address will be safe with us." placeholder="Enter a line" type="text" name="line" required> <br>
                    {{message|safe}}
                <button class="go-button" type="submit"> Submit </button>
  		        </form>
          </div>
"""
@app.route("/")
def index():
    return render_template_string(html)

@app.route("/sent", methods=['GET', 'POST'])
def sent():
    line = None
    if request.method == 'POST':
        line = request.form['username']
        with open("user_input_flasks.txt", "a+") as file:
            file.write(line+"\n")
        return render_template_string(html)
if __name__ == "__main__":
    app.run(debug=True)
