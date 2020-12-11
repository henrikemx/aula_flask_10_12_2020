DROP TABLE IF EXISTS entradas;
-- cria tabela para guardar os posts do blog
CREATE TABLE entradas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo STRING NOT NULL,
    texto STRING NOT NULL
);
