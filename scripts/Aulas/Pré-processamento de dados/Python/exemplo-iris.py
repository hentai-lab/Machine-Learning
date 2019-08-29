import pandas
import numpy
import seaborn

iris = pandas.read_csv("../../../../docs/Iris.csv")
iris_dataframe = pandas.DataFrame(iris)
iris_columns = ["ID", "Sepal_Length", "Sepal_Width", "Petal_Length", "Petal_Width", "Species"]
iris_dataframe.columns = iris_columns
print(iris_dataframe.head())
print(iris_dataframe['Species'].value_counts())
print(iris_dataframe.dtypes)

iris_scatterplot = seaborn.scatterplot(x='Petal_Length', y='Petal_Width', data=iris_dataframe, hue='Species')
iris_scatterplot.set_title("Relação entre atributos")
iris_scatterplot.set_xlabel("Petal Length")
iris_scatterplot.set_ylabel("Petal Width")
print(iris_scatterplot)