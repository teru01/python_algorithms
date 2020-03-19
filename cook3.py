import sys
import urllib.request as req
import urllib.parse
import json

INITIAL_POINT = 20
ENDPOINT_URL = "https://tanaka-server.herokuapp.com/"

class Player:
    def __init__(self):
        self.current_point = 20
        self.win_count = 0

def main():
    player = Player()
    for i in range(3):
        parity_ok = False
        point_ok = False
        while not parity_ok:
            print('偶数か奇数どちらに賭けますか？ 偶数: 0, 奇数: 1を入力してください')
            try:
                n = int(input().strip())
                if n == 0:
                    is_user_select_odd = False
                    parity_ok = True
                elif n == 1:
                    is_user_select_odd = True
                    parity_ok = True
                else:
                    raise ValueError
            except ValueError:
                print('偶数: 0, 奇数: 1を入力してください')
        while not point_ok:
            print('何ポイント賭けますか？ ポイント数を入力してください')
            try:
                point = int(input().strip())
                if point > player.current_point:
                    raise ValueError
                point_ok = True
            except ValueError:
                print('整数を入力してください')
            except ValueError:
                print('そのポイントは賭けられません')

        params = make_parametes(is_user_select_odd, point)
        response = post_request(ENDPOINT_URL, params)
        player.current_point += response['points']
        show_result(player, response, is_user_select_odd)
    show_final_result(player)

def post_request(endpoint, parameters):
    request = req.Request(endpoint, urllib.parse.urlencode(parameters).encode(), method='POST')
    try:
        with req.urlopen(request) as response:
            result = json.loads(response.read())
            return result
    except:
        pass
    # except url

def make_parametes(is_odd, bet_point):
    if is_odd:
        bet_str = "odd"
    else:
        bet_str = "even"
    return {
        "bet": bet_str,
        "points": bet_point
    }

def show_result(player, response_json, is_user_select_odd):
    print('サーバが返したダイスの目は，{}でした'.format(response_json['dice']))
    result = 'はずれ'
    if response_json['result'] == 'odd':
        if is_user_select_odd:
            result = '当たり'
            player.win_count += 1
        dice_sum = '奇数'
    elif response_json['result'] == 'even':
        if not is_user_select_odd:
            result = '当たり'
            player.win_count += 1
        dice_sum = '偶数'
    print(f'サイコロの出た目の合計は{dice_sum}でした')
    print(f'結果は{result}です')
    print('現在のポイントは{}です'.format(player.current_point))


def show_final_result(player):
    print('最終ポイントは{}です'.format(player.current_point))
    print('当たっていた回数は{}回です'.format(player.win_count))

if __name__ == '__main__':
    main()
