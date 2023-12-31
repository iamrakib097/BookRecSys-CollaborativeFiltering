@app.route('/recommend_books', methods=['POST'])
def recommend_books():
    user_input = request.form.get('user_input')
    
    # Check if user_input is in the index
    if user_input not in pt.index:
        return render_template('recommend.html', data=None)

    index_array = np.where(pt.index == user_input)[0]

    # Check if index_array is not empty
    if not index_array:
        return render_template('recommend.html', data=None)

    index = index_array[0]
    similar_items = sorted(list(enumerate(similarity_scores[index])), key=lambda x: x[1], reverse=True)[1:5]

    data = []
    for i in similar_items:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        data.append(item)

    return render_template('recommend.html', data=data)