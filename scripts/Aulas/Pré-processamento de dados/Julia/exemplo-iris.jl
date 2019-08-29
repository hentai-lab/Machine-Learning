using CSV
using DataFrames

iris = CSV.read("../../../../docs/Iris.csv")
iris_dataframe = DataFrame(iris)