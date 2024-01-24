from flask import Flask, render_template, request
import turndown

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        html_input = request.form['html_input']
        markdown_output = convert_to_markdown(html_input)
        return render_template('index.html', markdown_output=markdown_output)

    return render_template('index.html')

def convert_to_markdown(html_input):
    # Turndownライブラリを使用してHTMLをMarkdownに変換
    converter = turndown.TurndownService()
    markdown_output = converter.turndown(html_input)
    return markdown_output

if __name__ == '__main__':
    app.run(debug=True)