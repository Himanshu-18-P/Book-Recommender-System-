from flask import Flask , request , render_template , jsonify
import pickle
import numpy as np
from asgiref.wsgi import WsgiToAsgi


popular_df = pickle.load(open('model/popular.pkl' , 'rb'))
pivot_table = pickle.load(open('model/pivot_table.pkl' , 'rb'))
books = pickle.load(open('model/books.pkl' , 'rb'))
sim_score = pickle.load(open('model/sim_score.pkl' , 'rb'))


def create_app():
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return render_template('index.html' , book_name = list(popular_df['Book-Title'].values) , 
                               author = list(popular_df['Book-Author'].values),
                               image = list(popular_df['Image-URL-M'].values),
                               votes = list(popular_df['num_rating'].values),
                               rating = list(popular_df['avg_rating'].apply(lambda x : round(x , 2)).values)
                               )

   
    @app.route('/recommend')
    def recommand_ui():
            return render_template('recommend.html')
    
    @app.route('/recommend_books' , methods= ['POST'])
    def recommend():
        try:
            data = request.form.get('user_input')
            def recommand(book_name):
                # index fatch from name 
                book_index  = np.where(pivot_table.index == book_name)[0][0]  
                book_list = sorted(list(enumerate(sim_score[book_index])) ,key = lambda x : x[1] , reverse=True)[1:6]  
                res = []
                for i in book_list:
                    temp = []
                    temp_df = books[books['Book-Title'] ==pivot_table.index[i[0]] ]
                    temp.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
                    temp.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
                    temp.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].str.replace('http' , 'https').values))
                    res.append(temp)

                return res
            print(recommand(data.strip()))
            return render_template('recommend.html' , data = recommand(data.strip()))
        
        except Exception as e:
            return render_template('recommend.html' , error = "Not Found")
            # return jsonify({'massage' : "book not found or check spelling"} , 300)
        

    return app  

if __name__ == '__main__':
    import uvicorn
    app = create_app()
    app.run(debug=True)
    # print('done')