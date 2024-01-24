
from flask import Flask, render_template, request
import markdown

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text_input = request.form['text_input']
        html_output = convert_to_html(text_input)
        markdown_output = convert_to_markdown(html_output)
        return render_template('index.html', markdown_output=markdown_output)

    return render_template('index.html')

def convert_to_html(text_input):
    # ここでテキストをHTMLに変換するロジックを実装
    # 例えば、Markdown内でテキストを<p>タグでラップするとします
    html_output = f'<p>{text_input}</p>'
    return html_output

def convert_to_markdown(html_input):
    # markdownライブラリを使用してHTMLをMarkdownに変換
    markdown_output = markdown.markdown(html_input)
    return markdown_output

if __name__ == '__main__':
    app.run(debug=True)