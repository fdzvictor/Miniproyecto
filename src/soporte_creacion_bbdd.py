query1 = """CREATE TABLE centro_hospitalario (
    id_centro SERIAL PRIMARY KEY
    ncodi FLOAT
);
"""
query2 = """CREATE TABLE tipo_hospitalizacion (
    id_tipo PRIMARY KEY,
    id_ingresos INT NOT NULL,
    FOREIGN KEY (id_ingreso)
        REFERENCES ingresos(id_ingreso)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
"""
query3 = """CREATE TABLE gastos (
    id_gasto SERIAL PRIMARY KEY,
    anio INT NOT NULL,
    ncodi INT,
    total_compra DECIMAL,
    productos_farmaceuticos DECIMAL,
    material_sanitario DECIMAL,
    implantes DECIMAL,
    resto_material_sanitario DECIMAL,
    servicios_contratados DECIMAL,
    trabajos_contratados DECIMAL,
    resto_compras DECIMAL,
    resto_servicios_externos DECIMAL,
    gasto_personal DECIMAL,
    sueldos DECIMAL,
    indemnizacion DECIMAL,
    seguridad_social_empresa DECIMAL,
    otros_gastos_sociales DECIMAL,
    dotacion_amortizacion DECIMAL,
    perdida_deterioro DECIMAL,
    resto_gasto DECIMAL,
    total_compra_gasto DECIMAL,
    FOREIGN KEY (ncodi)
        REFERENCES centro_hospitalario(ncodi)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
"""
query4 = """CREATE TABLE ingresos (
    id_ingreso SERIAL PRIMARY KEY,
    anio INT NOT NULL,
    ncodi NUMERIC(10, 2),
    particulares DECIMAL,
    aseguradoras DECIMAL,
    aseguradoras_enfermedad DECIMAL,
    aseguradoras_trafico DECIMAL,
    mutuas DECIMAL,
    tipo VARCHAR(50),
    FOREIGN KEY (ncodi)
        REFERENCES centro_hospitalario(ncodi)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
"""