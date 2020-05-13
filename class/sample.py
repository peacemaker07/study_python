class Car:
    """
    車クラス
    """

    #
    # 以下の変数がプロパティと呼ばれる
    #
    maker = None  # メーカー
    name = None  # 車種名
    displacement = None  # 排気量
    color = None # 色

    def __init__(self, maker, name, displacement, color):
        """
        コンストラクタ
        """
        self.maker = maker
        self.name = name
        self.displacement = displacement
        self.color = color

    #
    # 以下の関数がメソッドと呼ばれる
    #
    def start(self):
        print(self.name + "が発進します")

    def stop(self):
        print(self.name + "が止まります")

    def curve(self):
        print(self.name + "が曲がります")


#
# 実体（インスタンス）をつくってみる
#

# カムリを製造
camry = Car('TOYOTA', 'camry', 2500, 'red')
print('====')
## プロパティを表示
print(camry.maker)
print(camry.name)
print(camry.displacement)
print(camry.color)
## メソッドを実行してみる
camry.start()
camry.curve()
camry.stop()

# レガシイを製造
legacy = Car('SUBARU', 'legacy', 2000, 'blue')
print('====')
## プロパティを表示
print(legacy.maker)
print(legacy.name)
print(legacy.displacement)
print(legacy.color)
## メソッドを実行してみる
legacy.start()
legacy.curve()
legacy.stop()

# S660を製造
s660 = Car('Honda', 'S660', 640, 'white')
print('====')
## プロパティを表示
print(s660.maker)
print(s660.name)
print(s660.displacement)
print(s660.color)
## メソッドを実行してみる
s660.start()
s660.curve()
s660.stop()
