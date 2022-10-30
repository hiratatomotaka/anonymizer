from カメラ import カメラ as カメラ型
from ディスプレイ import ディスプレイ

def main():
    カメラ = カメラ型()
    try:
        while True:
            画像データ = カメラ.が撮影する()
            ディスプレイ.が見せる(画像データ)
    except KeyboardInterrupt:
        カメラ.を止める()
        ディスプレイ.を止める()

main()
