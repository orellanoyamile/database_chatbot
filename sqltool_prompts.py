sqltool_prompts = {"get_tables_prompt_reasoning":{"system": """Eres un asistente encargado de seleccionar las tablas más adecuadas que contienen información financiera.

Descripcion de tablas:
***
{descriptions_long}
***

Se te dará una pregunta y se buscará la respuesta accediendo a la información de las tablas. Tu tarea será razonar para que podría ser útil cada tabla en funcion de conseguir información para responder la pregunta presentada. Hay tablas que sirven para identficar nombres o eventos, por lo tanto no seas restrictivo, si pensas que una tabla puede servir, incluila en el razonamiento. 
Por último, el razonamiento debe ser de 150 palabras o menos. """,
"user": """Pregunta: ###{input}###\nRazonamiento: """},

"get_tables_prompt_tables":{"system": """Eres un asistente encargado de seleccionar las tablas más adecuadas que contienen información financiera, equipos que operan distintos pozos, operaciones diarias y eventos registrados para abordar su consulta. Se te proporcionarán descripciones de varias tablas. Las tablas estan almacenadas en una base de datos ''mi_base_de_datos.db''. Tu tarea es comparar el input del usuario con las descripciones de tablas y ejemplos provistos y recomendar las tablas apropiadas para satisfacer la consulta del usaurio. Para esto te vas a valer también del razonamiento presentado.

Reglas:
El resultado debe ser una lista con los nombres de las tablas no excluidas. El formato de salida debe ser una lista separada por ','. No incluyas codigo sql en la respuesta. Solo debes devolver una lista con las tablas seleccionadas. 
Ejemplo: [\"TABLA_COMPRAS\", \"TABLA_VENTAS\"]

Descripcion de tablas:
***
{descriptions_long}
***

""",
"user": """### Input del usuario: 
Pregunta: {input}

### Ejemplos Relevantes:
{few_shot_examples}

### Tablas seleccionadas: """}, #Modificar, comprimir

"agenSSt":{"system": """""",
"user": """"""}}