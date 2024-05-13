import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Firebase Admin SDKの初期化
path = '/Users/hat/Documents/GitHub/get_syllabus_info_from_web_site/get-syllabus-info-43b21-firebase-adminsdk-jogd9-97e9407f2d.json'
cred = credentials.Certificate(path)
firebase_admin.initialize_app(cred)

# Firestoreクライアントの取得
db = firestore.client()

# Like検索を使用してFirestoreからデータを検索・取得する関数
def search_syllabus_like(keyword):
    # 各フィールドに対するクエリを作成
    queries = []
    fields = ['course_name', 'instructor', 'course_objective', 'course_plan', 'course_period', 'grade_allocation', 'credits', 'required_elective', 'educational_program']

    for field in fields:
        query = db.collection('syllabus').where(field, '>=', keyword).where(field, '<=', keyword + '\uf8ff')
        queries.append(query)

    # クエリを実行してドキュメントを取得
    results = []
    for query in queries:
        docs = query.get()
        results.extend(docs)

    if len(results) > 0:
        unique_docs = {}  # ユニークなドキュメントを格納する辞書

        for doc in results:
            syllabus_id = doc.id

            if syllabus_id not in unique_docs:
                unique_docs[syllabus_id] = True

                print(f'Document ID: {doc.id}')
                for field in fields:
                    value = doc.get(field)
                    if value:
                        print(f'{field.capitalize()}:')
                        if isinstance(value, str):
                            lines = value.split('\n')  # 値を改行で分割
                            for line in lines:
                                if '。' in line:
                                    sentences = line.split('。')  # 行を文単位で分割
                                    for sentence in sentences:
                                        print(sentence.strip() + '。')  # 文を出力
                                else:
                                    print(line.strip())  # 行をそのまま出力
                        else:
                            print(value)  # 文字列以外の値をそのまま出力
                    else:
                        print(f'{field.capitalize()}: Not available')  # フィールドの値が存在しない場合
                    print()

                print('---')
    else:
        print('No matching documents found.')  # 一致するドキュメントが見つからなかった場合

# 使用例
search_keyword = input("Enter a keyword to search: ")
search_syllabus_like(search_keyword)