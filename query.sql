CREATE TABLE parasha(
	id INTEGER primary KEY AutoIncrement,
	nroParasha int,
	nameParasha varchar(255),
	aliya1 text,
	aliya2 text,
	aliya3 text,
	aliya4 text,
	aliya5 text,
	aliya6 text,
	aliya7 text
)

INSERT INTO parasha(nroParasha, nameParasha, aliya1, aliya2, aliya3, aliya4, aliya5, aliya6, aliya7) 
values (5, "Bamidbar", "Primer aliya", "Segunda Aliya", "13 Cuando se aproximaba la Pascua de los judíos, subió Jesús a Jerusalén. 14 Y en el templo halló a los que vendían bueyes, ovejas y palomas, e instalados en sus mesas a los que cambiaban dinero. 15 Entonces, haciendo un látigo de cuerdas, echó a todos del templo, juntamente con sus ovejas y sus bueyes; regó por el suelo las monedas de los que cambiaban dinero y derribó sus mesas. 16 A los que vendían las palomas les dijo:

—¡Saquen esto de aquí! ¿Cómo se atreven a convertir la casa de mi Padre en un mercado?

17 Sus discípulos se acordaron de que está escrito: «El celo por tu casa me consumirá». 18 Entonces los judíos reaccionaron, preguntándole:

—¿Qué señal puedes mostrarnos para actuar de esta manera?

19 —Destruyan este templo —respondió Jesús—, y lo levantaré de nuevo en tres días.

20 —Tardaron cuarenta y seis años en construir este templo, ¿y tú vas a levantarlo en tres días?

21 Pero el templo al que se refería era su propio cuerpo. 22 Así, pues, cuando se levantó de entre los muertos, sus discípulos se acordaron de lo que había dicho, y creyeron en la Escritura y en las palabras de Jesús.

23 Mientras estaba en Jerusalén, durante la fiesta de la Pascua, muchos creyeron en su nombre al ver las señales que hacía. 24 En cambio Jesús no les creía porque los conocía a todos; 25 no necesitaba que nadie le informara nada acerca de los demás, pues él conocía el interior del ser humano.", " Cuarta Aliyá", "Quinta Aliya", "Sexta Aliya", "Septima Aliya")

SELECT aliya3 FROM parasha where nameParasha = "Bamidbar"