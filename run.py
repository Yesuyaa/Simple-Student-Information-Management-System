from app import create_app, db
import sys

app = create_app()

def init_db():
    try:
        with app.app_context():
            # 删除所有表（如果存在）
            print("正在删除旧的数据库表...")
            db.drop_all()
            
            # 创建所有表
            print("正在创建新的数据库表...")
            db.create_all()
            print("数据库表创建成功！")
    except Exception as e:
        print(f"数据库初始化错误: {str(e)}")
        sys.exit(1)

if __name__ == '__main__':
    print("正在初始化数据库...")
    init_db()
    print("启动应用服务器...")
    app.run(debug=True, host='127.0.0.1', port=5000)
