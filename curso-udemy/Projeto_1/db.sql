/**
Esse banco de dados é um projeto visando integração entre um sistema python e
uma aplicação web. Modelo voltado para restaurante/pizzaria ou qualquer negócio que lide
com venda de produtos e consumo por atendimento presencial funcionário/cliente.
**/

create database erp;

/**
Essa tabela armazena os cadastros. Ele contem o nome de usuario, senha e o nivel.
Esse nível pode ser de administrador, cliente, funcionário
**/
create table cadastros(
    usuario varchar(50) not null,
    senha varchar(8) not null,
    nivel int not null
);

insert into cadastros values ('admin', 'admin', 2);

/**
Esse é onde os produtos vendidos pela loja estão armazenados.
O grupo do produto, nesse caso, é se é uma bebida ou hamburguer. Coisas que classificam o produto
**/
create table produtos(
    id int auto_increment not null primary key,
    nome varchar(100) not null,
    ingredientes varchar(1000),
    grupo varchar(100),
    preco decimal(3,2)
);

/**
Armazena os pedidos do sistema web (Não desenvolvido).
Assim que o pedido é concluido, ele é excluido da tabela e é enviado para
a tabela estatisticaVendido.
**/
create table pedidos(
    id int not null primary key auto_increment,
    nome varchar(100) not null,
    ingredientes varchar(1000),
    grupo varchar(100),
    localEntrega varchar(500),
    observacoes tinytext
);

insert into pedidos (nome, ingredientes, grupo, localEntrega, observacoes) values
    ('pizza de mussarela', 'mussarela', 'pizzas', '', 'sem cebola'),
    ('coca', '', 'bebidas', '', '');

/**
Armazena todos os pedidos feitos a fim de gerar estatísticas sobre venda
Tempo de armazenamento é determidado pelo dono do negócio que usa o sistema.
**/
create table estatisticaVendido(
    id int not null primary key auto_increment,
    nome varchar(100) not null,
    grupo varchar(100),
    preco decimal(6,2)
);

insert into estatisticaVendido(nome, grupo, preco) values
    ('pizza de mussarela', 'pizzas', 34.90),
    ('coca', 'bebidas', 6),
    ('pizza de portuguesa', 'pizzas', 34.90),
    ('suco de laranja', 'pizzas', 7);
