from flask import Flask, render_template

import pandas as pd

popular_df = pd.read_pickle("popular.pkl")
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html',
                           book_name=list(popular_df['Book-Title'].values),
                           author=list(popular_df['Book-Author'].values),
                           image=list(popular_df['Image-URL-M'].values),
                           votes=list(popular_df['num_rating'].values),
                           rating=list(popular_df['avg_rating'].values)
                            )

@app.route('/recommend')
def recommend():
    return render_template('recommend.html',
                           
                           
                           )


if __name__ == '__main__':
    app.run(debug=True)
