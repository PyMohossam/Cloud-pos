from Quickbill.QP import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 2666 ,debug=True,threaded=True)
