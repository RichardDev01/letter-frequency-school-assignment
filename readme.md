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
python classify_rows.py "output_matrix/dutch_matrix.csv" "output_matrix/english_matrix.csv" "tekst/ne-en-tekst.txt"
```

![result](https://cdn.discordapp.com/attachments/701351521433944066/842802337898299442/unknown.png)

