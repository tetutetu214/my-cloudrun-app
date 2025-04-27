# テスト対象のファイルをインポート
import main

def test_hello_http():
    """
    hello_http関数が'Hello World!!!'を返すことを確認するテスト。
    このテストはAPIのグリーティングメッセージが正しいことを検証します。
    """
    # 引数をNone(無し)で hello_http関数を実際に呼び出し
    response = main.hello_http(None)
    # 関数の戻り値が"Hello World!!!"と等しい
    assert response == "Hello World!!!"
