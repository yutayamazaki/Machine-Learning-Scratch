# Machine-Learning-Scratch

![GitHub Actions](https://github.com/yutayamazaki/Machine-Learning-Scratch/workflows/Python%20CI%20jobs/badge.svg)

## Python実装とアルゴリズム解説と例

|  アルゴリズム名  |  Python実装  |  解説  |  使用例  |
| ---- | ---- | ---- | ---- |
| k近傍法 |  [k_neighbor.py](https://github.com/yutayamazaki/Machine-Learning-Scratch/blob/master/mlscratch/models/k_neighbor.py)  |  [k_nearest_neighbor.md](https://github.com/yutayamazaki/Machine-Learning-Scratch/blob/master/docs/k_nearest_neighbor.md)  |  [k_neighbor.py](https://github.com/yutayamazaki/Machine-Learning-Scratch/blob/master/examples/k_neighbor.py)  |
|  LinearRegression  |  [linear.py](https://github.com/yutayamazaki/Machine-Learning-Scratch/blob/master/mlscratch/models/linear.py)  |  [linear_regression.md](https://github.com/yutayamazaki/Machine-Learning-Scratch/blob/master/docs/linear_regression.md)  |  [linear_regression.py](https://github.com/yutayamazaki/Machine-Learning-Scratch/blob/master/examples/linear_regression.py)  |
|  ロジスティック回帰  |  [logistic_regression.py](https://github.com/yutayamazaki/Machine-Learning-Scratch/blob/master/mlscratch/models/logistic_regression.py)  | None |  None  |
|  PCA  |  [pca.py](https://github.com/yutayamazaki/Machine-Learning-Scratch/blob/master/mlscratch/decomposition/pca.py)  |  Under construction  |  [pca.py](https://github.com/yutayamazaki/Machine-Learning-Scratch/blob/master/examples/pca.py)  |

## Cotribution
- flake8を用いてコーディング規約を順守するように設定している
- mlscratchディレクトリで`flake8`を実行することで，文法チェックが行える
- 以下のコマンドでテストを実行できる

```shell
python -m unittest discover tests
```
