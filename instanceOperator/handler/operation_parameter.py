operation = {
    'start': {
        'method_name': 'start_instances',
        'expectation': 'stopped',
        'message': {
            200: 'インスタンス起動処理を開始しました。',
            201: 'インスタンスが停止していません。',
            202: '例外が発生しました。詳細はLambda関数のログを確認してください。'
        }
    },
    'stop': {
        'method_name': 'stop_instances',
        'expectation': 'running',
        'message': {
            200: 'インスタンス停止処理を開始しました。',
            201: 'インスタンスが起動していません。',
            202: '例外が発生しました。詳細はLambda関数のログを確認してください。'
        }
    }
}


def key_check(action):
    try:
        operation[action]
    except Exception:
        return 1
    return 0


def get_parameter(action, value):
    return operation[action][value]
