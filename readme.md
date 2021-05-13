# How to use

## Creating a matrix of letter frequency

To save a matrix use the following command
````
type "tekst_file_path" | python mapper_lf.py | sort  | python reduce_lf.py | python mapper_percentage.py | python data_to_matrix.py "save_file.csv"
````

We used this command to create an English model.
```
type "tekst\alice.txt" | python mapper_lf.py | sort  | python reduce_lf.py | python mapper_percentage.py | python data_to_matrix.py "output_matrix\english_matrix.csv"
```

We used this command to create a Dutch model
```
type "tekst\columbus.txt" | python mapper_lf.py | sort  | python reduce_lf.py | python mapper_percentage.py | python data_to_matrix.py "output_matrix\dutch_matrix.csv"
```

## Comparing text to languages

```
Todo
```