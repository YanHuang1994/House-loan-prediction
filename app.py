from flask import Flask, request, jsonify, send_from_directory, render_template, redirect, url_for
from flask_cors import CORS
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score, classification_report

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# 假定全局变量用于存储模型和测试数据
loaded_model = None
X_test = None
Y_test = None

@app.route('/loadtestdata', methods=['GET'])
def load_test_data():
    print("Received data request")
    global X_test, Y_test
    X_test = pd.read_csv('./X_test.csv')
    rows, columns = X_test.shape
    print("Number of rows:", rows)
    print("Number of columns:", columns)
    Y_test = pd.read_csv('./Y_test.csv')
    return jsonify({
        'message': 'Test data loaded successfully',
        'rows': rows,
        'columns': columns
    }), 200

@app.route('/loadmodel', methods=['GET'])
def load_model():
    print("Received model request")
    global loaded_model
    with open('model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)
    return jsonify({'message': 'Model loaded successfully'}), 200

@app.route('/results', methods=['POST'])
def show_results():
    global X_test, Y_test, loaded_model
    if X_test is None or Y_test is None or loaded_model is None:
        return jsonify({'error': 'Data or model not loaded'}), 400

    try:
        y_pred = loaded_model.predict(X_test)
        accuracy = accuracy_score(Y_test, y_pred)
        report = classification_report(Y_test, y_pred, output_dict=True)
        # 获取precision、recall、f1-score
        weighted_precision = report['weighted avg']['precision']
        weighted_recall = report['weighted avg']['recall']
        weighted_f1_score = report['weighted avg']['f1-score']

        print("Accuracy:", accuracy)
        print("Weighted Precision:", weighted_precision)
        print("Weighted Recall:", weighted_recall)
        print("Weighted F1 Score:", weighted_f1_score)


        metrics = {
            'accuracy': accuracy,
            'precision': report['weighted avg']['precision'],
            'recall': report['weighted avg']['recall'],
            'f1_score': report['weighted avg']['f1-score']
        }

        return jsonify(metrics)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/downloaddata', methods=['GET'])
def download_data():
    file_type = request.args.get('type', 'xtest')  # 获取 URL 参数来决定下载哪个文件
    file_name = 'X_test.csv' if file_type == 'xtest' else 'Y_test.csv'
    return send_from_directory(directory='.', path=file_name, as_attachment=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.errorhandler(500)
def handle_500_error(e):
    return jsonify({'error': 'Internal Server Error', 'message': str(e)}), 500

@app.errorhandler(Exception)
def handle_exception(e):
    response = jsonify({'error': 'Internal Server Error', 'message': str(e)})
    response.status_code = 500
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
