Put your train.csv and test.csv in this folder. Should be compatible with Kaggle's Python Docker. Call these data sets from munge scripts using:

```shell
cd ./munge
python3
```

```python
train = pd.read_csv('../inputs/train.csv'
test = pd.read_csv('../inputs/test.csv'
```
