import sys
from app import create_app, db

def init_database():
    try:
        app = create_app()
        with app.app_context():
            # 删除所有表
            print("正在删除旧表...")
            db.drop_all()
            
            # 创建所有表
            print("正在创建新表...")
            db.create_all()
            
            # 验证表是否存在
            engine = db.engine
            inspector = db.inspect(engine)
            tables = inspector.get_table_names()
            
            print("成功创建的表：")
            for table in tables:
                print(f"- {table}")
                columns = inspector.get_columns(table)
                for column in columns:
                    print(f"  - {column['name']}: {column['type']}")

    except Exception as e:
        print(f"数据库初始化错误: {str(e)}")
        print(f"错误类型: {type(e).__name__}")
        sys.exit(1)

if __name__ == '__main__':
    print("开始初始化数据库...")
    init_database()
    print("数据库初始化完成！")
