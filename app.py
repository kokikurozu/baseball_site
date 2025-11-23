from flask import Flask, render_template, abort
from jinja2 import TemplateNotFound

app = Flask(__name__)

# トップページ
@app.route('/')
def index():
    return render_template('index.html')

# 汎用ルート：URLと同じ名前のHTMLファイルを探して表示する
# 例: /ops にアクセス -> templates/ops.html を表示
# 例: /blog/article1 -> templates/blog/article1.html (フォルダ分けも可能)
@app.route('/<page_name>')
def show_page(page_name):
    try:
        return render_template(f'{page_name}.html')
    except TemplateNotFound:
        # ファイルが見つからない場合は404エラーとする
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)