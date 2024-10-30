# Proyecto ETL: Análisis de Ingresos y Gastos de Organismos Sanitarios (2010-2020)

## Descripción del Proyecto
Este proyecto tiene como objetivo analizar los ingresos y gastos de organismos sanitarios en España desde 2010 hasta 2020. Utilizando un proceso ETL (Extracción, Transformación y Carga), hemos procesado y almacenado datos en una base de datos PostgreSQL para realizar un análisis exploratorio de datos (EDA). Este análisis nos permite identificar tendencias y patrones en las categorías de ingresos y gastos, así como obtener conclusiones relativas sobre los datos.

## Estructura de Datos

### Ingresos
La tabla de ingresos en la base de datos contiene las siguientes categorías:
- **particulares**: ingresos generados directamente por particulares.
- **aseguradoras**: ingresos generados por aseguradoras.
- **aseguradoras_enfermedad**: ingresos generados por aseguradoras de enfermedad.
- **aseguradoras_trafico**: ingresos generados por aseguradoras de tráfico.
- **mutuas**: ingresos provenientes de mutuas.
- **año**: año correspondiente al registro de los ingresos.

### Gastos
La tabla de gastos incluye las siguientes columnas:
- **año**: año correspondiente al registro de los gastos.
- **totalcompra**: gastos totales en compras.
- **producfarma**: gastos en productos farmacéuticos.
- **materialsani**: gastos en materiales sanitarios.
- **implantes**: gastos en implantes.
- **restomateriasani**: gastos en otros materiales sanitarios.
- **servcontratado**: gastos en servicios contratados.
- **trabajocontratado**: gastos en trabajos contratados.
- **xrestocompras**: otros gastos de compra.
- **variaexistencias**: variación de existencias.
- **servexteriores**: gastos en servicios exteriores.
- **sumistro**: gastos en suministros.
- **xrestoserviexter**: otros gastos de servicios exteriores.
- **gastopersonal**: gastos en personal.
- **sueldos**: sueldos.
- **indemnizacion**: indemnizaciones.
- **segsocempresa**: seguridad social a cargo de la empresa.
- **otrgassocial**: otros gastos sociales.
- **dotaamortizacion**: dotación de amortización.
- **perdidadeterioro**: pérdidas por deterioro.
- **xrestogasto**: otros gastos.
- **totcompragasto**: gastos totales.

### Tipo de Centro
La base de datos también clasifica los registros por **tipo_centro** hospitalario, permitiendo desglosar los análisis según el tipo de organismo sanitario.

## Proceso ETL

### Extracción
Los datos de ingresos y gastos fueron obtenidos de distintas fuentes oficiales de organismos sanitarios. Estos datos fueron recopilados, estandarizados y estructurados antes de su procesamiento.

### Transformación
Para la transformación de datos, se realizaron varias operaciones de limpieza y estandarización, utilizando las siguientes bibliotecas:
- **pandas** y **numpy**: para limpieza, filtrado y organización de los datos.
- **psycopg2**: para la conexión y carga de datos en PostgreSQL, y la creación de tablas en la base de datos.

### Carga
Una vez procesados, los datos fueron cargados en una base de datos PostgreSQL, estructurados en tablas de ingresos y gastos categorizados y vinculados al tipo de centro hospitalario.

## Análisis Exploratorio de Datos (EDA)
A través de un EDA detallado, calculamos y actualizamos los valores netos por categoría de ingresos y gastos anuales. Las principales áreas de análisis incluyen:
1. Comparativa de ingresos por fuentes de financiamiento (particulares, aseguradoras, mutuas, etc.).
2. Evolución de los gastos anuales en diferentes categorías, como productos farmacéuticos, materiales sanitarios y personal.
3. Análisis de los tipos de centros hospitalarios para identificar patrones de ingresos y gastos.

## Conclusiones
Se destacan las principales tendencias y observaciones obtenidas del análisis de los datos, con un enfoque en el comportamiento y evolución de las categorías de gastos e ingresos a lo largo del período 2013-2020.

## Requisitos y Librerías
Este proyecto requiere las siguientes bibliotecas de Python:
- **pandas**
- **numpy**
- **psycopg2**

## Instrucciones de Uso
1. Clona el repositorio.
2. Configura tu conexión a PostgreSQL en el archivo de configuración.
3. Ejecuta el script principal de ETL para extraer, transformar y cargar los datos en la base de datos.
4. Realiza el análisis exploratorio de datos utilizando los scripts de EDA.

## Análisis Personalizado
_Aquí puedes incluir tu propio análisis y observaciones sobre los datos._
