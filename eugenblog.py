from app import create_application

if __name__ == '__main__':
    app = create_application()
    app.run(host='0.0.0.0', port=5000)
