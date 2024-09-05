CREATE DATABASE UsuariosDB;

USE UsuariosDB;

CREATE TABLE Usuarios (
    Codigo INT PRIMARY KEY AUTO_INCREMENT,
    Nome VARCHAR(100),
    CPF VARCHAR(11),
    Data_Nascimento DATE,
    Endereco VARCHAR(255),
    Sexo CHAR(1),
    Email VARCHAR(100)
);

INSERT INTO Usuarios (Nome, CPF, Data_Nascimento, Endereco, Sexo, Email)
VALUES 
('João Silva', '12345678901', '1990-01-01', 'Rua A, 123', 'M', 'joao.silva@email.com'),
('Maria Souza', '23456789012', '1985-05-15', 'Avenida B, 456', 'F', 'maria.souza@email.com'),
('Carlos Pereira', '34567890123', '1978-07-22', 'Rua C, 789', 'M', 'carlos.pereira@email.com'),
('Ana Oliveira', '45678901234', '1992-11-30', 'Rua D, 321', 'F', 'ana.oliveira@email.com'),
('Lucas Lima', '56789012345', '1988-03-10', 'Avenida E, 654', 'M', 'lucas.lima@email.com'),
('Fernanda Costa', '67890123456', '1995-08-17', 'Rua F, 987', 'F', 'fernanda.costa@email.com'),
('Paulo Almeida', '78901234567', '1983-12-02', 'Rua G, 159', 'M', 'paulo.almeida@email.com'),
('Juliana Santos', '89012345678', '1991-06-20', 'Avenida H, 753', 'F', 'juliana.santos@email.com'),
('Ricardo Martins', '90123456789', '1979-04-14', 'Rua I, 951', 'M', 'ricardo.martins@email.com'),
('Patrícia Fernandes', '01234567890', '1986-09-25', 'Rua J, 852', 'F', 'patricia.fernandes@email.com'),
('André Gonçalves', '12345098765', '1984-05-30', 'Avenida K, 147', 'M', 'andre.goncalves@email.com'),
('Mariana Ribeiro', '23456109876', '1993-02-19', 'Rua L, 753', 'F', 'mariana.ribeiro@email.com'),
('Bruno Costa', '34567210987', '1987-10-08', 'Rua M, 159', 'M', 'bruno.costa@email.com'),
('Laura Mendes', '45678321098', '1990-07-25', 'Avenida N, 369', 'F', 'laura.mendes@email.com'),
('Eduardo Azevedo', '56789432109', '1981-01-13', 'Rua O, 951', 'M', 'eduardo.azevedo@email.com'),
('Camila Moreira', '67890543210', '1989-11-04', 'Rua P, 753', 'F', 'camila.moreira@email.com'),
('Felipe Rocha', '78901654321', '1994-12-22', 'Avenida Q, 456', 'M', 'felipe.rocha@email.com'),
('Roberta Silva', '89012765432', '1982-08-17', 'Rua R, 123', 'F', 'roberta.silva@email.com'),
('Thiago Neves', '90123876543', '1976-06-06', 'Rua S, 852', 'M', 'thiago.neves@email.com'),
('Carolina Nogueira', '01234987654', '1980-03-27', 'Avenida T, 654', 'F', 'carolina.nogueira@email.com');
