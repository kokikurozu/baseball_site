from flask import Flask, render_template, abort
from jinja2 import TemplateNotFound

app = Flask(__name__)

# トップページ
@app.route('/')
def index():
    return render_template('index.html')

# 各ページへの自動振り分け機能
# 例: /ops にアクセス -> templates/ops.html を探して表示
@app.route('/<page_name>')
def show_page(page_name):
    try:
        # 指定された名前のHTMLファイルを表示する
        return render_template(f'{page_name}.html')
    except TemplateNotFound:
        # ファイルがなければ404エラーを出す
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)