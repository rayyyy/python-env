def main():
    """サンプルプログラム"""

    for i in range(1, 6):
        if i % 2 == 0:
            print("%sは偶数です" % i)
        else:
            print("%sは奇数です" % i)


# コマンドラインから直接実行された場合は__name__に'__main__'が入る
if __name__ == '__main__':
    main()
