# Documentatie

## Aanmaken van matrix modellen 
Voor deze opdracht hebben we gebruik gemaakt van verschillende mappers en reducers om tot het juiste resultaat te komen 

Voor het uitleggen van het procces, maken we gebruik van de Engelse train tekst naar een matrix

De eerste stap, de eerste mapper

```type "tekst\alice.txt" | python mapper_lf.py ```

Het resultaat van deze uitkomst zijn alle letter paren gemapt met een 1 maar niet gesoorteerd

![](https://cdn.discordapp.com/attachments/843175127771775048/843175138140487720/unknown.png)

Na deze mapper gaan we sorteren, hier gebruiken wij de standaard functie voor

```type "tekst\alice.txt" | python mapper_lf.py | sort```

![](https://cdn.discordapp.com/attachments/843175127771775048/843175498791649310/unknown.png)

Nu alles gesorteerd is, gaan we alles samen voegen van wat bij elkaar hoort, ook wel reduce

```type "tekst\alice.txt" | python mapper_lf.py | sort | python reduce_lf```

![](https://cdn.discordapp.com/attachments/843175127771775048/843175859241746512/unknown.png)

Alles is nu bij elkaar opgeteld maar we willen het gaan normaliseren door de percentage te berekenen van hoevaak de combinatie voorkomt ten opzichten van de totaal combinaties

```type "tekst\alice.txt" | python mapper_lf.py | sort  | python reduce_lf.py | python mapper_percentage.py```

![](https://cdn.discordapp.com/attachments/843175127771775048/843176353775616090/unknown.png)

Nadat we alle percentages hebben, maken we een matrix ervan en kunnen we het opslaan

```type "tekst\alice.txt" | python mapper_lf.py | sort  | python reduce_lf.py | python mapper_percentage.py | python data_to_matrix.py "output_matrix\english_matrix.csv"```

![](https://cdn.discordapp.com/attachments/843175127771775048/843177561663733850/unknown.png)

* Dit process wordt ook gedaan voor de Nederlandse tekst en wordt appart opgeslagen

## Classificeren

Tijdens het classificeren kwam we een paar obstakels tegen die we graag willen toelichten.

In de meegeleverde tekst vanaf de canvas, staat op regel 62 in de tekst een blanke regel..

Deze regel hebben wij er uitgefilterd omdat je niet een taal kan afleiden van een lege regel en dus niet mag/moet meenemen in het classificeren

Achteraf hadden we de opdracht van tevoren al anders op willen bouwen, vanwege een gebrek aan tijd hebben we dit niet allemaal opnieuw kunnen schrijven,.

Dit kom omdat we aan het begin van de opdracht dachten dat we een hele tekst moesten classificeren maar dit bleek per regel te moeten.

Om dit op te lossen hebben in de classify_rows.py de functies zo geschreven dat het hetzelfde doet als een losse mapper/reduce functie.

Onze classify_rows doet hetzelfde als een mapper, hij geeft aan of een row Engels of Nederlands is met een 1, na deze functie soorteren wij alles en reduce wij de rows tot een eindresultaat

Als laaste puntje: 
Om uiteindelijk te bepalen in welke taal de zin is moeten we kijken welke matrix (Engels/Nederlands) het meeste overeen komt met de matrix van de zin

We hebben uiteindelijk dit stukje code gebruikt om te kijken hoeveel 2 matrixen overeen komen:
```
nederlands_result = abs(row_result - nederlands_model).sum()
```
We hadden verwacht dat dit hetzelfde zou doen:
```
nederlands_result = mean_squared_error(nederlands_model, row_result)
```
Maar dit blijkt niet zo te zijn, we weten niet waarom.

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
python classify_rows.py "output_matrix/dutch_matrix.csv" "output_matrix/english_matrix.csv" "tekst/ne-en-tekst.txt" | sort | python reduce_rows.py
```
Results

![result](https://cdn.discordapp.com/attachments/843175127771775048/843179796200423434/unknown.png)

