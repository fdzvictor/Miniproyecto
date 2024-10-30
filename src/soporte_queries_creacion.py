


# Centro hospitalario identificador de hospitales y nombres 
query_creation_hospitales = """
create table if not exists hospitales (
    ncodi INT primary key,
    name VARCHAR(300)
);
"""

# Tipos de hospityalizacion de los hospitales 
query_creation_tipo_hosp = """
create table if not exists tipo_hospitalizacion (
    tipo_id SERIAL primary key,
    nombre VARCHAR(100) unique not null
    );
"""

# Gastos
query_creation_gastos = """
create table if not exists gastos (
    gastos_id SERIAL primary key,
    anio INT not null,
    totalcompra NUMERIC , 
    producfarma NUMERIC , 
    materialsani NUMERIC , 
    implantes NUMERIC , 
    restomateriasani NUMERIC , 
    servcontratado NUMERIC , 
    trabajocontratado NUMERIC , 
    xrestocompras NUMERIC , 
    variaexistencias NUMERIC , 
    servexteriores NUMERIC , 
    sumistro NUMERIC , 
    xrestoserviexter NUMERIC , 
    gastopersonal NUMERIC , 
    sueldos NUMERIC , 
    indemnizacion NUMERIC , 
    segsocempresa NUMERIC , 
    otrgassocial NUMERIC , 
    dotaamortizacion NUMERIC , 
    perdidadeterioro NUMERIC , 
    xrestogasto NUMERIC , 
    totcompragasto NUMERIC,
    ncodi INT references hospitales(ncodi)
);
"""

# Ingresos hospitalizaciones 
query_creation_ingresos = """
create table if not exists ingresos (
    id_ingresos serial primary key,
    anio INT not null,
    particulares NUMERIC,
    aseguradoras NUMERIC,
    aseguradoras_enfermedad NUMERIC,
    aseguradoras_trafico NUMERIC,
    mutuas NUMERIC,
    ncodi INT references hospitales(ncodi),
    tipo_id INT references tipo_hospitalizacion(tipo_id)
);"""


# Inserción de valores en hospitales

query_insert_hospitales = """
    INSERT INTO hospitales
    VALUES (%s, %s)
"""

query_insert_tipo_hosp = """
    INSERT INTO tipo_hospitalizacion (nombre)
    VALUES (%s)
"""

query_insert_hospitales = """
    INSERT INTO gastos (
        anio,
        ncodi,
        total_compra,
        productos_farmaceuticos,
        material_sanitario,
        implantes,
        resto_material_sanitario,
        servicios_contratados,
        trabajos_contratados,
        resto_compras,
        resto_servicios_externos,
        gasto_personal,
        sueldos,
        indemnizacion,
        seguridad_social_empresa,
        otros_gastos_sociales,
        dotacion_amortizacion,
        perdida_deterioro,
        resto_gasto,
        total_compra_gasto
    )
    VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
        %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
    )
"""

query_insert_ingresos = """
    INSERT INTO ingresos (
        anio,
        ncodi,
        particulares,
        aseguradoras,
        aseguradoras_enfermedad,
        aseguradoras_trafico,
        mutuas,
        tipo
    )
    VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s
    )
"""