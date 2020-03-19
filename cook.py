import sys
from collections import defaultdict

# 表示回数がこの値を越えればハイライト
HIGHLIGHT_THRESHOULD = 1

# 単語から記号を除去して小文字に変換
def format_word(word_raw):
    return delete_symbol_if_exist(word_raw).lower()

def delete_symbol_if_exist(word):
    if word[-1] in (',', '.', '!', '?'):
        return word[:-1]
    else:
        return word

def main():
    if len(sys.argv) != 2:
        print("Please spicify 1 file name. Usage: python q1.py [filename]", file=sys.stderr)
        exit(1)
    words_dict = defaultdict(int)
    try:
        with open(sys.argv[1], encoding='utf-8') as file:
            for line in file:
                for word_raw in line.split():
                    word_lower = format_word(word_raw)
                    words_dict[word_lower] += 1

        # 単語を全て読み込んだらメモリに乗らない可能性があるため，もう一度表示用に同じファイルを開く
        with open(sys.argv[1], encoding='utf-8') as file:
            for line in file:
                for i, word_raw in enumerate(line.split()):
                    word_lower = format_word(word_raw)
                    if i != 0:
                        # 行頭だけ単語間スペースを除去
                        print(' ', end='')
                    if words_dict[word_lower] > HIGHLIGHT_THRESHOULD:
                        # 背景色を赤色で表示
                        print(f'\033[41m{word_raw}\033[m', end='')
                    else:
                        print(f'{word_raw}', end='')
    except FileNotFoundError:
        print(f'file "{sys.argv[1]}" not found.')
        exit(1)


if __name__ == '__main__':
    main()
