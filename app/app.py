from flask import Flask, render_template, request
import markdown

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 'text_input' フィールドが存在するか確認
        if 'text_input' in request.form:
            quill_content = request.form['text_input']
            html_output = convert_to_html(quill_content)
            markdown_output = convert_to_markdown(html_output)
            return render_template('index.html', markdown_output=markdown_output)

    return render_template('index.html')

def convert_to_html(quill_content):
    # Quillのリッチテキストデータそのままを使用
    return quill_content

def convert_to_markdown(html_input):
    # markdownライブラリを使用してHTMLをMarkdownに変換
    markdown_output = markdown.markdown(html_input)
    return markdown_output

if __name__ == '__main__':
    app.run(debug=True)
