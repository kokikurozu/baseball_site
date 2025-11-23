from flask import Flask, render_template, abort

app = Flask(__name__)

# ここにデータを登録します（データベースの代わり）
# 新しい指標を追加したいときは、ここを増やすだけでOKです。
metrics_data = {
    "ops": {
        "title": "OPS",
        "subtitle": "On-base Plus Slugging",
        "formula": "出塁率 + 長打率",
        "description": "打者の「得点能力」を最も手軽かつ正確に表す指標。得点との相関が高く、現代野球の基本となる数値。",
        "evaluation": ["0.800：優秀", "0.900：超一流", "1.000：MVP級"]
    },
    "woba": {
        "title": "wOBA",
        "subtitle": "Weighted On-Base Average",
        "formula": "得点価値による加重平均",
        "description": "OPSの進化版。四球、単打、本塁打などの「得点価値」に基づいて重み付け計算をした、より精密な指標。",
        "evaluation": ["0.320：平均", "0.370：優秀", "0.400以上：リーグ最高峰"]
    },
    "whip": {
        "title": "WHIP",
        "subtitle": "Walks plus Hits per IP",
        "formula": "(被安打 + 与四球) ÷ 投球回",
        "description": "1イニングあたり何人のランナーを出したかを示す指標。防御率よりも運の要素が少なく、投手の実力を測りやすい。",
        "evaluation": ["1.30：平均", "1.10：エース級", "1.00未満：球界代表クラス"]
    },
    "war": {
        "title": "WAR",
        "subtitle": "Wins Above Replacement",
        "formula": "総合評価指標",
        "description": "「控え選手と比較して、どれだけチームの勝利数を増やしたか」を表す指標。攻撃・守備・走塁すべてを統合した究極の数値。",
        "evaluation": ["2.0：レギュラー", "5.0：オールスター", "8.0：MVP"]
    }
}

# トップページ（一覧）
@app.route('/')
def index():
    return render_template('index.html', metrics=metrics_data)

# 詳細ページ（IDによって中身を変える）
# 例: /metric/ops にアクセスすると、OPSのデータをdetail.htmlに渡して表示
@app.route('/metric/<metric_id>')
def detail(metric_id):
    data = metrics_data.get(metric_id)
    if not data:
        abort(404) # データがない場合は404エラー
    return render_template('detail.html', data=data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)